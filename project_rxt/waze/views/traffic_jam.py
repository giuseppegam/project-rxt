"""TrafficJamView class."""
from django.contrib.gis.geos import Point
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from waze.models import City, RoadType, Street, TrafficJam
from waze.serializers import TrafficJamSerializer


class TrafficJamView(APIView):
    """TrafficJamView class."""

    def get(self, request, *args, **kwargs):
        """Get method."""
        filter = request.query_params.get('filter-open')
        print(f'Get Query TRaffic Jam method. filter-open: {filter}')
        if filter:
            traffic_alerts = TrafficJam.objects.filter(
                finished_at__isnull=True)
            print(f'Traffic_jam_open qty: {len(traffic_alerts)}')
            serializer = TrafficJamSerializer(traffic_alerts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No filter applied'},
                            status=status.HTTP_400)

    def post(self, request):
        """ Post method."""

        list_serializer = []
        list_jams = []
        for jam in request.data:
            try:
                uuid_id = jam.get('uuid')
                uuid_object = TrafficJam.objects.get(uuid=uuid_id)
                uuid_object.update_at = timezone.now()
                uuid_object.save()
            except TrafficJam.DoesNotExist:

                if jam['line'] is not None:
                    list_lines = []
                    for line_location in jam['line']:
                        line_point = Point(line_location['x'], line_location['y'])
                        line_object = {'line': line_point}
                        list_lines.append(line_object)
                    jam['line'] = list_lines

                list_segments = []
                if jam['segment'] is not None:
                    segments = jam['segment']
                    # Create a list of segments
                    list_segments = []
                    for segment_data in segments:
                        segment_object = {
                            'id_waze': segment_data['ID'],
                            'from_node': segment_data['fromNode'],
                            'to_node': segment_data['toNode'],
                            'is_forward': segment_data['isForward']
                        }

                        list_segments.append(segment_object)

                    jam['segment'] = list_segments

                # Check if street is not None
                street_name = jam['street']
                if street_name not in ['']:
                    try:
                        street_object = Street.objects.get(name=street_name)
                    except Street.DoesNotExist:
                        street_object = Street.objects.create(name=street_name)
                    jam['street'] = street_object.pk
                else:
                    jam['street'] = None

                city_name = jam.get('city')
                city = City.objects.get(name=city_name)
                jam['city'] = city.pk

                road_type_value = jam.get('road_type')
                road_type = RoadType.objects.get(value=road_type_value)
                jam['road_type'] = road_type.pk

                list_jams.append(jam)

        serializer = TrafficJamSerializer(data=list_jams, many=True)

        if serializer.is_valid():
            serializer.save()
            list_serializer.append(serializer.data)
            return Response(list_serializer,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        """Put method."""
        at = timezone.now()
        updated_jams = []
        filter_update_open = self.request.query_params.get(
            'update-at-open',
            None)
        filter_finished_open = self.request.query_params.get(
            'finished-at-open',
            None)
        print(f'Get Query Set Traffic Jam. update-at-open: {filter}')

        if filter_update_open:
            for jam in request.data:

                try:
                    traffic_jam = TrafficJam.objects.get(
                        uuid=jam['uuid'])
                    traffic_jam.updated_at = at
                    traffic_jam.save()
                    updated_jams.append(traffic_jam)
                except TrafficJam.DoesNotExist as e:
                    print(f'Exception: {e}')
                    return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = TrafficJamSerializer(updated_jams, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if filter_finished_open:
            for jam in request.data:
                try:
                    traffic_jam = TrafficJam.objects.get(
                        uuid=jam['uuid'])
                    traffic_jam.finished_at = at
                    traffic_jam.save()
                    updated_jams.append(traffic_jam)

                except TrafficJam.DoesNotExist as e:
                    print(f'Exception: {e}')
                    return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = TrafficJamSerializer(updated_jams, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

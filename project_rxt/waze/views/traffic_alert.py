"""TrafficAlertView class."""
from django.contrib.gis.geos import Point
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from waze.models import (AlertSubtype, AlertType, City, RoadType, Street,
                         TrafficAlert)
from waze.serializers import TrafficAlertSerializer


# Create your views here.
class TrafficAlertView(APIView):
    """TrafficAlertView class."""

    def get(self, request):
        """Get method."""
        filter = request.query_params.get('filter-open')
        print(f'Get Query Set method. filter-open: {filter}')
        if filter:
            traffic_alerts = TrafficAlert.objects.filter(
                finished_at__isnull=True)
            print(f'Traffic_alerts_open qty: {len(traffic_alerts)}')
            serializer = TrafficAlertSerializer(traffic_alerts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No filter applied'},
                            status=status.HTTP_400)

    def post(self, request):
        """Post method."""
        list_serialazer = []
        list_alerts = []
        for alert in request.data:
            try:
                uuid = alert.get('uuid')
                uuid_object = TrafficAlert.objects.get(uuid=uuid)
                uuid_object.update_at = timezone.now()
                uuid_object.save()
            except TrafficAlert.DoesNotExist:
                road_type_value = alert.get('road_type')
                road_type = RoadType.objects.get(value=road_type_value)
                alert['road_type'] = road_type.pk

                city_name = alert.get('city')
                city = City.objects.get(name=city_name)
                alert['city'] = city.pk

                # Search for the alert subtype
                alert_type = alert.get('type')
                alert_type_object = AlertType.objects.get(
                    name__contains=alert_type)

                # Check if the alert has a subtype
                if alert['subtype'] == '' or alert['subtype'] is None:
                    alert_subtype_name = 'NO_SUBTYPE'
                else:
                    alert_subtype_name = alert.get('subtype')

                alert_subtype = AlertSubtype.objects.get(
                    alert_type=alert_type_object.pk, name=alert_subtype_name)
                alert['subtype'] = alert_subtype.pk

                location = alert.get('location')
                lon = location.get('x')
                lat = location.get('y')

                street_name = alert.get('street')

                if alert['street'] not in ['']:
                    try:
                        street = Street.objects.get(name=street_name)
                    except Street.DoesNotExist:
                        street = Street.objects.create(name=street_name)
                    alert['street'] = street.pk
                else:
                    alert['street'] = None

                # Create a Point object
                point = Point(lon, lat)

                # Now you can use point when creating the object
                alert['location'] = point
                list_alerts.append(alert)

        serializer = TrafficAlertSerializer(data=list_alerts, many=True)
        if serializer.is_valid():
            serializer.save()
            list_serialazer.append(serializer.data)
            return Response(list_serialazer, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        at = timezone.now()
        updated_alerts = []
        filter_update_open = self.request.query_params.get(
            'update-at-open',
            None)
        filter_finished_open = self.request.query_params.get(
            'finished-at-open',
            None)
        print(f'Get Query Set method. update-at-open: {filter}')
        if filter_update_open:
            for alert in request.data:
                # print(f'alert: {alert}')
                try:
                    traffic_alert = TrafficAlert.objects.get(
                        uuid=alert['uuid'])
                    traffic_alert.updated_at = at
                    traffic_alert.save()
                    updated_alerts.append(traffic_alert)
                except TrafficAlert.DoesNotExist as e:
                    print(f'Exception: {e}')
                    return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = TrafficAlertSerializer(updated_alerts, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if filter_finished_open:
            for alert in request.data:
                try:
                    traffic_alert = TrafficAlert.objects.get(
                        uuid=alert['uuid'])
                except TrafficAlert.DoesNotExist as e:
                    print(f'Exception: {e}')
                    return Response(status=status.HTTP_404_NOT_FOUND)
                try:
                    traffic_alert.finished_at = at
                    traffic_alert.save()
                    updated_alerts.append(traffic_alert)
                except Exception as e:
                    print(f'Exception: {e}')
                    return Response(status=status.HTTP_400_BAD_REQUEST)

            serializer = TrafficAlertSerializer(updated_alerts, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

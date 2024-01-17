""" Serializers for traffic jams."""
from rest_framework import serializers

from waze.models import Line, Segment, TrafficJam
from waze.serializers import LineSerializer, SegmentSerializer


class TrafficJamSerializer(serializers.ModelSerializer):
    """TrafficJamSerializer class."""
    line = LineSerializer(many=True)
    segment = SegmentSerializer(many=True)

    class Meta:
        """Meta class."""

        model = TrafficJam
        fields = (
            'uuid',
            'pubMillis',
            'line',
            'segment',
            'speed',
            'speedKPH',
            'length',
            'delay',
            'street',
            'city',
            'road_type',
            'start_node',
            'end_node',
            'level',
            'turn_type',
            'blocking_alert_uuid',
            'finished_at',
            'created_at', 'updated_at', 'deleted_at')
        read_only_fields = ('created_at', 'updated_at', 'deleted_at')       

    def create(self, validated_data):
        lines_data = validated_data.pop('line')
        segment_data = validated_data.pop('segment')
        traffic_jam = TrafficJam.objects.create(**validated_data)
        for line_data in lines_data:
            Line.objects.create(traffic_jam=traffic_jam, **line_data)
        for segment_data in segment_data:
            Segment.objects.create(traffic_jam=traffic_jam, **segment_data)
        return traffic_jam

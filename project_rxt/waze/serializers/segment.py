from rest_framework import serializers

from waze.models import Segment


class SegmentSerializer(serializers.ModelSerializer):
    """SegmentSerializer class."""

    class Meta:
        """Meta class."""

        model = Segment
        fields = ('id', 'id_waze', 'from_node', 'to_node', 'traffic_jam',
                  'unusual_traffic', 'is_forward', 'created_at', 'updated_at', 'deleted_at')
        read_only_fields = ('created_at', 'updated_at', 'deleted_at')
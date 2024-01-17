from rest_framework import serializers

from waze.models import Line


class LineSerializer(serializers.ModelSerializer):
    """LineSerializer class."""

    class Meta:
        """Meta class."""

        model = Line
        fields = ('id', 'line', 'traffic_jam', 'created_at',
                  'updated_at', 'deleted_at')
        read_only_fields = ('created_at', 'updated_at', 'deleted_at')

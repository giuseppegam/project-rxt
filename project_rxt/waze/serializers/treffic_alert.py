"""Serializer class for TrafficAlert model."""

from rest_framework import serializers

from waze.models import TrafficAlert


class TrafficAlertSerializer(serializers.ModelSerializer):
    """Serializer class for TrafficAlert model."""

    class Meta:
        """Meta class for TrafficAlertSerializer."""
        model = TrafficAlert
        fields = ('uuid', 'pubMillis', 'location', 'magvar', 'subtype',
                  'report_description', 'street', 'city', 'road_type',
                  'report_rating', 'jam_uuid', 'reliability', 'confidence',
                  'report_by_municipality_user', 'n_thumbs_up', 'finished_at',
                  'created_at', 'updated_at', 'deleted_at', )
        read_only_fields = ('created_at', 'updated_at', 'deleted_at')

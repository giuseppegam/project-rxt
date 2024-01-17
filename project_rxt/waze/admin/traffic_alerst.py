"""Waze traffic alerts admin module."""
from django.contrib.gis import admin

from waze.models import TrafficAlert

from .abstract import BaseModelGISAdmin


@admin.register(TrafficAlert)
class TrafficAlertAdmin(BaseModelGISAdmin):
    """Admin class for TrafficAlerts model."""
    list_display = ('uuid', 'pubMillis', 'city', 'street', 'location', 'magvar',
                    'alert_type', 'subtype', 'reliability',
                    'confidence', 'report_by_municipality_user',
                    'n_thumbs_up', 'finished_at')

    readonly_fields = ('created_at', 'updated_at', 'deleted_at')

    fieldsets = (
        ('Traffic Alert', {
            'fields': (
                'uuid', 'pubMillis', 'location', 'magvar', 'subtype',
                'report_description', 'street', 'city', 'road_type',
                'report_rating', 'jam_uuid', 'reliability', 'confidence',
                'report_by_municipality_user', 'n_thumbs_up', 'finished_at'
            )
        }),
        ('Audit Log', {
            'fields': ('created_at', 'updated_at', 'deleted_at')
        }),
    )

    def alert_type(self, obj):
        return obj.subtype.alert_type

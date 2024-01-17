"""Admin class for TrafficJams model."""
from django.contrib.gis import admin

from waze.models import TrafficJam

from .abstract import BaseModelGISAdmin


@admin.register(TrafficJam)
class TrafficJamsAdmin(BaseModelGISAdmin):
    """Admin class for TrafficJams model."""
    list_display = ('uuid', 'pubMillis', 'speed', 'speedKPH',
                    'length', 'delay', 'city', 'road_type',
                    'start_node', 'end_node', 'level', 'turn_type',
                    'blocking_alert_uuid', 'created_at', 'updated_at',
                    'deleted_at', 'finished_at')

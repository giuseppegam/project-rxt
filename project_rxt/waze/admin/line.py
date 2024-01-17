from django.contrib.gis import admin

from waze.models import Line


@admin.register(Line)
class LineAdmin(admin.GISModelAdmin):
    """Admin class for Line model."""
    map_template = 'gis/admin/openlayers.html'  # Add this line
    gis_widget_kwargs = {
        'attrs': {
            'default_lat': -20.477163,
            'default_lon': -54.616323,
            'default_zoom': 15,
            'display_raw': True,
        }
    }
    list_select_related = True
    list_display = ('id', 'line', 'traffic_jam', 'created_at', 'deleted_at')
    fieldsets = (
        ('Line', {
            'fields': ('line', 'traffic_jam')
        }),
    )

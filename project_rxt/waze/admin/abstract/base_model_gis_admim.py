"""We define the Base Model Admin GiS class here."""
from typing import Tuple

from django.contrib.gis import admin
from django.urls import reverse
from django.utils.html import format_html


class BaseModelGISAdmin(admin.GISModelAdmin):
    """
    Base ModelAdmin class that provides common configuration for Django Admin.
    """
    map_template = 'gis/admin/openlayers.html'  # Add this line
    gis_widget_kwargs = {
        'attrs': {
            'default_lat': -20.477163,
            'default_lon': -54.616323,
            'default_zoom': 15,
            'display_raw': True,
        }
    }

    common_fields = ('created_at', 'updated_at', 'deleted_at')
    list_display: Tuple[str, ...] = common_fields + ('view_changes',)
    list_filter = common_fields
    search_fields = common_fields
    ordering = common_fields
    readonly_fields: Tuple[str, ...] = common_fields
    date_hierarchy = 'created_at'
    empty_value_display = '-empty-'
    list_select_related = True
    save_on_top = True
    show_full_result_count = True
    show_change_link = True
    show_full_result_count = True

    def view_changes(self, obj):
        """View changes method."""
        url = reverse('admin:auditlog_logentry_changelist')
        url += f'?object_id={obj.id}'
        return format_html('<a href="{}">View changes</a>', url)

    class Meta:
        """
        Contains optional metadata for the GIS model like table name, ordering, etc.
        """
        abstract = True

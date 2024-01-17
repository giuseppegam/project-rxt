"""We are using the Django admin site to manage the RoadType model."""
from django.contrib import admin

from waze.models import RoadType

from .abstract import BaseModelAdmin as base


@admin.register(RoadType)
class RoadTypeAdmin(base):
    """
    Django admin class for RoadType model. Inherits from the base ModelAdmin.
    Adds specific fields for RoadType to the common fields defined in the base.
    """
    fieldsets = (
        ('Road Type', {
            'fields': ('value', 'type', 'description', 'is_active')
        }),
        ('Audit Log', {
            'fields': ('created_at', 'updated_at', 'deleted_at')
        }),
    )

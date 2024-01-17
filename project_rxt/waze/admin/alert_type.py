"""Waze AlertType admin class."""
from django.contrib import admin

from waze.models import AlertType

from .abstract import BaseModelAdmin as base


# Register your models here.
@admin.register(AlertType)
class AlertTypeAdmin(base):
    """
    Django admin class for AlertType model. Inherits from the base ModelAdmin.
    Adds specific fields for AlertType to common fields defined in the base.
    """
    list_display = ('name', 'description', 'is_active')
    fieldsets = (
        ('Alert Type', {
            'fields': ('name', 'description', 'is_active')
        }),
        ('Audit Log', {
            'fields': ('created_at', 'updated_at', 'deleted_at')
        }),
    )

"""We are using the Django admin site to manage the AlertSubtype model."""
from django.contrib import admin

from waze.models import AlertSubtype

from .abstract import BaseModelAdmin as base


# Register your models here.
@admin.register(AlertSubtype)
class AlertSubtypeAdmin(base):
    """
    Django admin class for AlertSubtype model. Inherits from 
    the base ModelAdmin.
    Adds specific fields for AlertSubtype to the common fields 
    defined in the base.
    """
    list_display = ('name', 'description', 'alert_type', 'is_active')
    fieldsets = (
        ('Alert SubType', {
            'fields': ('name', 'description', 'alert_type', 'is_active')
        }),
        ('Audit Log', {
            'fields': ('created_at', 'updated_at', 'deleted_at')
        }),
    )

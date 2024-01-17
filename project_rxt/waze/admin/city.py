from django.contrib import admin

from waze.models import City

from .abstract import BaseModelAdmin as base


# Register your models here.
@admin.register(City)
class CityAdmin(base):
    """
    City Admin
    """
    list_display = ('name', 'is_active', 'country')
    ordering = ('name',)
    fieldsets = (
        ('City', {
            'fields': ('name', 'is_active', 'country')
        }),
        ('Audit Log', {
            'fields': ('created_at', 'updated_at', 'deleted_at')
        }),
    )
from django.contrib import admin

from waze.models import Country

from .abstract import BaseModelAdmin as base


# Register your models here.
@admin.register(Country)
class CountryAdmin(base):
    """
    Country Admin
    """
    list_display = ('name', 'acronym', 'is_active')
    ordering = ('name',)
    fieldsets = (
        ('Country', {
            'fields': ('name', 'acronym', 'is_active')
        }),
        ('Audit Log', {
            'fields': ('created_at', 'updated_at', 'deleted_at')
        }),
    )
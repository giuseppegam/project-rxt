"""We are using the Django admin site to manage the models."""
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html


class BaseModelAdmin(admin.ModelAdmin):
    """
    Base ModelAdmin class that provides common configuration for Django Admin.
    Includes fields for creation, update, and deletion timestamps, and a link to view changes.
    """

    common_fields = ('created_at', 'updated_at', 'deleted_at')
    list_display = common_fields + ('view_changes',)
    list_filter = common_fields
    search_fields = common_fields
    ordering = common_fields
    readonly_fields = ('id',) + common_fields
    date_hierarchy = 'created_at'
    empty_value_display = '-empty-'
    list_select_related = True
    save_on_top = True
    show_full_result_count = True
    show_change_link = True
    show_full_result_count = True

    def view_changes(self, obj):
        url = reverse('admin:auditlog_logentry_changelist')
        url += f'?object_id={obj.id}'
        return format_html('<a href="{}">View changes</a>', url)
    view_changes.short_description = 'Change history'

    class Meta:
        """
        Contains optional metadata for the GIS model like table name, ordering, etc.
        """
        abstract = True

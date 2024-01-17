"""Waze alert subtype model."""
from auditlog.registry import auditlog
from django.db import models

from .abstract import Base


class AlertSubtype(Base):
    """
    Represents different subtypes of alerts in the Waze for Cities program.
    """
    id: models.AutoField = models.AutoField(primary_key=True)
    name: models.CharField = models.CharField(
        max_length=60, null=False, blank=False)
    description: models.CharField = models.CharField(
        max_length=255, null=True, blank=True)
    alert_type: models.ForeignKey = (
        models.ForeignKey(
            'AlertType', on_delete=models.PROTECT, null=False, blank=False))
    is_active: models.BooleanField = models.BooleanField(
        default=True, null=False, blank=False)

    def __str__(self):
        return str(self.name)  # Convert name to string representation

    class Meta:
        db_table = 'alert_subtype'


auditlog.register(AlertSubtype)

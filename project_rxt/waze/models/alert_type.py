"""We define the AlertType model here."""
from auditlog.registry import auditlog
from django.db import models

from .abstract import Base


class AlertType(Base):
    """
    Represents different types of alerts in the Waze for Cities partner program.
    """
    id: models.AutoField = models.AutoField(primary_key=True)
    name: models.CharField = models.CharField(
        max_length=30, unique=True, null=False, blank=False)
    description: models.CharField = models.CharField(
        max_length=255, null=True, blank=True)
    is_active: models.BooleanField = models.BooleanField(
        default=True, null=False, blank=False)

    def __str__(self):
        return str(self.name)  # Convert name to string representation

    class Meta:
        db_table = 'alert_type'


auditlog.register(AlertType)

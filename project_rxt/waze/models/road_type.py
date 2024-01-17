"""We define the RoadsType model here."""
from auditlog.registry import auditlog
from django.db import models

from .abstract.abstract_base import Base


class RoadType(Base):
    """
    Represents different road types in the Waze for Cities partner program.
    """
    id: models.AutoField = models.AutoField(primary_key=True)
    value: models.IntegerField = models.IntegerField(
        unique=True, null=False, blank=False)
    type: models.CharField = models.CharField(
        max_length=30, unique=True, null=False, blank=False)
    description: models.CharField = models.CharField(
        max_length=255, null=True, blank=True)
    is_active: models.BooleanField = models.BooleanField(
        default=True, null=False, blank=False)

    def __str__(self):
        return str(self.type)  # Convert name to string representation

    class Meta:
        db_table = 'road_type'


auditlog.register(RoadType)

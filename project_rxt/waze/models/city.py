""" This module contains the City model. """
from auditlog.registry import auditlog
from django.db import models

from .abstract import Base


class City(Base):
    """
    Represents a city in the Waze for Cities partner program.
    """
    id: models.AutoField = models.AutoField(primary_key=True)
    name: models.CharField = models.CharField(
        max_length=255, unique=True, null=False, blank=False)
    country: models.ForeignKey = (
        models.ForeignKey(
            'Country', on_delete=models.CASCADE, blank=False, null=False))
    is_active: models.BooleanField = models.BooleanField(
        default=True, null=False, blank=False)

    def __str__(self):
        return str(self.name)  # Convert name to string representation

    class Meta:
        """ Meta class for City model."""
        db_table = 'city'


auditlog.register(City)

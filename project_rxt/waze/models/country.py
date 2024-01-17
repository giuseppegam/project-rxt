""" This module contains the Country model. """
from auditlog.registry import auditlog
from django.db import models

from .abstract import Base


class Country(Base):
    """
    Represents a country in the Waze for Cities partner program.
    """
    id: models.AutoField = models.AutoField(primary_key=True)
    name: models.CharField = models.CharField(
        max_length=90, unique=True, null=False, blank=False)
    acronym: models.CharField = models.CharField(
        max_length=3, unique=True, null=False, blank=False)
    is_active: models.BooleanField = models.BooleanField(
        default=True, null=False, blank=False)

    def __str__(self):
        return str(self.name)  # Convert name to string representation

    class Meta:
        db_table = 'country'


auditlog.register(Country)

""" Street model. """
from auditlog.registry import auditlog
from django.db import models

from .abstract import Base


class Street(Base):
    """Represents a street."""
    id: models.AutoField = models.AutoField(
        primary_key=True, blank=False, null=False)

    name: models.CharField = models.CharField(
        max_length=255, blank=False, null=False, unique=True)

    def __str__(self):
        return str(self.name)  # Convert name to string representation

    class Meta:
        db_table = 'street'


auditlog.register(Street)

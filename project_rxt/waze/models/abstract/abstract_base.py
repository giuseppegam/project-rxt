"""Module providing models for the waze app."""
from django.db import models


class Base(models.Model):
    """Class representing a base models for all models in the project."""
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)
    deleted_at: models.DateTimeField = models.DateTimeField(
        null=True, blank=True)

    class Meta:
        """
        Contains optional metadata for the model like table name, ordering, etc.
        """
        abstract = True

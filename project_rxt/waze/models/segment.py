""" This module defines the Segments class. """
from django.db import models

from .abstract import Base


class Segment(Base):

    """ We define the Segments class here. """

    id: models.AutoField = models.AutoField(primary_key=True)
    id_waze: models.IntegerField = models.IntegerField(
        blank=False, null=False)
    from_node: models.IntegerField = models.IntegerField(
        blank=False, null=False)
    to_node: models.IntegerField = models.IntegerField(
        blank=False, null=False)
    traffic_jam: models.ForeignKey = models.ForeignKey(
        'TrafficJam',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='segment'
    )
    unusual_traffic: models.ForeignKey = models.ForeignKey(
        'UnusualTraffic',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    is_forward: models.BooleanField = models.BooleanField(
        null=False)

    def __str__(self):
        return str(self.id)  # Convert name to string representation

    class Meta:
        """ Meta class for City model."""
        db_table = 'segment'

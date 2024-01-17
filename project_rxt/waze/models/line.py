"""We define the Line class here."""
from django.contrib.gis.db import models as gis
from django.db import models

from .abstract import Base


class Line(Base):
    """
    Represents different subtypes of alerts in the Waze for Cities partner program.
    """
    id: models.AutoField = models.AutoField(primary_key=True)
    traffic_jam: models.ForeignKey = models.ForeignKey(
        'TrafficJam',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='line')
    unusual_traffic: models.OneToOneField = models.OneToOneField(
        'UnusualTraffic', on_delete=models.PROTECT, blank=True, null=True,
        related_name='line_related_unusual_traffic')
    line: gis.PointField = gis.PointField(
        blank=False, null=False)

    def __str__(self):
        # Convert name to string representation
        return str(self.id)  # Convert name to string representation

    class Meta:
        db_table = 'line'

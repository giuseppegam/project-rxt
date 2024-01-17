"""We define the TrafficJams class here."""
from auditlog.registry import auditlog
from django.db import models

from .abstract import Base


class TrafficJam(Base):
    """
    Represents different subtypes of alerts in the Waze for Cities
    partner program.
    """
    uuid: models.BigIntegerField = models.BigIntegerField(primary_key=True)
    pubMillis: models.DateTimeField = models.DateTimeField(
        blank=True, null=True)
    speed: models.FloatField = models.FloatField(blank=False, null=False)
    speedKPH: models.FloatField = models.FloatField(blank=False, null=False)
    length: models.IntegerField = models.IntegerField(blank=False, null=False)
    delay: models.IntegerField = models.IntegerField(blank=False, null=False)
    street: models.ForeignKey = models.ForeignKey(
        'Street', on_delete=models.PROTECT, blank=True, null=True)
    city: models.ForeignKey = models.ForeignKey(
        'City', on_delete=models.PROTECT, blank=False, null=False)
    road_type: models.ForeignKey = models.ForeignKey(
        'RoadType', on_delete=models.PROTECT, blank=False, null=False)
    start_node: models.CharField = models.CharField(
        max_length=255, blank=True, null=True)
    end_node: models.CharField = models.CharField(
        max_length=255, blank=True, null=True)
    level: models.IntegerField = models.IntegerField()
    turn_type: models.CharField = models.CharField(
        max_length=5, blank=True, null=True)
    blocking_alert_uuid: models.CharField = models.CharField(
        max_length=255, blank=True, null=True)
    finished_at: models.DateTimeField = models.DateTimeField(
        blank=True, null=True)

    def __str__(self):
        return str(self.uuid)  # Convert name to string representation

    class Meta:
        db_table = 'traffic_jam'


auditlog.register(TrafficJam)

"""We define the UnsusualTraffic class here."""
from auditlog.registry import auditlog
from django.db import models

from .abstract import Base


class UnusualTraffic(Base):
    """
    Represents different subtypes of alerts in the Waze for Cities partner program.
    """
    id: models.AutoField = models.AutoField(primary_key=True)
    detection_time: models.TimeField = models.TimeField()
    detection_date_millis: models.IntegerField = models.IntegerField()
    updated_date: models.TimeField = models.TimeField()
    updated_date_millis: models.IntegerField = models.IntegerField()
    type: models.CharField = models.CharField(max_length=255)
    """Irregularity type - NONE(0, "NONE"), SMALL(1, "Small"),
    MEDIUM(2, "Medium"), LARGE(3, "Large"), HUGE(4, "Huge");"""
    speed: models.FloatField = models.FloatField()
    regular_speed: models.FloatField = models.FloatField()
    delay_seconds: models.IntegerField = models.IntegerField()
    seconds: models.IntegerField = models.IntegerField()
    length: models.IntegerField = models.IntegerField()
    trend: models.IntegerField = models.IntegerField()
    """-1 improving, 0 constant, 1 getting worse"""
    street: models.ForeignKey = models.ForeignKey(
        'Street', on_delete=models.PROTECT, blank=True, null=True)
    city: models.ForeignKey = models.ForeignKey(
        'City', on_delete=models.PROTECT, blank=False, null=False)
    severity: models.FloatField = models.FloatField(blank=False, null=False)
    """1-4, 4 being worst severity"""
    jam_level: models.IntegerField = models.IntegerField()
    """1-4, 4 being worst jam level"""
    drivers_count: models.IntegerField = models.IntegerField()
    alerts_count: models.IntegerField = models.IntegerField()

    def __str__(self):
        return str(self.name)  # Convert name to string representation

    class Meta:
        db_table = 'unsusual_traffic'


auditlog.register(UnusualTraffic)

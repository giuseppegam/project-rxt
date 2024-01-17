"""We define the TrafficAlerts class here."""
from auditlog.registry import auditlog
from django.contrib.gis.db import models as gis
from django.db import models

from .abstract import Base


class TrafficAlert(Base):
    """
    Represents different subtypes of alerts in the Waze for Cities partner program.
    """
    uuid: models.CharField = models.CharField(
        primary_key=True, max_length=255, blank=False, null=False, unique=True)
    pubMillis: models.DateTimeField = models.DateTimeField(
        blank=False, null=False)
    location: gis.PointField = gis.PointField(blank=False, null=False)
    magvar: models.IntegerField = models.IntegerField()
    subtype: models.ForeignKey = (
        models.ForeignKey(
            'AlertSubtype', on_delete=models.PROTECT, blank=False, null=False))
    report_description: models.CharField = models.CharField(
        max_length=255, blank=True, null=True)
    street: models.ForeignKey = models.ForeignKey(
        'Street', on_delete=models.PROTECT, blank=True, null=True)
    city: models.ForeignKey = models.ForeignKey(
        'City', on_delete=models.PROTECT, blank=False, null=False)
    road_type: models.ForeignKey = (
        models.ForeignKey('RoadType', on_delete=models.PROTECT))
    report_rating: models.IntegerField = models.IntegerField(blank=False, null=False)
    jam_uuid: models.CharField = models.CharField(
        max_length=36, blank=True, null=True)
    reliability: models.IntegerField = models.IntegerField(
        blank=True, null=True)
    confidence: models.IntegerField = models.IntegerField()
    report_by_municipality_user: models.BooleanField = models.BooleanField(
        blank=True, null=True)
    n_thumbs_up: models.IntegerField = models.IntegerField(blank=True, null=True)
    finished_at: models.DateTimeField = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.uuid)  # Convert name to string representation

    class Meta:
        db_table = 'traffic_alert'


auditlog.register(TrafficAlert)

""" Management command to update alert subtypes from Waze API """
from django.core.management.base import BaseCommand

from waze.models import AlertSubtype, AlertType


class AlertSubtypeCommand(BaseCommand):
    """ Populate AlertSubType model with initial data """
    help = 'Populate AlertSubType model with initial data'

    def handle(self, *args, **options):
        alert_subtypes = [
            ('ACCIDENT_MAJOR', 'Major accident.', 'ACCIDENT'),
            ('ACCIDENT_MINOR', 'Minor accident.', 'ACCIDENT'),
            ('NO_SUBTYPE', 'No subtype.', 'ACCIDENT'),
            ('JAM', 'Traffic jam.', 'JAM'),
            ('JAM_MODERATE_TRAFFIC', 'Moderate traffic jam.', 'JAM'),
            ('JAM_HEAVY_TRAFFIC', 'Heavy traffic jam.', 'JAM'),
            ('JAM_STAND_STILL_TRAFFIC', 'Standstill traffic jam.', 'JAM'),
            ('JAM_LIGHT_TRAFFIC', 'Light traffic jam.', 'JAM'),
            ('NO_SUBTYPE', 'No subtype.', 'JAM'),
            ('HAZARD_ON_ROAD', 'Hazard on road.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_ON_SHOULDER', 'Hazard on shoulder.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_WEATHER', 'Weather hazard.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_ON_ROAD_OBJECT', 'Hazard on road object.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_ON_ROAD_POT_HOLE', 'Hazard on road pot hole.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_ON_ROAD_ROAD_KILL', 'Hazard on road road kill.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_ON_SHOULDER_CAR_STOPPED', 'Hazard on shoulder car stopped.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_ON_SHOULDER_ANIMALS', 'Hazard on shoulder animals.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_ON_SHOULDER_MISSING_SIGN', 'Hazard on shoulder missing sign.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_WEATHER_FOG', 'Hazard weather fog.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_WEATHER_HAIL', 'Hazard weather hail.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_WEATHER_HEAVY_RAIN', 'Hazard weather heavy rain.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_WEATHER_HEAVY_SNOW', 'Hazard weather heavy snow.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_WEATHER_FLOOD', 'Hazard weather flood.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_WEATHER_MONSOON', 'Hazard weather monsoon.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_WEATHER_TORNADO', 'Hazard weather tornado.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_WEATHER_HEAT_WAVE', 'Hazard weather heat wave.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_WEATHER_HURRICANE', 'Hazard weather hurricane.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_WEATHER_FREEZING_RAIN', 'Hazard weather freezing rain.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_ON_ROAD_LANE_CLOSED', 'Hazard on road lane closed.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_ON_ROAD_OIL', 'Hazard on road oil.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_ON_ROAD_ICE', 'Hazard on road ice.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_ON_ROAD_CONSTRUCTION', 'Hazard on road construction.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_ON_ROAD_CAR_STOPPED', 'Hazard on road car stopped.', 'WEATHERHAZARD / HAZARD'),
            ('HAZARD_ON_ROAD_TRAFFIC_LIGHT_FAULT', 'Hazard on road traffic light fault.', 'WEATHERHAZARD / HAZARD'),
            ('NO_SUBTYPE', 'No subtype.', 'WEATHERHAZARD / HAZARD'),
            ('NO_SUBTYPE', 'No subtype.', 'MISC'),
            ('NO_SUBTYPE', 'No subtype.', 'CONSTRUCTION'),
            ('NO_SUBTYPE', 'No subtype.', 'ROAD_CLOSED')
        ]

        for name, description, alert_type_name in alert_subtypes:
            alert_type = AlertType.objects.get(name=alert_type_name)
            AlertSubtype.objects.create(name=name, description=description, alert_type=alert_type)

        self.stdout.write(self.style.SUCCESS('Successfully populated AlertSubType'))

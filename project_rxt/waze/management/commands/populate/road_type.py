""" Populate RoadType model with initial data """
from django.core.management.base import BaseCommand

from waze.models import RoadType


class RoadTypeCommand(BaseCommand):
    """ Populate RoadType model with initial data """

    help = 'Populate RoadType model with initial data'

    def handle(self, *args, **options):
        road_types = [
            {'type': 'Streets', 'value': 1},
            {'type': 'Primary Street', 'value': 2},
            {'type': 'Freeways', 'value': 3},
            {'type': 'Ramps', 'value': 4},
            {'type': 'Trails', 'value': 5},
            {'type': 'Primary', 'value': 6},
            {'type': 'Secondary', 'value': 7},
            {'type': '4X4 Trails', 'value': 8},
            {'type': '4X4 Trails', 'value': 14},
            {'type': 'Ferry crossing', 'value': 15},
            {'type': 'Walkway', 'value': 9},
            {'type': 'Pedestrian', 'value': 10},
            {'type': 'Exit', 'value': 11},
            {'type': 'Stairway', 'value': 16},
            {'type': 'Private road', 'value': 17},
            {'type': 'Railroads', 'value': 18},
            {'type': 'Runway/Taxiway', 'value': 19},
            {'type': 'Parking lot road', 'value': 20},
            {'type': 'Service road', 'value': 21},
            {'type': 'NO_TYPE', 'value': 22},
        ]

        for road_type in road_types:
            RoadType.objects.create(type=road_type['type'],
                                    value=road_type['value'])

        self.stdout.write(self.style.SUCCESS(
            'Successfully populated RoadType model'))

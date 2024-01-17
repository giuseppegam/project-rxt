"""Populate AlertType model with initial data."""
from django.core.management.base import BaseCommand

from waze.models import AlertType


class AlertTypeCommand(BaseCommand):
    """Populate AlertType model with initial data"""
    help = 'Populate AlertType model with initial data'

    def handle(self, *args, **options):
        road_types = [
            {'name': 'ACCIDENT', 'description': ''},
            {'name': 'JAM', 'description': ''},
            {'name': 'WEATHERHAZARD / HAZARD', 'description': ''},
            {'name': 'MISC', 'description': ''},
            {'name': 'CONSTRUCTION', 'description': ''},
            {'name': 'ROAD_CLOSED', 'description': ''}
        ]
        
        for road_type in road_types:
            AlertType.objects.create(name=road_type['name'], description=road_type['description'])
        
        self.stdout.write(self.style.SUCCESS('Successfully populated AlertType' 
                                             'model'))

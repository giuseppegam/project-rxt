"""Run all populate commands"""""
from django.core.management.base import BaseCommand

from .populate import AlertTypeCommand, AlertSubtypeCommand, RoadTypeCommand, CountryCommand, CityCommand


class Command(BaseCommand):
    """Run all populate commands"""
    help = 'Run all populate commands'

    def handle(self, *args, **options):
        # Call each populate command individually
        AlertTypeCommand().handle(*args, **options)
        AlertSubtypeCommand().handle(*args, **options)
        RoadTypeCommand().handle(*args, **options)
        CountryCommand().handle(*args, **options)
        CityCommand().handle(*args, **options)

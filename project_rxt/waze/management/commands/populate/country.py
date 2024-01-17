""" Populate Country model with initial data """
from django.conf import settings
from django.core.management.base import BaseCommand

from waze.models import Country


class CountryCommand(BaseCommand):
    """"Populate Country model with initial data"""
    help='Populate Country model with initial data'
    def handle(self, *args, **options):
        Country.objects.create(
            name=settings.WAZE_PLACE['country_name'],
            acronym=settings.WAZE_PLACE['country_acronym'])
        self.stdout.write(self.style.SUCCESS('Country created successfully'))
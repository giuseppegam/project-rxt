"""Populate City model with initial data"""
from django.conf import settings
from django.core.management.base import BaseCommand

from waze.models import City, Country


class CityCommand(BaseCommand):
    """"Populate City model with initial data"""
    help = 'Populate City model with initial data'

    def handle(self, *args, **options):
        """Populate City model with initial data"""
        country = Country.objects.using('waze').get(
            acronym=settings.WAZE_PLACE['country_acronym'])
        City.objects.create(
            name=settings.WAZE_PLACE['city_name'], country=country)
        self.stdout.write(self.style.SUCCESS('City created successfully'))
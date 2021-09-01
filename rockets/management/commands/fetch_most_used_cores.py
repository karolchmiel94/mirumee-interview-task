from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User

from spacex_api.service import get_cores_data
from utilities.parser import parse_string_to_bool

from .exceptions import ArgumentParsingException


class Command(BaseCommand):
    help = 'Fetch most used first stages from SpaceX API'

    def add_arguments(self, parser):
        parser.add_argument('cores_number', type=int, nargs='?', default=None,
                            help='Integer number of cores to fetch.')
        parser.add_argument('-successful', type=str, default=None,
                            help='Include or exclude successful flights. Values: True / False')
        parser.add_argument('-planned', type=str, default=None,
                            help='Include or exclude planned future missions. Values: True / False')

    def handle(self, *args, **kwargs):
        cores_number = kwargs['cores_number']
        successful = kwargs['successful']
        if successful:
            try:
                successful = parse_string_to_bool(successful)
            except:
                return ArgumentParsingException('-successful').message
        planned = kwargs['planned']
        if planned:
            try:
                planned = parse_string_to_bool(planned)
            except:
                return ArgumentParsingException('-planned').message
        cores = get_cores_data(cores_number, successful, planned)
        self.stdout.write('Fetching has been finished.')
        self.stdout.write(str(cores))

# Command example: python manage.py fetch_most_used_cores 11 -successful True -planned False
# Command example: python manage.py fetch_most_used_cores 3
# Command example: python manage.py fetch_most_used_cores

from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User

from rockets.service import fetch_cores_if_not_in_database


class Command(BaseCommand):
    help = 'Populate database'

    def handle(self, *args, **options):
        for index in range(1, 4):
            user, created = User.objects.get_or_create(
                username='testuser{}'.format(index), email='', password='testpassword')
            self.stdout.write(str(user))
            self.stdout.write('Created username: {} with password: {}'.format(
                user.username, user.password))
        self.stdout.write(
            'Checking whether cores data exists and fetching it if not.')
        fetch_cores_if_not_in_database()
        self.stdout.write('Creating test data has finished.')

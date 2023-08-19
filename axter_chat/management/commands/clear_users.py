from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Clear all user records from the database'

    def handle(self, *args, **kwargs):
        # Delete all user records
        User.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('All users have been deleted.'))

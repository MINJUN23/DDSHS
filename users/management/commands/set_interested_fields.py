from django.core.management.base import BaseCommand
from users.models import FIELD_CHOICES, InterestedField


class Command(BaseCommand):
    help = 'Set InterestedFields with FIELD_CHOICES on user.models'

    def handle(self, *args, **options):
        InterestedField.objects.all().delete()
        for FIELD in FIELD_CHOICES:
            InterestedField.objects.get_or_create(field=FIELD[0])

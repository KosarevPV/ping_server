from django.core.management.base import BaseCommand

from django.contrib.auth import get_user_model


class Command(BaseCommand):

    def handle(self, *args, **options):
        get_user_model().objects.all().delete()
        get_user_model().objects.create(
            password=f'pbkdf2_sha256$260000$jg0zd4YOkKMS4o4cgtXJ2T$wi2Y4YG0vTn8PmBcCX'
                     f'6skaj7Ub8I0Y37mWMvYK64SgY=',
            is_superuser=True, username='admin', is_staff=True, email='admin@admin.com')

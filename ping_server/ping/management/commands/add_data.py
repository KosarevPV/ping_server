from django.core.management.base import BaseCommand

from django.contrib.auth import get_user_model
from ping.models import Domains
from django_celery_beat.models import PeriodicTask, IntervalSchedule


class Command(BaseCommand):

    def handle(self, *args, **options):
        Domains.objects.all().delete()
        PeriodicTask.objects.all().delete()
        IntervalSchedule.objects.all().delete()
        domains = ['github.com', 'yandex.by', 'youtube.com']
        for item in domains:
            Domains.objects.create(domain_name=item)

        get_user_model().objects.all().delete()
        get_user_model().objects.create(
            password=f'pbkdf2_sha256$600000$yMhL3L0EMVRjRTwBsCojwV$Sb+C/EdI4VKQdAnRxtkRwH4puXyJ0jVO4b3Xw9QIFeY=',
            is_superuser=True, username='admin', is_staff=True, email='admin@admin.com')

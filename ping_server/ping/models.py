import json

from django.db import models

from django.utils import timezone
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from ping_server.settings import N


class Domains(models.Model):
    """Модель доменов"""
    domain_name = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        super(Domains, self).save(*args, **kwargs)

        schedule, created = IntervalSchedule.objects.get_or_create(
            every=N,
            period=IntervalSchedule.SECONDS,
        )

        PeriodicTask.objects.create(
            name=f'Domain: {self.domain_name}',
            task='save_response_time',
            interval=schedule,
            args=json.dumps([self.pk]),
            start_time=timezone.now(),
        )


    class Meta:
        verbose_name = "Domain"
        verbose_name_plural = 'Domains'


class Responses(models.Model):
    """Модель ответов"""
    domain = models.ForeignKey(Domains, models.CASCADE)
    responses_time = models.FloatField()
    created = models.DateTimeField(auto_now_add=True, editable=False)

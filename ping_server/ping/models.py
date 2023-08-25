from django.db import models


class Domains(models.Model):
    """Модель доменов"""
    domain_name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Domain"
        verbose_name_plural = 'Domains'



class Responses(models.Model):
    """Модель ответов"""
    domain = models.ForeignKey(Domains, models.CASCADE)
    responses_time = models.TimeField()
    created = models.DateTimeField(auto_now_add=True, editable=False)

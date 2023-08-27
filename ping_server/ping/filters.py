from django.db import models
from django_filters import rest_framework, FilterSet, DateFromToRangeFilter

from ping.models import Responses


class ResponsesFilter(rest_framework.FilterSet):

    class Meta:
        model = Responses
        fields = ['domain']

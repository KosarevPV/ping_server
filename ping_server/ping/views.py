from rest_framework.viewsets import ModelViewSet
from .models import Responses, Domains
from .serializers import ResponsesModelSerializer, DomainsModelSerializer
from django.http import HttpResponse


class ResponsesModelViewSet(ModelViewSet):
    queryset = Responses.objects.all()
    serializer_class = ResponsesModelSerializer


class DomainsModelViewSet(ModelViewSet):
    queryset = Domains.objects.all()
    serializer_class = DomainsModelSerializer


class ResponsesQuerysetFilterViewSet(ModelViewSet):
    queryset = Responses.objects.all()
    serializer_class = ResponsesModelSerializer
    filterset_fields = ['domain']


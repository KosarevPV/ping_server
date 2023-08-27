from rest_framework.serializers import ModelSerializer
from .models import Responses, Domains


class ResponsesModelSerializer(ModelSerializer):
    class Meta:
        model = Responses
        fields = '__all__'


class DomainsModelSerializer(ModelSerializer):
    class Meta:
        model = Domains
        fields = '__all__'

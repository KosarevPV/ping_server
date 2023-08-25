from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Responses


class ResponsesModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Responses
        fields = '__all__'

from rest_framework.viewsets import ModelViewSet
from .models import Responses
from .serializers import ResponsesModelSerializer


class ResponsesModelViewSet(ModelViewSet):
    queryset = Responses.objects.all()
    serializer_class = ResponsesModelSerializer

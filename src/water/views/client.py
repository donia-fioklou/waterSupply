from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from water.models.client import Client
from water.serialisers.serializer_client import ClientSerialiser

class ClientViewSet(ModelViewSet):
    
    serializer_class=ClientSerialiser
    
    
    def get_queryset(self):
        return Client.objects.all()



    
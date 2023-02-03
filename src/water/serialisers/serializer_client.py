from rest_framework.serializers import ModelSerializer
from water.models.client import Client

class ClientSerialiser(ModelSerializer):
    
    class Meta:
        model=Client
        fields=['distributeur','nom','contact','adresse']
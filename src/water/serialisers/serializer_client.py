from rest_framework.serializers import ModelSerializer
from water.models.client import Client
from water.models.commande import Commmande

class ClientSerializer(ModelSerializer):
    
    class Meta:
        model=Client
        fields=['nom','contact','adresse']

class CommandeSerializer(ModelSerializer):
    
    class Meta:
        model=Commmande
        fields='__all__'
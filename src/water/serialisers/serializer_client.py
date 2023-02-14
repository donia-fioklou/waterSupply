from rest_framework.serializers import ModelSerializer
from water.models.client import Client
from water.models.commande import Commande

class ClientSerializer(ModelSerializer):
    
    class Meta:
        model=Client
        fields=['nom','contact','adresse']

class CommandeSerializer(ModelSerializer):
    
    class Meta:
        model=Commande
        fields=['qte_sachet','client']

class ApprovisonnerSerializer(ModelSerializer):
    
    class Meta:
        model=Commande
        fields=['qte_sachet','client','montant','date_appro',
'com_statut']
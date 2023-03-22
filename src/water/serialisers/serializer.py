from rest_framework.serializers import ModelSerializer
from water.models.client import Client
from water.models.commande import Commande


class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = ['id','nom', 'contact', 'adresse']
    def create(self, validated_data):
        user = self.context['request'].user
        return Client.objects.create(user=user, **validated_data)


class CommandeSerializer(ModelSerializer):

    class Meta:
        model = Commande
        fields = ['id', 'user','qte_sachet', 'client', 'date_com',
                  'montant',
                  'date_appro',
                  'commandeStatut',]
    def create(self, validated_data):
        user = self.context['request'].user
        return Commande.objects.create(user=user, **validated_data)
        


class ApprovisonnerSerializer(ModelSerializer):

    class Meta:
        model = Commande
        fields = ['qte_sachet', 'client', 'montant', 'date_appro',
                  'com_statut']

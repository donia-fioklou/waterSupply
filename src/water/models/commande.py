from django.db import models

from water.models.client import Client
from water.models.distributeur import Distributeur

class Commmande(models.Model):
    client=models.ForeignKey(Client,on_delete= models.CASCADE)
    distributeur=models.ForeignKey(Distributeur,on_delete=models.CASCADE)
    qte_sachet=models.PositiveIntegerField()
    date_com=models.DateField(auto_now_add=True)
    montant=models.FloatField(blank=True)
    date_appro=models.DateField(blank=True)
    com_statut=(('E','En attente'),
                 ('L','Livrer')   )
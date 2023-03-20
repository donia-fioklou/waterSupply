from django.db import models

from water.models.client import Client
from django.contrib.auth.models import User

class Commande(models.Model):
    client=models.ForeignKey(Client,on_delete= models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    qte_sachet=models.PositiveIntegerField()
    date_com=models.DateField(auto_now_add=True)
    montant=models.FloatField(null=True)
    date_appro=models.DateField(null=True)
    com_statut=(('E','En attente'),
                 ('L','Livrer')   )
    commandeStatut=models.CharField(max_length=1,choices=com_statut,default='E',verbose_name='rôle')
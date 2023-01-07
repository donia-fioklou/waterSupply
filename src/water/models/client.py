from django.db import models

from water.models.distributeur import Distributeur
from water.models.localisation import Localisation
class Client(models.Model):
    distributeur=models.ForeignKey(Distributeur,on_delete=models.CASCADE)
    nom=models.CharField( max_length=50)
    contact=models.IntegerField(max_length=8)
    adresse=models.CharField(max_length=200)
    localiston=Localisation(blank=True)
    dateCreation=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return  self.nom
    
    class Meta():
        verbose_name="Client"
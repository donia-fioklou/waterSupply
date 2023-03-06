from django.db import models
from django.contrib.auth.models import User
#from authentication.models import User
from water.models.localisation import Localisation

class Client(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    nom=models.CharField( max_length=50)
    contact=models.IntegerField(max_length=8)
    adresse=models.CharField(max_length=200)
    localiston=Localisation()
    dateCreation=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return  self.nom
    
    class Meta():
        verbose_name="Client"
    
    
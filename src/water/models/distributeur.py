from django.db import models
class Distributeur(models.Model):
    nom=models.CharField( max_length=50)
    contact=models.IntegerField(max_length=8)
    adresse=models.CharField(max_length=200)
    dateCreation=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return  self.nom
    
    class Meta():
        verbose_name="Distributeur"
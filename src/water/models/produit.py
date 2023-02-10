from django.db import models

class Produit(models.Model):
    nom=models.CharField( max_length=200)
    qte=models.IntegerField(max_length=4)
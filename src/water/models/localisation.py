from django.db import models

class Localisation(models.Model):
    longitude=models.FloatField()
    latitude=models.FloatField()
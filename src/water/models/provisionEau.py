from django.db import models

class ProvisionEau(models.Model):
    qte=models.IntegerField(max_length=4)
    date_prov=models.DateField(auto_now_add=False)
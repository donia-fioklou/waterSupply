import uuid
from django.db import models

class ProvisionEau(models.Model):
    code=models.CharField( max_length=5,unique=True,blank=True)
    qte=models.IntegerField(max_length=4)
    date_prov=models.DateField(auto_now_add=False)
    
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = uuid.uuid4().hex[:5]
        super().save(*args, **kwargs)
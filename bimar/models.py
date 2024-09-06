from django.db import models
from django.contrib.auth.models import User



class Doctor(models.Model):
    user = models.ForeignKey(User , on_delete=models.PROTECT)
    date = models.DateField()

class Khedmat(models.Model):
    title = models.CharField(max_length=10)
    price = models.DecimalField()
    def __str__(self) -> str:
        return self.title
    
class Nobat(models.Model):
    bimar_name = models.ForeignKey(User , on_delete=models.PROTECT)
    khedmat_type = models.ForeignKey(Khedmat , on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.bimar_name
# Create your models here.

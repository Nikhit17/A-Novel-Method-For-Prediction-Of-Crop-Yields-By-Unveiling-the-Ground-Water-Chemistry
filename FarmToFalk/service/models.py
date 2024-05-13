from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Add_details(models.Model):
    Crop=models.CharField(max_length=50)
    
    ph=models.CharField(max_length=50)
    K=models.CharField(max_length=50)
    N=models.CharField(max_length=50)
    P=models.CharField(max_length=50)
    Humidity=models.CharField(max_length=50)
    Temeprature=models.CharField(max_length=50)
    Rainfall=models.CharField(max_length=50)
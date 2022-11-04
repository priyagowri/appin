from email.message import Message
from django.db import models

# Create your models here.

class Datas(models.Model):
    name =models.CharField(max_length=20,default="")
    email= models.CharField(max_length=10,default="")
    phone=models.IntegerField(default="")
    programs=models.CharField(max_length=20,default="")
    message=models.CharField(max_length=50,default="")


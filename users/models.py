from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username=models.CharField(max_length=30, unique=True)
    email=models.EmailField()
    password1=models.CharField(max_length=30)
    password2=models.CharField(max_length=30)


    def __str__(self):
        return self.email

class Details(models.Model):
    #userDetails=models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    about=models.CharField(max_length=200,default='')
    highestQualification=models.CharField(max_length=50,default='')
    tenthPercent = models.FloatField(max_length=5, null=True)
    twelfthPercent = models.FloatField(max_length=5, null=True)
    currentPercent = models.FloatField(max_length=5, null=True)
    category = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.highestQualification

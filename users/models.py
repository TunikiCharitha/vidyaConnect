from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # add additional fields in here
    username=models.CharField(max_length=30, unique=True)
    email=models.EmailField()
    password1=models.CharField(max_length=30)
    password2=models.CharField(max_length=30)
    highestQualification=models.CharField(max_length=50)
    tenthPercent=models.FloatField(max_length=5,null=True)
    twelfthPercent=models.FloatField(max_length=5,null=True)
    currentPercent=models.FloatField(max_length=5,null=True)


    def __str__(self):
        return self.email
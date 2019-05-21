from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import multiselectfield
from multiselectfield import MultiSelectField
class CustomUser(AbstractUser):
    username=models.CharField(max_length=30, unique=True,error_messages={'invalid':'Username should be atleast 6 characters long'})
    email=models.EmailField()
    password1=models.CharField(max_length=30)
    password2=models.CharField(max_length=30)
    flag=models.CharField(max_length=5,default='first')

    def __str__(self):
        return self.username


class Profile(models.Model):

    cat_choices = (
        ('Internships', 'Internships'),
        ('Scholarships', 'Scholarships'),
        ('EntranceExams', 'EntranceExams'),
        ('Jobs', 'Jobs'),
        ('Events', 'Events'),
        ('HigherEducation', 'HigherEducation'),
        ('Startups', 'Startups'),
        ('Fellowships', 'Fellowships'),
        ('DataScience', 'DataScience'),
        ('ArtificialIntelligence', 'ArtificialIntelligence'),
    )

    user=models.OneToOneField(CustomUser,null=True, on_delete=models.CASCADE)
    about=models.CharField(max_length=200,default='')
    highestQualification=models.CharField(max_length=50,default='')
    currentPercent = models.FloatField(max_length=5, null=True)
    #category = models.CharField(max_length=30,null=True)
    category=MultiSelectField(choices=cat_choices,default='none')
    def __str__(self):
        return self.highestQualification
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
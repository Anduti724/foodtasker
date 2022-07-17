from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Restorant(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE, related_name='restorant')
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    adress=models.CharField(max_length=255)
    logo=CloudinaryField('image')

    def __str__(self) :
        return self.name


from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):

    phone_number = models.CharField(max_length=15)
    age = models.PositiveIntegerField(null=True)
   

    AUTHENTICATION_METHOD = 'email'
    def __str__(self):
        return self.username
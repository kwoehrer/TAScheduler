from django.db import models


# Create your models here.

class User(models.Model):
    class UserTypes(models.TextChoices):
        Admin = 'Admin'
        Instructor = 'Instructor'
        TA = 'TA'

    #Blank is used to denote if its required or not.
    email = models.CharField(max_length=30, unique=True, blank=False, null=False)
    username = models.CharField(max_length=30, unique=True, blank=False, null=False)
    password = models.CharField(max_length=30, blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    phone_number = models.CharField(max_length=10, unique=True, blank=True, null=True)
    home_address = models.CharField(max_length=30, blank=True, null=True)
    user_type = models.CharField(choices=UserTypes.choices, default='TA', blank=False, null=False)

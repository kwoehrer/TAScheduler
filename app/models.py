from django.db import models


# Create your models here.

class User(models.Model):
    class UserTypes(models.TextChoices):
        Admin = 'Admin'
        Instructor = 'Instructor'
        TA = 'TA'

    email = models.CharField(max_length=30, unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10, unique=True)
    home_address = models.CharField(max_length=30)
    user_type = models.CharField(choices=UserTypes.choices, default='TA')


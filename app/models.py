from django.db import models


# Create your models here.

class User(models.Model):
    class UserTypes(models.TextChoices):
        Admin = 'Admin'
        Instructor = 'Instructor'
        TA = 'TA'

    #Blank/Null is used to denote if its required or not.
    account_ID = models.AutoField(primary_key=True,Unique=True, db_index=True, auto_created=True)
    email = models.CharField(max_length=30, unique=True, blank=False, null=False)
    username = models.CharField(max_length=30, unique=True, blank=False, null=False, db_index=True)
    password = models.CharField(max_length=30, blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False, db_index=True)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    phone_number = models.CharField(max_length=10, unique=True, blank=True, null=True)
    home_address = models.CharField(max_length=30, blank=True, null=True)
    user_type = models.CharField(choices=UserTypes.choices, default='TA', blank=False, null=False, db_index=True)

#Seperate subtypes for extensibility
class Admin(models.Model):
    account_ID = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)

class Instructor(models.Model):
    account_ID = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)

class TA(models.Model):
    account_ID = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)

class Course(models.Model):

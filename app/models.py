from django.db import models
from django.db.models import UniqueConstraint
from django.core.validators import validate_email

# Create your models here.

class User(models.Model):
    class UserTypes(models.TextChoices):
        Admin = 'Admin'
        Instructor = 'Instructor'
        TA = 'TA'

    #Blank/Null is used to denote if its required or not.
    account_ID = models.AutoField(primary_key=True,Unique=True, db_index=True, auto_created=True)
    email = models.CharField(max_length=30, unique=True, blank=False, null=False, validators=validate_email)
    username = models.CharField(max_length=30, unique=True, blank=False, null=False, db_index=True)
    password = models.CharField(max_length=30, blank=False, null=False) #Need to validate
    first_name = models.CharField(max_length=30, blank=False, null=False, db_index=True)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    phone_number = models.CharField(max_length=10, unique=True, blank=True, null=True) #Need to validate
    home_address = models.CharField(max_length=70, blank=True, null=True) #Need to validate
    user_type = models.CharField(choices=UserTypes.choices, default='TA', blank=False, null=False, db_index=True)

#Seperate subtypes for extensibility
class Admin(models.Model):
    account_ID = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)

class Instructor(models.Model):
    account_ID = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)

class TA(models.Model):
    account_ID = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)

class Course(models.Model):
    class SemesterTypes(models.TextChoices):
        Spring = 'Spring'
        Summer = 'Summer'
        Fall = 'Fall'
        Winter = 'Winter'
        Special = 'Special'

    course_ID = models.AutoField(primary_key=True, Unique=True, db_index=True, auto_created=True)
    name = models.CharField(max_length=30, blank=False, null=False)
    semester = models.CharField(choices=SemesterTypes.choices, default='Spring', blank=False, null=False, db_index=True)
    year = models.IntegerField(max_length=4, blank=False, null=False, default=2022) #Need to validate
    description = models.CharField(max_length=30, blank=False, null=False)
    credits = models.IntegerField(max_length=1, blank=False, null=False, default=3) #Need to validate

class Section(models.Model):
    #NOTE THERE IS AN AUTOGEN ID FOR THIS MODEL.
    course_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    section_num = models.AutoField(blank=False, null=False, auto_created=True)
    MeetingTimes = models.CharField(maxlength=50, blank=False, null=False)

    UniqueConstraint(fields=[course_ID,section_num], name="SectionCompPK") #Functions similar to a unique Comp PK

class InstructorAssignments:
    #NOTE THERE IS AN AUTOGEN ID FOR THIS MODEL.
    account_ID = models.ForeignKey(Instructor, on_delete=models.CASCADE, blank=False, null=False)
    course_ID = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False, null=False)
    UniqueConstraint(fields=[course_ID, account_ID], name="CompPK")

class TASectionAssignments:
    #NOTE THERE IS AN AUTOGEN ID FOR THIS MODEL.
    account_ID = models.ForeignKey(TA, on_delete=models.CASCADE, blank=False, null=False)
    section_ID = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False, null=False)
    UniqueConstraint(fields=[section_ID, account_ID], name="CompPK") #Functions similar to a unique Comp PK

class TACourseAssignments:
    #NOTE THERE IS AN AUTOGEN ID FOR THIS MODEL.
    account_ID = models.ForeignKey(TA, on_delete=models.CASCADE, blank=False, null=False)
    course_ID = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False, null=False)
    UniqueConstraint(fields=[course_ID, account_ID], name="CompPK")#Functions similar to a unique Comp PK

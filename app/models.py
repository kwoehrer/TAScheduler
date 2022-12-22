import datetime

from django.core.validators import validate_email, MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import UniqueConstraint


# Create your models here.

class User(models.Model):
    class UserTypes(models.TextChoices):
        Admin = 'Admin'
        Instructor = 'Instructor'
        TA = 'TA'

    # Blank/Null is used to denote if its required or not.
    account_ID = models.AutoField(primary_key=True, auto_created=True)
    email = models.EmailField(max_length=30, unique=True, blank=False, null=False)
    username = models.CharField(max_length=30, unique=True, blank=False, null=False, db_index=True)
    # Need to validate password - do at form level, unsure if we need to salt for security
    password = models.CharField(max_length=30, blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False, db_index=True)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    phone_number = models.CharField(max_length=10, unique=True, blank=True, null=True)
    home_address = models.CharField(max_length=70, blank=True, null=True)
    user_type = models.CharField(max_length=50, choices=UserTypes.choices, default='TA', blank=False, null=False,
                                 db_index=True)

# Seperate subtypes for extensibility
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

    course_ID = models.AutoField(primary_key=True, db_index=True, auto_created=True)
    name = models.CharField(max_length=30, blank=False, null=False)
    semester = models.CharField(choices=SemesterTypes.choices, max_length=10, default='Spring', blank=False, null=False,
                                db_index=True)
    year = models.IntegerField(blank=False, null=False, default=2022,
                               validators=[MinValueValidator(datetime.date.today().year - 10,
                                                             message="Course.year cannot be more than 10 years into " + " the past."),
                                           MaxValueValidator(datetime.date.today().year + 10,
                                                             message="Course.year cannot be more than 10 years into " + " the future.")])
    # Above validator validates that they don't add anything more than 10 years in the future
    description = models.CharField(max_length=70, blank=False, null=False)
    credits = models.IntegerField(blank=False, null=False, default=3,
                                  validators=[MaxValueValidator(9, message="Course.credit field must be less than 10."),
                                              MinValueValidator(1,
                                                                message="Course.credit field must be greater than 1.")])
    UniqueConstraint(fields=[name, semester, year], name="CourseCompPK")



class Section(models.Model):
    # NOTE THERE IS AN AUTOGEN ID FOR THIS MODEL.
    course_ID = models.ForeignKey(Course, on_delete=models.CASCADE)
    section_num = models.IntegerField(blank=False, null=False)  # Validate in wrapper class
    MeetingTimes = models.CharField(max_length=50, blank=False, null=False)
    ta_account_id = models.ForeignKey(TA, on_delete=models.SET_NULL, blank=True, null=True)
    UniqueConstraint(fields=[course_ID, section_num], name="SectionCompPK")  # Functions similar to a unique Comp PK


class InstructorAssignments(models.Model):
    # NOTE THERE IS AN AUTOGEN ID FOR THIS MODEL.
    account_ID = models.ForeignKey(Instructor, on_delete=models.CASCADE, blank=False, null=False)
    course_ID = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False, null=False)
    UniqueConstraint(fields=[course_ID, account_ID], name="CompPK")


class TACourseAssignments(models.Model):
    # NOTE THERE IS AN AUTOGEN ID FOR THIS MODEL.
    account_ID = models.ForeignKey(TA, on_delete=models.CASCADE, blank=False, null=False)
    course_ID = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False, null=False)
    UniqueConstraint(fields=[course_ID, account_ID], name="CompPK")  # Functions similar to a unique Comp PK

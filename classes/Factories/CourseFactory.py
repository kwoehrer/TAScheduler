from abc import ABC, abstractmethod
from enum import Enum

from app.models import User, Admin, TA, Instructor, Course
from classes.Courses.CoursesClass import AbstractCourse
from classes.Users.users import InstructorUser, TAUser, AdminUser, AbstractUser


class AbstractCourseFactory(ABC):
    @abstractmethod
    def create_course(self, creator: AbstractUser, newAccountAttrbitutes: []):
        pass

    @abstractmethod
    def delete_course(self, deletor: AbstractUser, newAccountAttrbitutes: []):
        pass


class ConcreteCourseFactory(AbstractCourseFactory:
    def create_course(self, creator: AbstractUser, new_course_attributes: []):
        # Verify creator is an admin
        if not (isinstance(creator, AdminUser)) or creator.getUserType() != "Admin":
            raise TypeError("Only admin user accounts can create courses.")

        name = new_course_attributes['name']
        semester = new_course_attributes['semester']
        year = new_course_attributes['year']
        description = new_course_attributes['description']
        credit = new_course_attributes['credits']

        # Verify arguments are correct
        semester_valid_list = ['Spring', 'Summer', 'Fall', 'Winter', 'Special']
        if semester not in semester_valid_list:
            raise ValueError("The semester for a course was not a valid semester.")

        if len(User.objects.filter(name=name, semester=semester, year=year)) != 0:
            raise ValueError("A course with the same name, year, and semester already exists")

        if credit > 9 or credit < 1:
            raise ValueError("Invalid credit amount for course.")

        new_course = Course(name=name, semester=semester, year=year, description=description, credit=credit)
        new_course.save()

    def delete_course(self, deletor: AbstractUser, delete_course: AbstractCourse):
        # verify our logged in user/deletor can delete accounts
        if not isinstance(deletor, AdminUser) or deletor.getUserType() != "Admin":
            raise TypeError("Only admin user accounts can delete accounts.")

        # verify course is not already deleted
        delete_id = delete_course.get_course_id()
        if len(Course.objects.filter(course_ID=delete_id)) == 0:
            raise ValueError("Cannot delete an account that has already been deleted.")

        Course.objects.filter(course_ID=delete_id).delete()

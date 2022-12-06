from django.test import TestCase

from app.models import Admin, User, TA, Instructor, Course
from classes import Courses
from classes.Courses.CoursesClass import AbstractCourse, ConcreteCourse
from classes.Factories.AccountFactory import AbstractAccountFactory, ConcreteAccountFactory
from classes.Factories.CourseFactory import AbstractCourseFactory, ConcreteCourseFactory
from classes.Users.users import AdminUser, InstructorUser, TAUser, AbstractUser


class Testcreate_course(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='testadmin', password='password1', first_name="admin", last_name='admin',
                            phone_number=1234567890, home_address='123 Hell Lane', user_type='Admin',
                            email='adminemail@aol.com')
        admin_user_model = User.objects.filter(username='testadmin')[0]
        admin_model = Admin.objects.create(account_ID=admin_user_model)

        User.objects.create(username='ta', password='password1', first_name="ta", last_name='ta',
                            phone_number=1234567898, home_address='123 Hell Lane', user_type='TA',
                            email='taemail@aol.com')
        ta_user_model = User.objects.filter(username='ta')[0]
        ta_model = TA.objects.create(account_ID=ta_user_model)

        User.objects.create(username='instructor', password='password1', first_name="instr", last_name='instr',
                            phone_number=1234567896, home_address='123 Hell Lane', user_type='Instrutor',
                            email='instremail@aol.com')
        instr_user_model = User.objects.filter(username='instructor')[0]
        instr_model = Instructor.objects.create(account_ID=instr_user_model)

        User.objects.create(username='deladmin', password='password1', first_name="admin", last_name='admin',
                            phone_number=1234567895, home_address='123 Hell Lane', user_type='Admin',
                            email='deladminemail@aol.com')
        admin_user_model = User.objects.filter(username='deladmin')[0]
        del_admin_model = Admin.objects.create(account_ID=admin_user_model)

        self.acc_fact: AbstractAccountFactory = ConcreteAccountFactory()

        self.admin: AbstractUser = AdminUser(admin_model)
        self.del_admin: AbstractUser = AdminUser(del_admin_model)
        self.ta: AbstractUser = TAUser(ta_model)
        self.instr: AbstractUser = InstructorUser(instr_model)  # changed to instructorUser

        self.course_fact: AbstractCourseFactory = ConcreteCourseFactory()
        Course.objects.create(course_ID='123', name='hello world', semester='Spring', year='2022',
                              description='teaching hello world', credits='3')
        course_model = Course.objects.filter(course_ID='123')[0]
        self.course: AbstractCourse = ConcreteCourse(course_model)

        self.good_course_attributes = dict()
        self.good_course_attributes['name'] = 'Brian'
        self.good_course_attributes['semester'] = 'Spring'
        self.good_course_attributes['year'] = 2023
        self.good_course_attributes['description'] = 'Doe'
        self.good_course_attributes['credits'] = 4

    def test_no_arg(self):
        with self.assertRaises(TypeError, msg="Zero Arguments failed to throw type error"):
            self.course_fact.create_course()

    def test_one_arg(self):
        with self.assertRaises(TypeError, msg="One Argument failed to throw type error"):
            self.course_fact.create_course(self.admin)

    def test_three_arg(self):
        with self.assertRaises(TypeError, msg="Three Arguments failed to throw type error"):
            self.course_fact.create_course(self.admin, self.admin, self.admin)

    def test_TA_create_course(self):
        with self.assertRaises(TypeError, msg='TA User should not be able to create a course'):
            self.course_fact.create_course(self.ta, self.course)

    def test_instr_create_course(self):
        with self.assertRaises(TypeError, msg='Instructor User should not be able to create a course'):
            self.course_fact.create_course(self.instr, self.course)

    def test_admin_verify_create_course(self):
        self.course_fact.create_course(self.admin, self.good_course_attributes)



class Testdelete_course(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='testadmin', password='password1', first_name="admin", last_name='admin',
                            phone_number=1234567890, home_address='123 Hell Lane', user_type='Admin',
                            email='adminemail@aol.com')
        admin_user_model = User.objects.filter(username='testadmin')[0]
        admin_model = Admin.objects.create(account_ID=admin_user_model)

        User.objects.create(username='ta', password='password1', first_name="ta", last_name='ta',
                            phone_number=1234567898, home_address='123 Hell Lane', user_type='TA',
                            email='taemail@aol.com')
        ta_user_model = User.objects.filter(username='ta')[0]
        ta_model = TA.objects.create(account_ID=ta_user_model)

        User.objects.create(username='instructor', password='password1', first_name="instr", last_name='instr',
                            phone_number=1234567896, home_address='123 Hell Lane', user_type='Instrutor',
                            email='instremail@aol.com')
        instr_user_model = User.objects.filter(username='instructor')[0]
        instr_model = Instructor.objects.create(account_ID=instr_user_model)

        User.objects.create(username='deladmin', password='password1', first_name="admin", last_name='admin',
                            phone_number=1234567895, home_address='123 Hell Lane', user_type='Admin',
                            email='deladminemail@aol.com')
        admin_user_model = User.objects.filter(username='deladmin')[0]
        del_admin_model = Admin.objects.create(account_ID=admin_user_model)

        self.acc_fact: AbstractAccountFactory = ConcreteAccountFactory()

        self.admin: AbstractUser = AdminUser(admin_model)
        self.del_admin: AbstractUser = AdminUser(del_admin_model)
        self.ta: AbstractUser = TAUser(ta_model)
        self.instr: AbstractUser = InstructorUser(instr_model)  # changed to instructorUser

        self.course_fact: AbstractCourseFactory = ConcreteCourseFactory()
        Course.objects.create(course_ID='123', name='hello world', semester='Spring', year='2022',
                              description='teaching hello world', credits='3')
        course_model = Course.objects.filter(course_ID='123')[0]
        self.course: AbstractCourse = ConcreteCourse(course_model)

    def test_admin_delete_course(self):
        self.course_fact.delete_course(self.admin, self.course)
        with self.assertRaises(IndexError, msg='TA User should not be able to delete a course'):
            len(Course.objects.filter(course_ID='123')[0].course_ID)

    def test_TA_delete_course(self):
        with self.assertRaises(TypeError, msg='TA User should not be able to delete a course'):
            self.course_fact.delete_course(self.ta, self.course)

    def test_instr_delete_course(self):
        with self.assertRaises(TypeError, msg='Instructor User should not be able to delete a course'):
            self.course_fact.delete_course(self.instr, self.course)

    def test_delete_deleted_course(self):
        Course.objects.filter(course_ID='123').delete()
        with self.assertRaises(ValueError, msg='Cannot delete a course that was already deleted'):
            self.course_fact.delete_course(self.admin, self.course)

class InvalidInputTests(TestCase):

    def setUp(self) -> None:
        User.objects.create(username='testadmin', password='password1', first_name="admin", last_name='admin',
                            phone_number=1234567890, home_address='123 Hell Lane', user_type='Admin',
                            email='adminemail@aol.com')
        admin_user_model = User.objects.filter(username='testadmin')[0]
        admin_model = Admin.objects.create(account_ID=admin_user_model)

        User.objects.create(username='ta', password='password1', first_name="ta", last_name='ta',
                            phone_number=1234567898, home_address='123 Hell Lane', user_type='TA',
                            email='taemail@aol.com')
        ta_user_model = User.objects.filter(username='ta')[0]
        ta_model = TA.objects.create(account_ID=ta_user_model)

        User.objects.create(username='instructor', password='password1', first_name="instr", last_name='instr',
                            phone_number=1234567896, home_address='123 Hell Lane', user_type='Instrutor',
                            email='instremail@aol.com')
        instr_user_model = User.objects.filter(username='instructor')[0]
        instr_model = Instructor.objects.create(account_ID=instr_user_model)

        User.objects.create(username='deladmin', password='password1', first_name="admin", last_name='admin',
                            phone_number=1234567895, home_address='123 Hell Lane', user_type='Admin',
                            email='deladminemail@aol.com')
        admin_user_model = User.objects.filter(username='deladmin')[0]
        del_admin_model = Admin.objects.create(account_ID=admin_user_model)

        self.acc_fact: AbstractAccountFactory = ConcreteAccountFactory()

        self.admin: AbstractUser = AdminUser(admin_model)
        self.del_admin: AbstractUser = AdminUser(del_admin_model)
        self.ta: AbstractUser = TAUser(ta_model)
        self.instr: AbstractUser = InstructorUser(instr_model)  # changed to instructorUser

        self.course_fact: AbstractCourseFactory = ConcreteCourseFactory()
        Course.objects.create(course_ID='123', name='hello world', semester='Spring', year='2022',
                              description='teaching hello world', credits='3')
        course_model = Course.objects.filter(course_ID='123')[0]
        self.course: AbstractCourse = ConcreteCourse(course_model)

        self.good_course_attributes = dict()
        self.good_course_attributes['name'] = 'Brian'
        self.good_course_attributes['semester'] = 'Spring'
        self.good_course_attributes['year'] = 2023
        self.good_course_attributes['description'] = 'Doe'
        self.good_course_attributes['credits'] = 4

    def test_invalid_long_name(self):
        self.good_course_attributes['name'] = '1234567891234567891234567891234' # 31 characters
        with self.assertRaises(ValueError,
                               msg='Cannot create a course with a 31 character length name'):
            self.course_fact.create_course(self.admin, self.good_course_attributes)

    def test_invalid_short_name(self):
        self.good_course_attributes['name'] = ''  # 31 characters
        with self.assertRaises(ValueError,
                               msg='Cannot create a course with a 0 character length name'):
            self.course_fact.create_course(self.admin, self.good_course_attributes)

    def test_invalid_semester(self):
        self.good_course_attributes['semester'] = 'gold'
        with self.assertRaises(ValueError,
                               msg='Cannot create a course with an invalid semester'):
            self.course_fact.create_course(self.admin, self.good_course_attributes)

    def test_invalid_no_semester(self):
        self.good_course_attributes['semester'] = ''
        with self.assertRaises(ValueError,
                               msg='Cannot create a course with no semester'):
            self.course_fact.create_course(self.admin, self.good_course_attributes)

    def test_invalid_past_year(self):
        self.good_course_attributes['year'] = 1000
        with self.assertRaises(ValueError,
                               msg='Cannot create a course with an invalid past year, which is 10+ years ago'):
            self.course_fact.create_course(self.admin, self.good_course_attributes)

    def test_invalid_future_year(self):
        self.good_course_attributes['year'] = 3000
        with self.assertRaises(ValueError,
                               msg='Cannot create a course with an invalid future year, which is 10+ years ahead'):
            self.course_fact.create_course(self.admin, self.good_course_attributes)

    def test_invalid_high_credit(self):
        self.good_course_attributes['credits'] = 10
        with self.assertRaises(ValueError,
                               msg='Cannot create a course with more than 9 credits'):
            self.course_fact.create_course(self.admin, self.good_course_attributes)

    def test_invalid_low_credit(self):
        self.good_course_attributes['credits'] = 0
        with self.assertRaises(ValueError,
                               msg='Cannot create a course with less than 1 credit'):
            self.course_fact.create_course(self.admin, self.good_course_attributes)

    def test_invalid_description(self):
        self.good_course_attributes['description'] = ''
        with self.assertRaises(ValueError,
                               msg='Cannot create a course without a description'):
            self.course_fact.create_course(self.admin, self.good_course_attributes)

    def test_invalid_description(self):
        self.good_course_attributes['description'] = '1234567891234567891234567891234'
        with self.assertRaises(ValueError,
                               msg='Cannot create a course with a description over 30 characters long'):
            self.course_fact.create_course(self.admin, self.good_course_attributes)
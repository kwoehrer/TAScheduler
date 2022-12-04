from django.test import TestCase

from app.models import Admin, User, TA, Instructor
from classes import Courses
from classes.Courses.CoursesClass import AbstractCourse, ConcreteCourse
from classes.Factories.AccountFactory import AbstractAccountFactory, ConcreteAccountFactory
from classes.Users.users import AdminUser, InstructorUser, TAUser, AbstractUser


class TestCreateCourse(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='testadmin', password='password1', first_name="admin", last_name='admin',
                            phone_number=1234567890, home_address='123 Hell Lane', user_type='Admin',
                            email='adminemail@aol.com')
        admin_user_model = User.objects.filter(username='testadmin')[0]
        admin_model = Admin.objects.create(account_ID=admin_user_model.account_ID)

        User.objects.create(username='ta', password='password1', first_name="ta", last_name='ta',
                            phone_number=1234567890, home_address='123 Hell Lane', user_type='TA',
                            email='taemail@aol.com')
        ta_user_model = User.objects.filter(username='ta')[0]
        ta_model = TA.objects.create(account_ID=ta_user_model.account_ID)

        User.objects.create(username='instructor', password='password1', first_name="instr", last_name='instr',
                            phone_number=1234567890, home_address='123 Hell Lane', user_type='Instrutor',
                            email='instremail@aol.com')
        instr_user_model = User.objects.filter(username='instructor')[0]
        instr_model = Instructor.objects.create(account_ID=instr_user_model.account_ID)

        User.objects.create(username='deladmin', password='password1', first_name="admin", last_name='admin',
                            phone_number=1234567890, home_address='123 Hell Lane', user_type='Admin',
                            email='deladminemail@aol.com')
        admin_user_model = User.objects.filter(username='deladmin')[0]
        del_admin_model = Admin.objects.create(account_ID=admin_user_model.account_ID)

        self.acc_fact: AbstractAccountFactory = ConcreteAccountFactory()

        self.admin: AbstractUser = AdminUser(admin_model)
        self.del_admin: AbstractUser = AdminUser(del_admin_model)
        self.ta: AbstractUser = TAUser(ta_model)
        self.instr: AbstractUser = AdminUser(instr_model)

        self.course_fact: AbstractCourse = ConcreteCourse()
        Courses.objects.create(course_ID='123', name='hello world', semester='Spring', year='2022',
                               description='teaching hello world', credits='3')
        course_model = Courses.objects.filter(course_ID='123')[0]
        self.course: AbstractCourse = ConcreteCourse(course_model)

    def test_no_arg(self):
        with self.assertRaises(TypeError, msg="Zero Arguments failed to throw type error"):
            self.course_fact.createCourse()

    def test_one_arg(self):
        with self.assertRaises(TypeError, msg="One Argument failed to throw type error"):
            self.course_fact.createCourse(self.admin)

    # createCourse(self, creator: AbstractUser, newAccountAttributes[])
    def test_two_arg(self):
        with self.assertRaises(TypeError, msg="Two Arguments failed to throw type error"):
            self.course_fact.createCourse(self.admin, self.admin)

    def test_three_arg(self):
        with self.assertRaises(TypeError, msg="Three Arguments failed to throw type error"):
            self.course_fact.createCourse(self.admin, self.admin, self.admin)

    def test_TA_createCourse(self):
        with self.assertRaises(ValueError, msg='TA User should not be able to create a course'):
            self.course_fact.createCourse(self, self.ta, self.course)

    def test_instr_createCourse(self):
        with self.assertRaises(ValueError, msg='Instructor User should not be able to create a course'):
            self.course_fact.createCourse(self, self.instr, self.course)

    def test_admin_createCourse(self):
        self.course_fact.createCourse(self, self.admin, self.course)
        # should pass
        pass

class TestDeleteCourse(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='testadmin', password='password1', first_name="admin", last_name='admin',
                            phone_number=1234567890, home_address='123 Hell Lane', user_type='Admin',
                            email='adminemail@aol.com')
        admin_user_model = User.objects.filter(username='testadmin')[0]
        admin_model = Admin.objects.create(account_ID=admin_user_model.account_ID)

        User.objects.create(username='ta', password='password1', first_name="ta", last_name='ta',
                            phone_number=1234567890, home_address='123 Hell Lane', user_type='TA',
                            email='taemail@aol.com')
        ta_user_model = User.objects.filter(username='ta')[0]
        ta_model = TA.objects.create(account_ID=ta_user_model.account_ID)

        User.objects.create(username='instructor', password='password1', first_name="instr", last_name='instr',
                            phone_number=1234567890, home_address='123 Hell Lane', user_type='Instrutor',
                            email='instremail@aol.com')
        instr_user_model = User.objects.filter(username='instructor')[0]
        instr_model = Instructor.objects.create(account_ID=instr_user_model.account_ID)

        User.objects.create(username='deladmin', password='password1', first_name="admin", last_name='admin',
                            phone_number=1234567890, home_address='123 Hell Lane', user_type='Admin',
                            email='deladminemail@aol.com')
        admin_user_model = User.objects.filter(username='deladmin')[0]
        del_admin_model = Admin.objects.create(account_ID=admin_user_model.account_ID)

        self.acc_fact: AbstractAccountFactory = ConcreteAccountFactory()

        self.admin: AbstractUser = AdminUser(admin_model)
        self.del_admin: AbstractUser = AdminUser(del_admin_model)
        self.ta: AbstractUser = TAUser(ta_model)
        self.instr: AbstractUser = AdminUser(instr_model)

        self.course_fact: AbstractCourse = ConcreteCourse()
        Courses.objects.create(course_ID='123', name='hello world', semester='Spring', year='2022',
                               description='teaching hello world', credits='3')
        course_model = Courses.objects.filter(course_ID='123')[0]
        self.course: AbstractCourse = ConcreteCourse(course_model)

    def test_admin_deleteCourse(self):
        self.course_fact.deleteCourse(self, self.admin, self.course)
        length_match = len(Courses.objects.get(course_ID='123'))
        self.assertEqual(0, length_match, msg='Course was not successfully deleted from the Course table.')

    def test_TA_deleteCourse(self):
        with self.assertRaises(ValueError, msg='TA User should not be able to delete a course'):
            self.course_fact.deleteCourse(self, self.ta, self.course)

    def test_instr_deleteCourse(self):
        with self.assertRaises(ValueError, msg='Instructor User should not be able to delete a course'):
            self.course_fact.deleteCourse(self, self.instr, self.course)

    def test_delete_deleted_course(self):
        course_id = Courses.bjects.filter(course_ID='123')[0]
        Courses.objects.filter(course_ID=course_id).delete()
        with self.assertRaises(ValueError, msg='Cannot delete a course that was already deleted'):
            self.course_fact.deleteCourse(self, self.admin, self.course)

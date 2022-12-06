from django.test import TestCase

from app.models import Admin, User, TA, Instructor
from classes.Factories.AccountFactory import AbstractAccountFactory, ConcreteAccountFactory
from classes.Users.users import AdminUser, InstructorUser, TAUser, AbstractUser


class TestCreateAccount(TestCase):

    def setUp(self) -> None:
        User.objects.create(username='testadmin', password='password1', first_name="admin", last_name='admin',
                            phone_number=1234567890, home_address='123 Hell Lane', user_type='Admin',
                            email='adminemail@aol.com')
        admin_user_model = User.objects.filter(username='testadmin')[0]
        admin_model = Admin.objects.create(account_ID=admin_user_model)

        User.objects.create(username='ta', password='password1', first_name="ta", last_name='ta',
                            phone_number=2345678901, home_address='123 Hell Lane', user_type='TA',
                            email='taemail@aol.com')
        ta_user_model = User.objects.filter(username='ta')[0]
        ta_model = TA.objects.create(account_ID=ta_user_model)

        User.objects.create(username='instructor', password='password1', first_name="instr", last_name='instr',
                            phone_number=3456789012, home_address='123 Hell Lane', user_type='Instrutor',
                            email='instremail@aol.com')
        instr_user_model = User.objects.filter(username='instructor')[0]
        instr_model = Instructor.objects.create(account_ID=instr_user_model)

        self.acc_fact: AbstractAccountFactory = ConcreteAccountFactory()
        self.good_account_attributes = dict()
        self.good_account_attributes['username'] = 'username'
        self.good_account_attributes['password'] = 'password1'
        self.good_account_attributes['first_name'] = 'John'
        self.good_account_attributes['last_name'] = 'Doe'
        self.good_account_attributes['phone_number'] = '2622622662'
        self.good_account_attributes['home_address'] = '123 Mary Jane Lane'
        self.good_account_attributes['email'] = 'newemail@aol.com'
        self.good_account_attributes['user_type'] = 'TA'
        self.admin: AbstractUser = AdminUser(admin_model)
        self.ta: AbstractUser = TAUser(ta_model)
        self.instr: AbstractUser = InstructorUser(instr_model)

    def test_no_arg(self):
        with self.assertRaises(TypeError, msg="Zero Arguments failed to throw type error"):
            self.acc_fact.create_account()

    def test_only_account_attributes(self):
        with self.assertRaises(TypeError, msg="Only account arguments failed to throw type error"):
            self.acc_fact.create_account()

    def test_only_admin_user(self):
        with self.assertRaises(TypeError, msg="Only creater argument failed to throw TypeError"):
            self.acc_fact.create_account(self.admin)

    def test_good_attribute_TA_user(self):
        with self.assertRaises(TypeError, msg='TA User should not be able to create another account'):
            self.acc_fact.create_account(self.ta, self.good_account_attributes)

    def test_good_attribute_Instructor_user(self):
        with self.assertRaises(TypeError, msg='Instructor User should not be able to create another account'):
            self.acc_fact.create_account(self.instr, self.good_account_attributes)

    def test_good_attribute_admin_user_creates_ta(self):
        self.acc_fact.create_account(self.admin, self.good_account_attributes)
        length_match = len(User.objects.filter(username=self.good_account_attributes['username']))
        self.assertEqual(1, length_match, msg='Account was not successfully created in user table.')
        length_match = len(TA.objects.filter(account_ID__username=self.good_account_attributes['username']))
        self.assertEqual(1, length_match, msg='Account was not successfully created in user table.')

    def test_good_attribute_admin_user_creates_instructor(self):
        self.good_account_attributes['user_type'] = 'Instructor'
        self.acc_fact.create_account(self.admin, self.good_account_attributes)
        length_match = len(User.objects.filter(username=self.good_account_attributes['username']))
        self.assertEqual(1, length_match, msg='Account was not successfully created in user table.')
        length_match = len(Instructor.objects.filter(account_ID__username=self.good_account_attributes['username']))
        self.assertEqual(1, length_match, msg='Account was not successfully created in user table.')

    def test_good_attribute_admin_user_creates_admin(self):
        self.good_account_attributes['user_type'] = 'Admin'
        self.acc_fact.create_account(self.admin, self.good_account_attributes)
        length_match = len(User.objects.filter(username=self.good_account_attributes['username']))
        self.assertEqual(1, length_match, msg='Account was not successfully created in user table.')
        length_match = len(Admin.objects.filter(account_ID__username=self.good_account_attributes['username']))
        self.assertEqual(1, length_match, msg='Account was not successfully created in user table.')

    def test_existing_username(self):
        self.good_account_attributes['username'] = 'testadmin'
        with self.assertRaises(ValueError,
                               msg='Cannot create an account where an existing account shares the username'):
            self.acc_fact.create_account(self.admin, self.good_account_attributes)

    def test_existing_email(self):
        self.good_account_attributes['email'] = 'adminemail@aol.com'
        with self.assertRaises(ValueError,
                               msg='Cannot create an account where an existing account shares the same email'):
            self.acc_fact.create_account(self.admin, self.good_account_attributes)

    def test_missing_required_attribute(self):
        self.good_account_attributes.pop('username')
        with self.assertRaises(KeyError,
                               msg='Cannot create an account without a username attribute specified'):
            self.acc_fact.create_account(self.admin, self.good_account_attributes)

    def test_missing_optional_attribute(self):
        self.good_account_attributes.pop('home_address')
        self.acc_fact.create_account(self.admin, self.good_account_attributes)
        length_match = len(User.objects.filter(username=self.good_account_attributes['username']))
        self.assertEqual(1, length_match, msg='Account was not successfully created in user table.')
        length_match = len(TA.objects.filter(account_ID__username=self.good_account_attributes['username']))
        self.assertEqual(1, length_match, msg='Account was not successfully created in user table.')

    def empty_password(self):
        self.good_account_attributes['password'] = ''
        with self.assertRaises(ValueError,
                               msg='Cannot create an account with an empty password.'):
            self.acc_fact.create_account(self.admin, self.good_account_attributes)

    def bad_password(self):
        self.good_account_attributes['password'] = 'abcde'
        with self.assertRaises(ValueError,
                               msg='Cannot create an account that does not meet password requirements'):
            self.acc_fact.create_account(self.admin, self.good_account_attributes)


class TestDeleteCourse(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='testadmin', password='password1', first_name="admin", last_name='admin',
                            phone_number=1234567890, home_address='123 Hell Lane', user_type='Admin',
                            email='adminemail@aol.com')
        admin_user_model = User.objects.filter(username='testadmin')[0]
        admin_model = Admin.objects.create(account_ID=admin_user_model)

        User.objects.create(username='ta', password='password1', first_name="ta", last_name='ta',
                            phone_number=2345678901, home_address='123 Hell Lane', user_type='TA',
                            email='taemail@aol.com')
        ta_user_model = User.objects.filter(username='ta')[0]
        ta_model = TA.objects.create(account_ID=ta_user_model)

        User.objects.create(username='instructor', password='password1', first_name="instr", last_name='instr',
                            phone_number=3456789012, home_address='123 Hell Lane', user_type='Instrutor',
                            email='instremail@aol.com')
        instr_user_model = User.objects.filter(username='instructor')[0]
        instr_model = Instructor.objects.create(account_ID=instr_user_model)

        User.objects.create(username='deladmin', password='password1', first_name="admin", last_name='admin',
                            phone_number=4567890123, home_address='123 Hell Lane', user_type='Admin',
                            email='deladminemail@aol.com')
        admin_user_model = User.objects.filter(username='deladmin')[0]
        del_admin_model = Admin.objects.create(account_ID=admin_user_model)

        self.acc_fact: AbstractAccountFactory = ConcreteAccountFactory()

        self.admin: AbstractUser = AdminUser(admin_model)
        self.del_admin: AbstractUser = AdminUser(del_admin_model)
        self.ta: AbstractUser = TAUser(ta_model)
        self.instr: AbstractUser = InstructorUser(instr_model)

    def test_no_arg(self):
        with self.assertRaises(TypeError, msg="Zero Arguments failed to throw type error"):
            self.acc_fact.delete_account()

    def test_one_arg(self):
        with self.assertRaises(TypeError, msg="One Argument failed to throw type error"):
            self.acc_fact.delete_account(self.admin)

    def test_three_arg(self):
        with self.assertRaises(TypeError, msg="Three Arguments failed to throw type error"):
            self.acc_fact.delete_account(self.admin, self.admin, self.admin)

    def test_TA_user(self):
        with self.assertRaises(TypeError, msg='TA User should not be able to delete another account'):
            self.acc_fact.delete_account(self.ta, self.instr)

    def test_instr_user(self):
        with self.assertRaises(TypeError, msg='Instructor User should not be able to delete another account'):
            self.acc_fact.delete_account(deletor=self.instr, deletee=self.ta)

    def test_delete_ta(self):
        self.acc_fact.delete_account(self.admin, self.ta)
        length_match = len(User.objects.filter(username='ta'))
        self.assertEqual(0, length_match, msg='Account was not successfully deleted from the user table.')
        length_match = len(TA.objects.filter(account_ID__username='ta'))
        self.assertEqual(0, length_match, msg='Account was not successfully deleted from the TA table')

    def test_delete_instructor(self):
        self.acc_fact.delete_account(self.admin, self.instr)
        length_match = len(User.objects.filter(username='instructor'))
        self.assertEqual(0, length_match, msg='Account was not successfully deleted from the user table.')
        length_match = len(Instructor.objects.filter(account_ID__username='instructor'))
        self.assertEqual(0, length_match, msg='Account was not successfully deleted from the instructor table')

    def test_delete_admin(self):
        self.acc_fact.delete_account(self.admin, self.del_admin)
        with self.assertRaises(User.DoesNotExist, msg='Account was not successfully deleted from the user table'):
            length_match = User.objects.get(username='deladmin')
        with self.assertRaises(Admin.DoesNotExist, msg='Account was not successfully deleted from the admin table'):
            Admin.objects.get(account_ID__username='deladmin')

    def test_delete_deleted_account(self):
        acc = User.objects.filter(username='deladmin')[0]
        User.objects.filter(account_ID=acc.account_ID).delete()
        with self.assertRaises(ValueError, msg='Cannot delete an account that was already deleted'):
            self.acc_fact.delete_account(self.admin, self.del_admin)

from django.test import TestCase

from app.models import Admin, User, TA, Instructor
from classes.Factories.AccountFactory import AbstractAccountFactory, ConcreteAccountFactory


class TestCreateAccount(TestCase):

    def setUp(self) -> None:
        User.objects.create(username='testadmin', password='password1', first_name="admin", last_name='admin',
                            phone_number=1234567890, home_address='123 Hell Lane', user_type='Admin', email='adminemail@aol.com')
        admin_user_model = Admin.objects.filter(username='testadmin')[0]
        admin_model = Admin.objects.create(account_ID=admin_user_model.account_ID)

        User.objects.create(username='ta', password='password1', first_name="ta", last_name='ta',
                            phone_number=1234567890, home_address='123 Hell Lane', user_type='TA', email='taemail@aol.com')
        ta_user_model = TA.objects.filter(username='ta')[0]
        ta_model = TA.objects.create(account_ID=ta_user_model.account_ID)

        User.objects.create(username='instructor', password='password1', first_name="instr", last_name='instr',
                            phone_number=1234567890, home_address='123 Hell Lane', user_type='Instrutor', email='instremail@aol.com')
        instr_user_model = Instructor.objects.filter(username='instructor')[0]
        instr_model = Instructor.objects.create(account_ID=instr_user_model.account_ID)

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
        self.admin: User = Admin_User(admin_model)
        self.ta: User = Ta_User(ta_model)
        self.instr: User = Instructor_User(instr_model)

    def test_no_arg(self):
        with self.assertRaises(TypeError, msg="Zero Arguments failed to throw type error"):
            self.acc_fact.create_account()

    def test_only_Account_attributes(self):
        with self.assertRaises(TypeError, msg="Only account arguments failed to throw type error"):
            self.acc_fact.create_account()

    def test_only_admin_user(self):
        with self.assertRaises(TypeError, msg="Only creater argument failed to throw TypeError"):
            self.acc_fact.create_account(self.admin)

    def test_good_attribute_TA_user(self):
        with self.assertRaises(ValueError, msg='TA User should not be able to create another account'):
            self.acc_fact.create_account(self.admin, self.good_account_attributes)

    def test_good_attribute_Instructor_user(self):
        with self.assertRaises(ValueError, msg='Instructor User should not be able to create another account'):
            self.acc_fact.create_account(self.instr, self.good_account_attributes)

    def test_good_attribute_admin_user_creates_ta(self):
        self.acc_fact.create_account(self.admin, self.good_account_attributes)
        length_match = len(User.objects.get(username=self.good_account_attributes['username']))
        self.assertEqual(1, length_match, msg='Account was not successfully created in user table.')
        length_match = len(TA.objects.get(username=self.good_account_attributes['username']))
        self.assertEqual(1, length_match, msg='Account was not successfully created in user table.')

    def test_good_attribute_admin_user_creates_instructor(self):
        self.good_account_attributes['user_type'] = 'Instructor'
        self.acc_fact.create_account(self.admin, self.good_account_attributes)
        length_match = len(User.objects.get(username=self.good_account_attributes['username']))
        self.assertEqual(1, length_match, msg='Account was not successfully created in user table.')
        length_match = len(TA.objects.get(username=self.good_account_attributes['username']))
        self.assertEqual(1, length_match, msg='Account was not successfully created in user table.')

    def test_good_attribute_admin_user_creates_admin(self):
        self.good_account_attributes['user_type'] = 'Admin'
        self.acc_fact.create_account(self.admin, self.good_account_attributes)
        length_match = len(User.objects.get(username=self.good_account_attributes['username']))
        self.assertEqual(1, length_match, msg='Account was not successfully created in user table.')
        length_match = len(TA.objects.get(username=self.good_account_attributes['username']))
        self.assertEqual(1, length_match, msg='Account was not successfully created in user table.')

    def test_existing_username(self):
        self.good_account_attributes['username'] = 'testadmin'
        with self.assertRaises(ValueError, msg='Cannot create an account where an existing account shares the username'):
            self.acc_fact.create_account(self.admin, self.good_account_attributes)

    def test_existing_email(self):
        self.good_account_attributes['email'] = 'adminemail@aol.com'
        with self.assertRaises(ValueError,
                               msg='Cannot create an account where an existing account shares the same email'):
            self.acc_fact.create_account(self.admin, self.good_account_attributes)

    def test_missing_required_attribute(self):
        self.good_account_attributes.pop('username')
        with self.assertRaises(ValueError,
                               msg='Cannot create an account without a username attribute specified'):
            self.acc_fact.create_account(self.admin, self.good_account_attributes)

    def test_missing_optional_attribute(self):
        self.good_account_attributes.pop('home_address')
        self.acc_fact.create_account(self.admin, self.good_account_attributes)
        length_match = len(User.objects.get(username=self.good_account_attributes['username']))
        self.assertEqual(1, length_match, msg='Account was not successfully created in user table.')
        length_match = len(TA.objects.get(username=self.good_account_attributes['username']))
        self.assertEqual(1, length_match, msg='Account was not successfully created in user table.')


class TestDeleteCourse(unittest.TestCase):
    pass


class TestEditCourse(unittest.TestCase):
    pass


class TestGetAllCourses(unittest.TestCase):
    pass


class TestFilterCourses(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()

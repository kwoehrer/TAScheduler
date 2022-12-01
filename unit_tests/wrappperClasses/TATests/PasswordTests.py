from django.test import TestCase
import re
from app.models import Admin, User, TA, Instructor
from classes.Users.users import AbstractUser


class TestAddress(TestCase):

    def setUp(self) -> None:
        User.objects.create(username='ta', password='password1', first_name="ta", last_name='ta',
                            phone_number=1234567890, home_address='123 Hell Lane', user_type='TA',
                            email='taemail@aol.com')
        ta_user_model = TA.objects.filter(username='ta')[0]
        ta_model = TA.objects.create(account_ID=ta_user_model.account_ID)

        self.ta: AbstractUser = TA(ta_model)
        self.acc: AbstractUser = TA()
        self.good_account_attributes = dict()
        self.good_account_attributes['username'] = 'username'
        self.good_account_attributes['password'] = 'password1'
        self.good_account_attributes['first_name'] = 'John'
        self.good_account_attributes['last_name'] = 'Doe'
        self.good_account_attributes['phone_number'] = '2622622662'
        self.good_account_attributes['home_address'] = '123 Mary Jane Lane'
        self.good_account_attributes['email'] = 'newemail@aol.com'
        self.good_account_attributes['user_type'] = 'TA'

    def testGoodNumber(self):
        with self.assertRaises(ValueError, msg="incorrect user type"):
            self.good_account_attributes['user_type'] = 'TA'
        self.assertEqual(self.good_account_attributes['password'], 'password', msg='incorrect number')

    def testBadNumber(self):
        with self.assertRaises(ValueError, msg="incorrect user type"):
            self.good_account_attributes['user_type'] = 'TA'
        length = len(self.good_account_attributes['password'])
        self.assertEqual(length, 10, msg='Bad length')

    def BadType(self):
        with self.assertRaises(ValueError, msg="incorrect user type"):
            self.good_account_attributes['user_type'] = 'TA'
        self.assertNotEqual(self.good_account_attributes['phone_number'], -1, msg="good type")

    def BadType2(self):
        with self.assertRaises(ValueError, msg="incorrect user type"):
            self.good_account_attributes['user_type'] = 'TA'
        with self.assertRaises(TypeError, msg="incorrect user type"):
            if re.match("^[0-9]*$", self.good_account_attributes['phone_number']) is not None:
                return True
            return False

    def test_no_arg(self):
        with self.assertRaises(TypeError, msg="Zero Arguments failed to throw type error"):
            self.acc.getPhoneNumber()

    def testExistingNumber(self):
        self.good_account_attributes['phone_number'] = 'newemail@aol.com'
        with self.assertRaises(ValueError,
                               msg='Cannot create an existing email'):
            self.acc.setPhoneNumber(self.ta.getPhoneNumber())
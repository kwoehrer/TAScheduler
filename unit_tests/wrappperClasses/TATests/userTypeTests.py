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

    def checkUserType(self):
        with self.assertRaises(TypeError, msg="Incorrect User Type"):
            self.good_account_attributes['user_type'] = 'Instructor'

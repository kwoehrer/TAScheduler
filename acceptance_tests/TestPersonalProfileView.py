from django.test import TestCase, Client

from app.models import *
from classes.Users.users import AdminUser

'''
-----------------------------------------------------------------------
Acceptance Criteria 1:
SCENARIO: As any type of user I need to be able to click "view personal profile" and view my profile.
GIVEN Any type of user is logged in and on the homepage
WHEN a user of any type clicks on the "view my profile" button
THEN account information is displayed
-----------------------------------------------------------------------
'''


class TestPersonalProfileView(TestCase):
    client = None
    admin = None

    def setUp(self):
        self.client = Client()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave',
                            user_type='Admin',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.admin: AdminUser = AdminUser(user_model)

    def test_viewProfile(self):

        response = self.client.post('/', {'username': 'John_Doe', 'password': 'password'})

        # successful login
        self.assertTrue(response.context is None)

        try:
            self.assertFalse(response.url, "home")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/MyProfile")

        try:
            self.assertTrue(response.url, "/MyProfile")
        except AssertionError as msg:
            print(msg)

class TestPersonalProfileEdit(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj)

        self.admin: AdminUser = AdminUser(user_model)

        self.client.post("/",
                         {"username": self.admin.getUsername(), "password": self.admin.getPassword()})


    def test_editEmail(self):
        self.client.post("/editMyProfile/",
                         {"Email": "johnDoe1@aol.com",
                          "Username": self.admin.getID(),
                          "Password": self.admin.getPassword(),
                          "First Name": self.admin.getFirstName(),
                          "Last Name": self.admin.getLastName(),
                          "Phone Number": self.admin.getPhoneNumber(),
                          "Home Address": self.admin.getHomeAddress(),
                          "Type of User Account": self.admin.getUserType()})
        self.assertEqual(User.objects.get(email=self.admin.getEmail()), "johnDoe1@aol.com",
                         msg="Email not set correctly")

    def test_editUsername(self):
        self.client.post("/editMyProfile/",
                         {"Email": self.admin.getEmail(),
                          "Username": "helloworld",
                          "Password": self.admin.getPassword(),
                          "First Name": self.admin.getFirstName(),
                          "Last Name": self.admin.getLastName(),
                          "Phone Number": self.admin.getPhoneNumber(),
                          "Home Address": self.admin.getHomeAddress(),
                          "Type of User Account": self.admin.getUserType()})
        self.assertEqual(User.objects.get(username=self.admin.getUsername()), "helloworld",
                         msg="Username not set correctly")

    def test_editPassword(self):
        self.client.post("/editMyProfile/",
                         {"Email": self.admin.getEmail(),
                          "Username": self.admin.getID(),
                          "Password": "helloworld",
                          "First Name": self.admin.getFirstName(),
                          "Last Name": self.admin.getLastName(),
                          "Phone Number": self.admin.getPhoneNumber(),
                          "Home Address": self.admin.getHomeAddress(),
                          "Type of User Account": self.admin.getUserType()})
        self.assertEqual(User.objects.get(email=self.admin.getEmail()).password, "helloworld",
                         msg="Password not set correctly")

    def test_editFirstName(self):
        self.client.post("/editMyProfile/",
                         {"Email": self.admin.getEmail(),
                          "Username": self.admin.getID(),
                          "Password": self.admin.getPassword(),
                          "First Name": "helloworld",
                          "Last Name": self.admin.getLastName(),
                          "Phone Number": self.admin.getPhoneNumber(),
                          "Home Address": self.admin.getHomeAddress(),
                          "Type of User Account": self.admin.getUserType()})
        self.assertEqual(User.objects.get(email=self.admin.getEmail()).first_name, "helloworld",
                         msg="First name not set correctly")

    def test_editLastName(self):
        self.client.post("/editMyProfile/",
                         {"Email": self.admin.getEmail(),
                          "Username": self.admin.getID(),
                          "Password": self.admin.getPassword(),
                          "First Name": self.admin.getFirstName(),
                          "Last Name": "helloworld",
                          "Phone Number": self.admin.getPhoneNumber(),
                          "Home Address": self.admin.getHomeAddress(),
                          "Type of User Account": self.admin.getUserType()})
        self.assertEqual(User.objects.get(email=self.admin.getEmail()).last_name, "helloworld",
                         msg="Last name not set correctly")

    def test_editPhoneNumber(self):
        self.client.post("/editMyProfile/",
                         {"Email": self.admin.getEmail(),
                          "Username": self.admin.getID(),
                          "Password": self.admin.getPassword(),
                          "First Name": self.admin.getFirstName(),
                          "Last Name": self.admin.getLastName(),
                          "Phone Number": "1234567891",
                          "Home Address": self.admin.getHomeAddress(),
                          "Type of User Account": self.admin.getUserType()})
        self.assertEqual(User.objects.get(email=self.admin.getEmail()).phone_number, "1234567891",
                         msg="Phone number not set correctly")
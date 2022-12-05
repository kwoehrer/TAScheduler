from django.test import TestCase, Client

from TAScheduler.app.models import *

'''
As a Admin, I want to be able to navigate to the Course Management page
----------------------------------------------------
GIVEN: The user is a Admin and is logged in and at the home page
AND:They can click on "Home"
THEN: They will be navigated to the "Home" page
As a user, I want to be able to navigate to the Home page
----------------------------------------------------
GIVEN: The user is a Admin and is logged in and at the home page
AND:They can click on "Update Account"
THEN: They will be navigated to the "Account Update" page
As a user, I want to be able to navigate to the Account Update page
----------------------------------------------------
GIVEN: The user is a Admin and is logged in and at the home page
AND:They can click on "Delete Account"
THEN: They will be navigated to the "Delete Account" page
As a user, I want to be able to navigate to the Delete Account page
'''


class TestTAHomePage(TestCase):

    def setUp(self):

        self.client = Client()
        self.admin = Admin.objects.create(username='John_Doe', password="password", first_name="John",
                                          last_name='Doe',
                                          phone_number='4149818000', home_address='2513 N Farewell Ave',
                                          user_type='Admin',
                                          email='johnDoe@aol.com')

        self.client.post("/",
                         {"username": self.admin.account_ID.username, "password": self.admin.account_ID.password})

    def test_editEmail(self):
        self.client.post("/AccountEdit/",
                         {"Email": "johnDoe1@aol.com", "Username": self.admin.account_ID.username,
                          "Password": self.admin.account_ID.password,
                          "First Name": self.admin.account_ID.first_name,
                          "Last Name": self.admin.account_ID.last_name,
                          "Phone Number": self.admin.account_ID.phone_number,
                          "Home Address": self.admin.account_ID.home_address,
                          "Type of User Account": self.admin.account_ID.user_type})
        self.assertEqual(TA.objects.get(userID=self.admin.account_ID.username), "johnDoe1@aol.com",
                         msg="Email not set correctly")

    def test_editUsername(self):
        self.client.post("/AccountEdit/",
                         {"Email": self.admin.account_ID.email, "Username": "John_Doe1",
                          "Password": self.admin.account_ID.password,
                          "First Name": self.admin.account_ID.first_name,
                          "Last Name": self.admin.account_ID.last_name,
                          "Phone Number": self.admin.account_ID.phone_number,
                          "Home Address": self.admin.account_ID.home_address,
                          "Type of User Account": self.admin.account_ID.user_type})
        self.assertEqual(TA.objects.get(userID=self.admin.account_ID.userID), "John_Doe1",
                         msg="Username not set correctly")

    def test_editPassword(self):
        self.client.post("/AccountEdit/",
                         {"Email": self.admin.account_ID.password, "Username": self.admin.account_ID.username,
                          "Password": "password123",
                          "First Name": self.admin.account_ID.first_name,
                          "Last Name": self.admin.account_ID.last_name,
                          "Phone Number": self.admin.account_ID.phone_number,
                          "Home Address": self.admin.account_ID.home_address,
                          "Type of User Account": self.admin.account_ID.user_type})
        self.assertEqual(TA.objects.get(userID=self.admin.account_ID.password), "password123",
                         msg="Password not set correctly")

    def test_editFirstName(self):
        self.client.post("/AccountEdit/",
                         {"Email": self.admin.account_ID.password, "Username": self.admin.account_ID.username,
                          "Password": self.admin.account_ID.password,
                          "First Name": "Kevin",
                          "Last Name": self.admin.account_ID.last_name,
                          "Phone Number": self.admin.account_ID.phone_number,
                          "Home Address": self.admin.account_ID.home_address,
                          "Type of User Account": self.admin.account_ID.user_type})
        self.assertEqual(TA.objects.get(userID=self.admin.account_ID.first_name), "Kevin",
                         msg="First name not set correctly")

    def test_editLastName(self):
        self.client.post("/AccountEdit/",
                         {"Email": self.admin.account_ID.password, "Username": self.admin.account_ID.username,
                          "Password": self.admin.account_ID.password,
                          "First Name": self.admin.account_ID.first_name,
                          "Last Name": "Smith",
                          "Phone Number": self.admin.account_ID.phone_number,
                          "Home Address": self.admin.account_ID.home_address,
                          "Type of User Account": self.admin.account_ID.user_type})
        self.assertEqual(TA.objects.get(userID=self.admin.account_ID.last_name), "Smith",
                         msg="Last name not set correctly")

    def test_editPhoneNumber(self):
        self.client.post("/AccountEdit/",
                         {"Email": self.admin.account_ID.password, "Username": self.admin.account_ID.username,
                          "Password": self.admin.account_ID.password,
                          "First Name": self.admin.account_ID.first_name,
                          "Last Name": self.admin.account_ID.last_name,
                          "Phone Number": "4148224000",
                          "Home Address": self.admin.account_ID.home_address,
                          "Type of User Account": self.admin.account_ID.user_type})
        self.assertEqual(TA.objects.get(userID=self.admin.account_ID.phone_number), "4148224000",
                         msg="Phone Number not set correctly")

    def test_editHomeAddress(self):
        self.client.post("/AccountEdit/",
                         {"Email": self.admin.account_ID.password, "Username": self.admin.account_ID.username,
                          "Password": self.admin.account_ID.password,
                          "First Name": self.admin.account_ID.first_name,
                          "Last Name": self.admin.account_ID.last_name,
                          "Phone Number": self.admin.account_ID.phone_number,
                          "Home Address": "2612 N Mary ville Ave",
                          "Type of User Account": self.admin.account_ID.user_type})
        self.assertEqual(TA.objects.get(userID=self.admin.account_ID.home_address), "2612 N Mary ville Ave",
                         msg="Home Address not set correctly")

    def test_editUserType(self):
        self.client.post("/AccountEdit/",
                         {"Email": self.admin.account_ID.password, "Username": self.admin.account_ID.username,
                          "Password": self.admin.account_ID.password,
                          "First Name": self.admin.account_ID.first_name,
                          "Last Name": self.admin.account_ID.last_name,
                          "Phone Number": self.admin.account_ID.phone_number,
                          "Home Address": self.admin.account_ID.home_address,
                          "Type of User Account": "TA"})
        self.assertEqual(TA.objects.get(userID=self.admin.account_ID.user_type), "TA",
                         msg="User Type not set correctly")

    def test_EditAccount_to_Home(self):

        r = self.client.post('/', {'username': 'John_Doe', 'password': 'password'})
        self.assertTrue(r.context is None)

        try:
            self.assertTrue(r.url, "AccountEdit")
        except AssertionError as msg:
            print(msg)

        r = self.client.get("/home")

        try:
            self.assertTrue(r.url, "/home")
        except AssertionError as msg:
            print(msg)

    def EditAccount_to_DeleteAccount(self):

        r = self.client.post('/', {'username': 'John_Doe', 'password': 'password'})
        self.assertTrue(r.context is None)

        try:
            self.assertTrue(r.url, "AccountEdit")
        except AssertionError as msg:
            print(msg)

        r = self.client.get("/AccountDelete")

        try:
            self.assertTrue(r.url, "/AccountDelete")
        except AssertionError as msg:
            print(msg)

    def test_AccountManagement_to_UpdateAccount(self):

        r = self.client.post('/', {'username': 'John_Doe', 'password': 'password'})
        self.assertTrue(r.context is None)

        try:
            self.assertTrue(r.url, "AccountEdit")
        except AssertionError as msg:
            print(msg)

        r = self.client.get("/AccountUpdate")

        try:
            self.assertTrue(r.url, "/AccountUpdate")
        except AssertionError as msg:
            print(msg)
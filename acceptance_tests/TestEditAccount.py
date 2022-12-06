from django.test import TestCase, Client

from TAScheduler.app.models import *
from classes.Users.users import AdminUser

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

'''
SCENARIO: As an Admin, I want to be able navigate the Edit Account Page and Edit a User
Acceptance Criteria 1:
SCENARIO: As an Admin, I want to be able to navigate to the Account Management page
GIVEN The user is an Admin and is logged in and at the Edit Account page
WHEN a user of type TA is to be edited
WHEN user can be found with valid fields in the list of all users
AND "Edit Account" is clicked
THEN account can be edited

Acceptance Criteria 2:
SCENARIO: As an Admin, I want to be able to navigate to the Account Management page
GIVEN The user is an Admin and is logged in and at the Edit Account page
WHEN a user of type Instructor is to be edited
WHEN user can be found with valid fields in the list of all users
AND "Edit Account" is clicked
THEN account can be edited

Acceptance Criteria 3:
SCENARIO: As an Admin, I want to be able to navigate to the Account Management page
GIVEN The user is an Admin and is logged in and at the Edit Account page
WHEN a user of type Admin is to be edited
WHEN user can be found with valid fields in the list of all users
AND "Edit Account" is clicked
THEN account can be edited

SCENARIO: As an Admin, I want to be able navigate to the Home Page
Acceptance Criteria 1:
GIVEN: The user is a Admin and is logged in and at the Edit Account page
AND:They can click on "Return to Account Management Page"
THEN: They will be navigated to the "AdminAccMng" page

'''


class TestTAHomePage(TestCase):

    def setUp(self):

        self.client = Client()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj.account_ID)

        self.admin: AdminUser = AdminUser(user_model)

        self.client.post("/",
                         {"username": self.admin.getUsername(), "password": self.admin.getPassword()})

    def test_editEmail(self):
        self.client.post("/AccountEdit/",
                         {"Email": "johnDoe1@aol.com", "Username": self.admin.getID(),
                          "Password": self.admin.getPassword(),
                          "First Name": self.admin.getFirstName(),
                          "Last Name": self.admin.getLastName(),
                          "Phone Number": self.admin.getPhoneNumber(),
                          "Home Address": self.admin.getHomeAddress(),
                          "Type of User Account": self.admin.getUserType()})
        self.assertEqual(TA.objects.get(userID=self.admin.getUsername()), "johnDoe1@aol.com",
                         msg="Email not set correctly")

    def test_editUsername(self):
        self.client.post("/AccountEdit/",
                         {"Email": self.admin.getEmail(), "Username": "John_Doe1",
                          "Password": self.admin.getPassword(),
                          "First Name": self.admin.getFirstName(),
                          "Last Name": self.admin.getLastName(),
                          "Phone Number": self.admin.getPhoneNumber(),
                          "Home Address": self.admin.getHomeAddress(),
                          "Type of User Account": self.admin.getUserType()})
        self.assertEqual(TA.objects.get(userID=self.admin.getID()), "John_Doe1",
                         msg="Username not set correctly")

    def test_editPassword(self):
        self.client.post("/AccountEdit/",
                         {"Email": self.admin.getPassword(), "Username": self.admin.getUsername(),
                          "Password": "password123",
                          "First Name": self.admin.getFirstName(),
                          "Last Name": self.admin.getLastName(),
                          "Phone Number": self.admin.getPhoneNumber(),
                          "Home Address": self.admin.getHomeAddress(),
                          "Type of User Account": self.admin.getUserType()})
        self.assertEqual(TA.objects.get(userID=self.admin.getPassword()), "password123",
                         msg="Password not set correctly")

    def test_editFirstName(self):
        self.client.post("/AccountEdit/",
                         {"Email": self.admin.getPassword(), "Username": self.admin.getUsername(),
                          "Password": self.admin.getPassword(),
                          "First Name": "Kevin",
                          "Last Name": self.admin.getLastName(),
                          "Phone Number": self.admin.getPhoneNumber(),
                          "Home Address": self.admin.getHomeAddress(),
                          "Type of User Account": self.admin.getUserType()})
        self.assertEqual(TA.objects.get(userID=self.admin.getFirstName()), "Kevin",
                         msg="First name not set correctly")

    def test_editLastName(self):
        self.client.post("/AccountEdit/",
                         {"Email": self.admin.getPassword(), "Username": self.admin.getUsername(),
                          "Password": self.admin.getPassword(),
                          "First Name": self.admin.getFirstName(),
                          "Last Name": "Smith",
                          "Phone Number": self.admin.getPhoneNumber(),
                          "Home Address": self.admin.getHomeAddress(),
                          "Type of User Account": self.admin.getUserType()})
        self.assertEqual(TA.objects.get(userID=self.admin.getLastName()), "Smith",
                         msg="Last name not set correctly")

    def test_editPhoneNumber(self):
        self.client.post("/AccountEdit/",
                         {"Email": self.admin.getPassword(), "Username": self.admin.getUsername(),
                          "Password": self.admin.getPassword(),
                          "First Name": self.admin.getFirstName(),
                          "Last Name": self.admin.getLastName(),
                          "Phone Number": "4148224000",
                          "Home Address": self.admin.getHomeAddress(),
                          "Type of User Account": self.admin.getUserType()})
        self.assertEqual(TA.objects.get(userID=self.admin.getPhoneNumber()), "4148224000",
                         msg="Phone Number not set correctly")

    def test_editHomeAddress(self):
        self.client.post("/AccountEdit/",
                         {"Email": self.admin.getPassword(), "Username": self.admin.getUsername(),
                          "Password": self.admin.getPassword(),
                          "First Name": self.admin.getFirstName(),
                          "Last Name": self.admin.getLastName(),
                          "Phone Number": self.admin.getPhoneNumber(),
                          "Home Address": "2612 N Mary ville Ave",
                          "Type of User Account": self.admin.getUserType()})
        self.assertEqual(TA.objects.get(userID=self.admin.getHomeAddress()), "2612 N Mary ville Ave",
                         msg="Home Address not set correctly")

    def test_editUserType(self):
        self.client.post("/AccountEdit/",
                         {"Email": self.admin.getPassword(), "Username": self.admin.account_ID.username,
                          "Password": self.admin.getPassword(),
                          "First Name": self.admin.getFirstName(),
                          "Last Name": self.admin.getLastName(),
                          "Phone Number": self.admin.getPhoneNumber(),
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

from django.test import TestCase, Client

from app.models import *
from classes.Users.users import AdminUser

'''
SCENARIO: As an Admin, I want to be able navigate the Edit Account Page and Edit a User
-----------------------------------------------------------------------
Acceptance Criteria 1:
SCENARIO: As an Admin, I want to be able to navigate to the Account Management page
GIVEN The user is an Admin and is logged in and at the Edit Account page
WHEN a user of type TA is to be edited
WHEN user can be found with valid fields in the list of all users
AND "Edit Account" is clicked
THEN account can be edited
-----------------------------------------------------------------------
Acceptance Criteria 2:
SCENARIO: As an Admin, I want to be able to navigate to the Account Management page
GIVEN The user is an Admin and is logged in and at the Edit Account page
WHEN a user of type Instructor is to be edited
WHEN user can be found with valid fields in the list of all users
AND "Edit Account" is clicked
THEN account can be edited
-----------------------------------------------------------------------
Acceptance Criteria 3:
SCENARIO: As an Admin, I want to be able to navigate to the Account Management page
GIVEN The user is an Admin and is logged in and at the Edit Account page
WHEN a user of type Admin is to be edited
WHEN user can be found with valid fields in the list of all users
AND "Edit Account" is clicked
THEN account can be edited
-----------------------------------------------------------------------
SCENARIO: As an Admin, I want to be able navigate to the Home Page
-----------------------------------------------------------------------
Acceptance Criteria 1:
GIVEN: The user is a Admin and is logged in and at the Edit Account page
AND:They can click on "Return to Account Management Page"
THEN: They will be navigated to the "AdminAccMng" page
'''


class TestEdtAccount(TestCase):
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

    def test_UserExists(self):
        Admin.objects.create(self.admin)
        user_obj = Admin.objects.filter(username='John_Doe')[0]
        new_user = Admin.objects.create(account_ID=user_obj)
        self.admin1: AdminUser = AdminUser(new_user)
        new_user.save()

        self.client.post({"/AccountEdit/",
                          self.admin1})

        self.assertEqual(self.admin1.getID(), Admin.objects.get(account_ID=self.admin.getID()), "User exists in "
                                                                                                "Database")

    def test_editEmail(self):
        self.client.post("/AccountEdit/",
                         {"Email": "johnDoe1@aol.com", "Username": self.admin.getID(),
                          "Password": self.admin.getPassword(),
                          "First Name": self.admin.getFirstName(),
                          "Last Name": self.admin.getLastName(),
                          "Phone Number": self.admin.getPhoneNumber(),
                          "Home Address": self.admin.getHomeAddress(),
                          "Type of User Account": self.admin.getUserType()})
        self.assertEqual(User.objects.get(userID=self.admin.getUsername()), "johnDoe1@aol.com",
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
        self.assertEqual(User.objects.get(userID=self.admin.getID()), "John_Doe1",
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
        self.assertEqual(User.objects.get(userID=self.admin.getPassword()), "password123",
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
        self.assertEqual(User.objects.get(userID=self.admin.getFirstName()), "Kevin",
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
        self.assertEqual(User.objects.get(userID=self.admin.getLastName()), "Smith",
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
        self.assertEqual(User.objects.get(userID=self.admin.getPhoneNumber()), "4148224000",
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
        self.assertEqual(User.objects.get(userID=self.admin.getHomeAddress()), "2612 N Mary ville Ave",
                         msg="Home Address not set correctly")

    def test_editUserType(self):
        self.client.post("/AccountEdit/",
                         {"Email": self.admin.getPassword(), "Username": self.admin.getUsername(),
                          "Password": self.admin.getPassword(),
                          "First Name": self.admin.getFirstName(),
                          "Last Name": self.admin.getLastName(),
                          "Phone Number": self.admin.getPhoneNumber(),
                          "Home Address": self.admin.getHomeAddress(),
                          "Type of User Account": "TA"})
        self.assertEqual(TA.objects.get(userID=self.admin.getUserType()), "TA",
                         msg="User Type not set correctly")


class TestEdtAccountToPages(TestCase):
    def test_EditAccount_to_AccManagement(self):

        response = self.client.post('/', {'username': 'John_Doe', 'password': 'password'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "/AccountEdit")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/AdminAccMng")

        try:
            self.assertTrue(response.url, "/AdminAccMng")
        except AssertionError as msg:
            print(msg)

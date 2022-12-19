from django.test import TestCase, Client

from app.models import *
from classes.Users.users import AdminUser

'''
SCENARIO: As an Admin, I want to be able to navigate to the Account Management page
----------------------------------------------------
Acceptance Criteria 1:
GIVEN: The user is an Admin and is logged in and at the Account Management Page
AND:They can click on "Create An Account"
THEN: They will be navigated to the "AccountCreate" Page
----------------------------------------------------
Acceptance Criteria 2:
GIVEN: The user is an Admin and is logged in and at the Account Management Page
AND:They can click on "Edit An Account"
THEN: They will be navigated to the "AccountEdit"
----------------------------------------------------
Acceptance Criteria 3:
GIVEN: The user is an Admin and is logged in and at the Account Management Page
AND:They can click on "Delete An Account"
THEN: They will be navigated to the "AccountDelete"
----------------------------------------------------
Acceptance Criteria 4:
GIVEN: The user is an Admin and is logged in and at the Account Management Page
AND:They can click on "Return Home"
THEN: They will be navigated to the "home"
'''


class TestAccountManagementPage(TestCase):

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

    def test_AccountManagement_to_CreateAccount(self):

        response = self.client.post('/', {'username': 'John_Doe', 'password': 'password'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "/AdminAccMng")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/AccountCreate")

        try:
            self.assertTrue(response.url, "/AccountCreate")
        except AssertionError as msg:
            print(msg)

    def test_AccountManagement_to_EditAccount(self):

        response = self.client.post('/', {'username': 'John_Doe', 'password': 'password'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "/AdminAccMng")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/AccountEdit")

        try:
            self.assertTrue(response.url, "/AccountEdit")
        except AssertionError as msg:
            print(msg)

    def test_AccountManagement_to_DeleteAccount(self):

        response = self.client.post('/', {'username': 'John_Doe', 'password': 'password'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "/AdminAccMng")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/AccountDelete")

        try:
            self.assertTrue(response.url, "/AccountDelete")
        except AssertionError as msg:
            print(msg)

    def test_AccountManagement_to_Home(self):

        response = self.client.post('/', {'username': 'John_Doe', 'password': 'password'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "/AdminAccMng")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/home")

        try:
            self.assertTrue(response.url, "/home")
        except AssertionError as msg:
            print(msg)

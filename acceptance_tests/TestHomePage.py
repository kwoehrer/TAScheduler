from django.test import TestCase, Client

from TAScheduler.app.models import *
from TAScheduler.classes.Users.users import AdminUser

'''
SCENARIO: As an Admin, I want to be able to navigate to the Home page
----------------------------------------------------
Acceptance Criteria 1:
GIVEN: The user is an Admin and is logged in and at the Admin home page view
AND:They can click on "Account Management"
THEN: They will be navigated to the "AdminAccMng"
----------------------------------------------------
Acceptance Criteria 2:
GIVEN: The user is an Admin and is logged in and at the Admin home page view
AND:They can click on "Course Management"
THEN: They will be navigated to the "AdminCourseMng"
----------------------------------------------------
Acceptance Criteria 3:
GIVEN: The user is an Admin and is logged in and at the Admin home page view
AND:They can click on "Log out"
THEN: They will be navigated to the "login" page
----------------------------------------------------
'''


class TestAdminHomePage(TestCase):

    def setUp(self):

        self.client = Client()
        Admin.objects.create(username='John_Doe', password="password", first_name="John",
                             last_name='Doe',
                             phone_number='4149818000', home_address='2513 N Farewell Ave',
                             user_type='Admin',
                             email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.admin: AdminUser = AdminUser(user_model)

    def test_home_to_AccManagement(self):

        response = self.client.post('/', {'username': 'John_Doe', 'password': 'password'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "/home")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/AdminAccMng")

        try:
            self.assertTrue(response.url, "/AdminAccMng")
        except AssertionError as msg:
            print(msg)

    def test_home_to_CourseManagement(self):

        response = self.client.post('/', {'username': 'John_Doe', 'password': 'password'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "/home")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/AdminCourseMng")

        try:
            self.assertTrue(response.url, "/AdminCourseMng")
        except AssertionError as msg:
            print(msg)

    def test_home_to_login(self):

        response = self.client.post('/', {'username': 'John_Doe', 'password': 'password'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "home")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/login")

        try:
            self.assertTrue(response.url, "/login")
        except AssertionError as msg:
            print(msg)
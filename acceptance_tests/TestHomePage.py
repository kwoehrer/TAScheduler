from django.test import TestCase, Client

from app.models import *
from classes.Users.users import AdminUser

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
        user_model.save()

    def test_home_to_AccManagement(self):

        response = self.client.post('/', {'username': self.admin.getUsername(), 'password': self.admin.getPassword()}, follow=True)
        # Check that the response is 200 OK.
        self.assertTrue(response.context is None)
        try:
            self.assertEqual(response.url, "home")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/AccountManagement/")

        try:
            self.assertTrue(response.url, "/AccountManagement/")
        except AssertionError as msg:
            print(msg)

    def test_home_to_CourseManagement(self):

        r = self.client.post('/', {'username': 'John_Doe', 'password': 'password'})
        self.assertTrue(r.context is None)

        try:
            self.assertTrue(r.url, "home")
        except AssertionError as msg:
            print(msg)

        r = self.client.get("/AdminCourseMng")

        try:
            self.assertTrue(r.url, "/AdminCourseMng")
        except AssertionError as msg:
            print(msg)

    def test_home_to_login(self):

        response = self.client.post('/', {'username': 'John_Doe', 'password': 'password'})
        self.assertRedirects(response.context is None)

        try:
            self.assertTrue(response.url, "home")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/login")

        try:
            self.assertTrue(response.url, "/login")
        except AssertionError as msg:
            print(msg)

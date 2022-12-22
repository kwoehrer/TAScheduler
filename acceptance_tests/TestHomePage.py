from django.test import TestCase, Client

from app.models import *
from classes.Users.users import AdminUser, InstructorUser, TAUser

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

        self.client.login(username='John_Doe', password='password')

    def test_home_to_AccManagement(self):
        response = self.client.get('/')
        # successful login

        self.assertEqual(str(response.resolver_match.url_name), "/AdminHome")

        response = self.client.get("/AdminAccMng")

        self.assertEqual(str(response.resolver_match.url_name), "/AdminAccMng")

    def test_home_to_CourseManagement(self):
        response = self.client.get('/')
        # successful login

        self.assertEqual(str(response.resolver_match.url_name), "/AdminHome")

        response = self.client.get("/AdminCourseMng")

        self.assertEqual(str(response.resolver_match.url_name), "/AdminCourseMng")

    def test_home_to_SendNotifications(self):
        response = self.client.get('/')
        # successful login

        self.assertEqual(str(response.resolver_match.url_name), "/AdminHome")

        response = self.client.get("/SendNotifications")

        self.assertEqual(str(response.resolver_match.url_name), "SendNotifications/AdminSendNotifications")

    def test_home_to_MyUserProfile(self):
        response = self.client.get('/')
        # successful login

        self.assertEqual(str(response.resolver_match.url_name), "/AdminHome")

        response = self.client.get("/MyUserProfile")

        self.assertEqual(str(response.resolver_match.url_name), "/MyUserProfile")

    def test_home_to_UserProfile(self):
        response = self.client.get('/')
        # successful login

        self.assertEqual(str(response.resolver_match.url_name), "/AdminHome")

        response = self.client.get("/UserProfile")

        self.assertEqual(str(response.resolver_match.url_name), "/ProfileStates/AdminViewState")

    def test_home_to_login(self):
        response = self.client.get('/')
        # successful login

        self.assertEqual(str(response.resolver_match.url_name), "/AdminHome")

        response = self.client.get("/login")

        self.assertEqual(str(response.resolver_match.url_name), "/login")

    def test_home_to_UserSearch(self):
        response = self.client.get('/')
        # successful login

        self.assertEqual(str(response.resolver_match.url_name), "/AdminHome")

        response = self.client.get("/searchStates/UserSearch")

        self.assertEqual(str(response.resolver_match.url_name), "/searchStates/UserSearch")

    def test_home_to_CourseSearch(self):
        response = self.client.get('/')
        # successful login

        self.assertEqual(str(response.resolver_match.url_name), "/AdminHome")

        response = self.client.get("/searchStates/CourseSearch")

        self.assertEqual(str(response.resolver_match.url_name), "/searchStates/CourseSearch")


'''
SCENARIO: As an Instructor, I want to be able to navigate to the Home page
----------------------------------------------------
Acceptance Criteria 1:
GIVEN: The user is an Instructor and is logged in and at the Instructor home page view
AND:They can click on "Send Notifications"
THEN: They will be navigated to the "Send Notifications" Page
----------------------------------------------------
Acceptance Criteria 2:
GIVEN: The user is an Instructor and is logged in and at the Instructor home page view
AND:They can click on "User Profile"
THEN: They will be navigated to the "InstrViewState" page
----------------------------------------------------
Acceptance Criteria 3:
GIVEN: The user is an Instructor and is logged in and at the Instructor home page view
AND:They can click on "User Search"
THEN: They will be navigated to the "User Search" page
---------------------------------------------------
Acceptance Criteria 4:
GIVEN: The user is an Instructor and is logged in and at the Instructor home page view
AND:They can click on "Course Search"
THEN: They will be navigated to the "Course Search" page
----------------------------------------------------
'''


class TestInstructorHomePage(TestCase):
    client = None
    admin = None

    def setUp(self):
        self.client = Client()
        User.objects.create(username='Steven_Adams', password="password123", first_name="Steven",
                            last_name='Adams',
                            phone_number='4149818008', home_address='2514 N Farewell Ave',
                            user_type='Instructor',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_object)
        self.instructor: InstructorUser = InstructorUser(user_model)

        self.client.login(username='Steven_Adams', password='password123')

    def test_home_to_SendNotifications(self):
        response = self.client.get('/')
        # successful login

        self.assertEqual(str(response.resolver_match.url_name), "/InstructorHome")

        response = self.client.get("/SendNotifications")

        self.assertEqual(str(response.resolver_match.url_name), "SendNotifications/InstructorSendNotifications")

    def test_home_to_MyUserProfile(self):
        response = self.client.get('/')
        # successful login

        self.assertEqual(str(response.resolver_match.url_name), "/InstructorHome")

        response = self.client.get("/MyUserProfile")

        self.assertEqual(str(response.resolver_match.url_name), "/MyUserProfile")

    def test_home_to_UserProfile(self):
        response = self.client.get('/')
        # successful login

        self.assertEqual(str(response.resolver_match.url_name), "/InstructorHome")

        response = self.client.get("/UserProfile")

        self.assertEqual(str(response.resolver_match.url_name), "/ProfileStates/InstrViewState")

    def test_home_to_login(self):
        response = self.client.get('/')
        # successful login

        self.assertEqual(str(response.resolver_match.url_name), "/InstructorHome")

        response = self.client.get("/login")

        self.assertEqual(str(response.resolver_match.url_name), "/login")

    def test_home_to_UserSearch(self):
        response = self.client.get('/')
        # successful login

        self.assertEqual(str(response.resolver_match.url_name), "/InstructorHome")

        response = self.client.get("/searchStates/UserSearch")

        self.assertEqual(str(response.resolver_match.url_name), "/searchStates/UserSearch")

    def test_home_to_CourseSearch(self):
        response = self.client.get('/')
        # successful login

        self.assertEqual(str(response.resolver_match.url_name), "/home")

        response = self.client.get("/searchStates/CourseSearch")

        self.assertEqual(str(response.resolver_match.url_name), "/searchStates/CourseSearch")


'''
SCENARIO: As a TA, I want to be able to navigate to the Home page
----------------------------------------------------
Acceptance Criteria 1:
GIVEN: The user is a TA and is logged in and at the TA home page view
AND:They can click on "Send Notifications"
THEN: They will be navigated to the "Send Notifications" Page
----------------------------------------------------
Acceptance Criteria 2:
GIVEN: The user is a TA and is logged in and at the TA home page view
AND:They can click on "User Profile"
THEN: They will be navigated to the "InstrViewState" page
----------------------------------------------------
Acceptance Criteria 3:
GIVEN: The user is a TA and is logged in and at the TA home page view
AND:They can click on "User Search"
THEN: They will be navigated to the "User Search" page
---------------------------------------------------
Acceptance Criteria 4:
GIVEN: The user is an TA and is logged in and at the TA home page view
AND:They can click on "Course Search"
THEN: They will be navigated to the "Course Search" page
----------------------------------------------------
'''


class TestTAHomePage(TestCase):
    client = None
    admin = None

    def setUp(self):
        self.client = Client()
        User.objects.create(username='Gregory_Micheal', password="password12345", first_name="Gregory",
                            last_name='Micheal',
                            phone_number='4149818009', home_address='2515 N Farewell Ave',
                            user_type='TA',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_object)
        self.instructor: InstructorUser = InstructorUser(user_model)

        self.client.login(username='Gregory_Micheal', password='password12345')

    def test_home_to_MyUserProfile(self):
        response = self.client.get('/')
        # successful login

        self.assertEqual(str(response.resolver_match.url_name), "/homeStates/TAHome")

        response = self.client.get("/MyUserProfile")

        self.assertEqual(str(response.resolver_match.url_name), "/MyUserProfile")

    def test_home_to_UserProfile(self):
        response = self.client.get('/')
        # successful login

        self.assertEqual(str(response.resolver_match.url_name), "/homeStates/TAHome")

        response = self.client.get("/UserProfile")

        self.assertEqual(str(response.resolver_match.url_name), "ProfileStates/TAViewState")

    def test_home_to_login(self):
        response = self.client.get('/')
        # successful login

        self.assertEqual(str(response.resolver_match.url_name), "/homeStates/TAHome")

        response = self.client.get("/login")

        self.assertEqual(str(response.resolver_match.url_name), "/login")

    def test_home_to_UserSearch(self):
        response = self.client.get('/')
        # successful login

        self.assertEqual(str(response.resolver_match.url_name), "/homeStates/TAHome")

        response = self.client.get("/searchStates/UserSearch")

        self.assertEqual(str(response.resolver_match.url_name), "/searchStates/UserSearch")

    def test_home_to_CourseSearch(self):
        response = self.client.get('/')
        # successful login

        self.assertEqual(str(response.resolver_match.url_name), "/homeStates/TAHome")

        response = self.client.get("/searchStates/CourseSearch")

        self.assertEqual(str(response.resolver_match.url_name), "/searchStates/CourseSearch")


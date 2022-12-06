from django.test import TestCase, Client

from TAScheduler.app.models import *
from TAScheduler.classes.Users.users import AdminUser, TAUser, InstructorUser

'''
As a TA, I want to be able to navigate to the View my profile info page
----------------------------------------------------
GIVEN: The user is a TA and is logged in and at the home page
AND:They can click on "Profile Information Page"
THEN: They will be navigated to the "Profile Information Page" page
As a user, I want to be able to navigate to the Send Message page
----------------------------------------------------
GIVEN: The user is a TA and is logged in and at the home page
AND:They can click on "View my course assignments"
THEN: They will be navigated to the "View my course assignments" page
As a user, I want to be able to navigate to the Lab page
----------------------------------------------------
GIVEN: The user is a TA and is logged in and at the home page
AND:They can click on "Search for users or courses"
THEN: They will be navigated to the "Search for users or courses" page
As a user, I want to be able to navigate to the Course page
----------------------------------------------------
GIVEN: The user is a TA and is logged in and at the home page
AND:They can click on "Log out"
THEN: They will be navigated to the "login" page
As a user, I want to be able to navigate to the User page
----------------------------------------------------
'''


class TestTAHomePage(TestCase):

    def setUp(self):

        self.client = Client()
        self.user_ta = TA.objects.create(username='John_Doe', password="password", first_name="John",
                                         last_name='Doe',
                                         phone_number='4149818000', home_address='2513 N Farewell Ave',
                                         user_type='TA',
                                         email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.ta: TAUser = TAUser(user_model)

    def test_home_to_profile_info(self):

        response = self.client.post('/', {'username': 'John_Doe', 'password': 'password'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "home")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/MyProfileOverview")

        try:
            self.assertTrue(response.url, "/MyProfileOverview")
        except AssertionError as msg:
            print(msg)

    def test_home_to_Profile_Overview(self):

        response = self.client.post('/', {'username': 'John_Doe', 'password': 'password'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "home")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/MyProfileOverview")

        try:
            self.assertTrue(response.url, "/MyProfileOverview")
        except AssertionError as msg:
            print(msg)

    def test_home_to_Profile_Course_Search(self):

        response = self.client.post('/', {'username': 'John_Doe', 'password': 'password'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "home")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/ProfileCourseSearch")

        try:
            self.assertTrue(response.url, "/ProfileCourseSearch")
        except AssertionError as msg:
            print(msg)

    def test_home_to_logout(self):

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


'''
As a Instructor, I want to be able to navigate to the View my profile info page
----------------------------------------------------
GIVEN: The user is a Instructor and is logged in and at the home page
AND:They can click on "Profile Information Page"
THEN: They will be navigated to the "Profile Information Page" page
As a user, I want to be able to navigate to the Send Message page
----------------------------------------------------
GIVEN: The user is a Instructor and is logged in and at the home page
AND:They can click on "View my course assignments"
THEN: They will be navigated to the "View my course assignments" page
As a user, I want to be able to navigate to the Lab page
----------------------------------------------------
GIVEN: The user is a Instructor and is logged in and at the home page
AND:They can click on "Search for users or courses"
THEN: They will be navigated to the "Search for users or courses" page
As a user, I want to be able to navigate to the Course page
----------------------------------------------------
GIVEN: The user is a Instructor and is logged in and at the home page
AND:They can click on "Send Notification"
THEN: They will be navigated to the "Send Notification" page
As a user, I want to be able to navigate to the Course page
----------------------------------------------------
GIVEN: The user is a Instructor and is logged in and at the home page
AND:They can click on "Log out"
THEN: They will be navigated to the "login" page
As a user, I want to be able to navigate to the User page
----------------------------------------------------
'''


class TestInstructorHomePage(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.user_instructor = Instructor.objects.create(username='Steven_Adams', password="passwordNew",
                                                         first_name="Steven",
                                                         last_name='Adams',
                                                         phone_number='4149818222', home_address='2512 N Kenwood Ave',
                                                         user_type='Instructor',
                                                         email='stevenAdams@aol.com')
        user_object = User.objects.filter(username='Steven_Adams')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.admin: InstructorUser = InstructorUser(user_model)

    def test_home_to_account_settings(self):

        response = self.client.post('/', {'username': 'Steven_Adams', 'password': 'passwordNew'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "home")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/ProfileInformationPage")

        try:
            self.assertTrue(response.url, "/ProfileInformationPage")
        except AssertionError as msg:
            print(msg)

    def test_home_to_lab(self):

        response = self.client.post('/', {'username': 'Steven_Adams', 'password': 'passwordNew'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "home")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/View_my_course_assignments")

        try:
            self.assertTrue(response.url, "/View_my_course_assignments")
        except AssertionError as msg:
            print(msg)

    def test_home_to_course(self):

        response = self.client.post('/', {'username': 'Steven_Adams', 'password': 'passwordNew'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "home")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/Search_for_users_or_courses")

        try:
            self.assertTrue(response.url, "/Search_for_users_or_courses")
        except AssertionError as msg:
            print(msg)

    def test_home_to_user(self):

        response = self.client.post('/', {'username': 'Steven_Adams', 'password': 'passwordNew'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "home")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/view_users")

        try:
            self.assertTrue(response.url, "/view_users")
        except AssertionError as msg:
            print(msg)

    def test_home_to_send_notification(self):

        response = self.client.post('/', {'username': 'Steven_Adams', 'password': 'password'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "home")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/send_notifications")

        try:
            self.assertTrue(response.url, "/send_notifications")
        except AssertionError as msg:
            print(msg)

    def test_home_to_logout(self):

        response = self.client.post('/', {'username': 'Steven_Adams', 'password': 'password'})
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


'''
As an Admin, I want to be able to navigate to the View my profile info page
----------------------------------------------------
GIVEN: The user is an Admin and is logged in and at the home page
AND:They can click on "Profile Information Page"
THEN: They will be navigated to the "Profile Information Page" page
As a user, I want to be able to navigate to the Send Message page
----------------------------------------------------
GIVEN: The user is an Admin and is logged in and at the home page
AND:They can click on "View my course assignments"
THEN: They will be navigated to the "View my course assignments" page
As a user, I want to be able to navigate to the Lab page
----------------------------------------------------
GIVEN: The user is an Admin and is logged in and at the home page
AND:They can click on "Search for users or courses"
THEN: They will be navigated to the "Search for users or courses" page
As a user, I want to be able to navigate to the Course page
----------------------------------------------------
GIVEN: The user is an Admin and is logged in and at the home page
AND:They can click on "Account Management"
THEN: They will be navigated to the "Account Management" page
As a user, I want to be able to navigate to the Course page
----------------------------------------------------
GIVEN: The user is an Admin and is logged in and at the home page
AND:They can click on "Course Management"
THEN: They will be navigated to the "Course Management" page
As a user, I want to be able to navigate to the Course page
----------------------------------------------------
GIVEN: The user is an Admin and is logged in and at the home page
AND:They can click on "Log out"
THEN: They will be navigated to the "login" page
As a user, I want to be able to navigate to the User page
----------------------------------------------------
'''


class TestAdminHomePage(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        User.objects.create(username='Micheal_Johnson', password="password3", first_name="Micheal",
                            last_name='Johnson',
                            phone_number='4149824444', home_address='2264 N Bradford Ave',
                            user_type='Admin',
                            email='michealJohnson@aol.com')
        user_object = User.objects.filter(username='Micheal_Johnson')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.admin: AdminUser = AdminUser(user_model)

    def test_home_to_account_settings(self):

        response = self.client.post('/', {'username': 'Micheal_Johnson', 'password': 'password3'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "home")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/ProfileInformationPage")

        try:
            self.assertTrue(response.url, "/ProfileInformationPage")
        except AssertionError as msg:
            print(msg)

    def test_home_to_lab(self):

        response = self.client.post('/', {'username': 'Micheal_Johnson', 'password': 'password3'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "home")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/ViewMyCourseAssignments")

        try:
            self.assertTrue(response.url, "/ViewMyCourseAssignments")
        except AssertionError as msg:
            print(msg)

    def test_home_to_course(self):

        response = self.client.post('/', {'username': 'Micheal_Johnson', 'password': 'password3'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "home")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/SearchForUsersOrCourses")

        try:
            self.assertTrue(response.url, "/SearchForUsersOrCourses")
        except AssertionError as msg:
            print(msg)

    def test_home_to_user(self):

        response = self.client.post('/', {'username': 'Micheal_Johnson', 'password': 'password3'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "/home")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/AdminAccMng")

        try:
            self.assertTrue(response.url, "/AdminCourseMng")
        except AssertionError as msg:
            print(msg)

    def test_home_to_logout(self):

        response = self.client.post('/', {'username': 'Micheal_Johnson', 'password': 'password3'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "/home")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/login")

        try:
            self.assertTrue(response.url, "/login")
        except AssertionError as msg:
            print(msg)

from django.test import TestCase, Client
from app.models import *
from classes.Users.users import AdminUser

'''
As an Admin, I want to be able to navigate to the Admin Send Notifications Page
----------------------------------------------------
Scenario: Navigate to the Send Notifications Search Page
GIVEN: The user is an Admin and is logged in and at the Send Notifications Page
AND: They can query all User accounts
AND: They can query all User accounts from a specific course
AND: They have put in a message to send to a recipient
THEN: They can click on "Send Email" and send a notification to the specific user
----------------------------------------------------
Scenario: Send Notification to an Instructor
GIVEN: The user is an Admin and is logged in and at the Send Notifications Page
AND: The user to query is an Instructor
AND: The user is present in the list of all User accounts
AND: The user is present in the list of all User accounts in a specified course
AND: They have put in a message to send to a recipient
THEN: They can click on "Send Email" and send a notification to the specific user
----------------------------------------------------
Scenario: Send Notification to a TA
GIVEN: The user is an Admin and is logged in and at the Send Notifications Page
AND: The user to query is a TA
AND: The user is present in the list of all TA accounts
AND: The user is present in the list of all TA accounts in a specified course
AND: They have put in a message to send to a recipient
THEN: They can click on "Send Email" and send a notification to the specific user
----------------------------------------------------
Scenario: Navigate to the Home Page
GIVEN: The user is an Admin and is logged in and at the Admin home page view
AND: They can click on "Return to Home Page"
THEN: They will be navigated to the "Home" page
----------------------------------------------------
'''


class TestAdminSearchHomePage(TestCase):
    client = None
    admin = None

    def setUp(self):
        self.client = Client()
        User.objects.create(username='Steven_Adams', password="password123", first_name="Steven",
                            last_name='Adams',
                            phone_number='4149818004', home_address='2514 N Farewell Ave',
                            user_type='Instructor',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='Steven_Adams')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.admin: AdminUser = AdminUser(user_model)

        self.client.login(username='Steven_Adams', password='password123')

        User.objects.create(username='Gregory_Micheal', password="password1234", first_name="Gregory",
                            last_name='Micheal',
                            phone_number='4149818005', home_address='2515 N Farewell Ave',
                            user_type='TA',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='Gregory_Micheal')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.admin: AdminUser = AdminUser(user_model)

        self.client.login(username='John_Doe', password='password1234')

    def test_SendNotifications_Instructor_Invalid_User_Type(self):
        resp = self.client.post('/SendNotifications/AdminSendNotifications',
                                {"Select User Type": "", "Select Course": "", "Select all Users within Course":
                                    "Steven_Adams", "Subject": "Welcome to COMPSCI 361", "Message": "First Day of Class"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for user type field",
                         "An error message was not displayed when user type is not selected")

    def test_SendNotifications_Instructor_Invalid_Course(self):
        resp = self.client.post('/SendNotifications/AdminSendNotifications',
                                {"Select User Type": "Instructor", "Select Course": "", "Select all Users within Course":
                                    "Steven_Adams", "Subject": "Welcome to COMPSCI 361", "Message": "First Day of Class"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for course field",
                         "An error message was not displayed when course is not selected")

    def test_SendNotifications_Instructor_Invalid_User(self):
        resp = self.client.post('/SendNotifications/AdminSendNotifications',
                                {"Select User Type": "Instructor", "Select Course": "COMPSCI 361", "Select all Users "
                                                                                                   "within Course":
                                    "", "Subject": "Welcome to COMPSCI 361", "Message": "First Day of Class"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for User field",
                         "An error message was not displayed when user is not selected")

    def test_SendNotifications_Instructor_Empty_Message(self):
        resp = self.client.post('/SendNotifications/AdminSendNotifications',
                                {"Select User Type": "Instructor", "Select Course": "", "Select all Users within Course":
                                    "Steven_Adams", "Subject": "Welcome to COMPSCI 361", "Message": ""})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for message field",
                         "An error message was not displayed when message is not selected")

    def test_SendNotifications_TA_Invalid_User_Type(self):
        resp = self.client.post('/SendNotifications/AdminSendNotifications',
                                {"Select User Type": "", "Select Course": "", "Select all Users within Course":
                                    "Gregory_Micheal", "Subject": "Welcome to COMPSCI 361", "Message": "First Day of "
                                                                                                       "Class"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for user type field",
                         "An error message was not displayed when user type is not selected")

    def test_SendNotifications_TA_Invalid_Course(self):
        resp = self.client.post('/SendNotifications/AdminSendNotifications',
                                {"Select User Type": "TA", "Select Course": "", "Select all Users within Course":
                                    "Gregory_Micheal", "Subject": "Welcome to COMPSCI 361", "Message": "First Day of "
                                                                                                       "Class"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for course field",
                         "An error message was not displayed when course is not selected")

    def test_SendNotifications_TA_Invalid_User(self):
        resp = self.client.post('/SendNotifications/AdminSendNotifications',
                                {"Select User Type": "TA", "Select Course": "COMPSCI 361", "Select all Users within "
                                                                                           "Course":
                                    "", "Subject": "Welcome to COMPSCI 361", "Message": "First Day of Class"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for User field",
                         "An error message was not displayed when user is not selected")

    def test_SendNotifications_TA_Empty_Message(self):
        resp = self.client.post('/SendNotifications/AdminSendNotifications',
                                {"Select User Type": "TA", "Select Course": "", "Select all Users within Course":
                                    "Gregory_Micheal", "Subject": "Welcome to COMPSCI 361", "Message": ""})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for message field",
                         "An error message was not displayed when message is not selected")

    def test_SendNotifications_to_Home(self):
        # test that the home page redirects to the UserSearch page
        # Make a GET request to /SendNotifications/AdminSendNotifications
        response = self.client.get("/SendNotifications/AdminSendNotifications")

        # Check that the response was a redirect to page /home
        self.assertRedirects(response, '/home', status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

        # Follow the redirect and check that the final URL is '/home'
        response = response.follow()
        self.assertEqual(response.url, '/home')

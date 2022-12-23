from django.test import TestCase, Client
from app.models import *
from classes.Users.users import AdminUser, InstructorUser, TAUser

'''
SCENARIO: As an Admin, I want to be able navigate the Edit My User Profile Page and Edit my Profile
-----------------------------------------------------------------------
SCENARIO: As an Admin, I want to be able to change my profile information
GIVEN The user is an Admin and is logged in and at the Edit My User Profile page
WHEN a user of type Admin is to be edited
WHEN user can be found with valid fields in the list of all users
AND "Submit Changes" is clicked
THEN account can be edited
-----------------------------------------------------------------------
SCENARIO: As an Admin, I want to be able navigate to the Home Page
-----------------------------------------------------------------------
Acceptance Criteria 1:
GIVEN: The user is a Admin and is logged in and at the Edit My Profile page
AND:They can click on "Return to Home"
THEN: They will be navigated to the "Admin Home" page
'''


class TestAdminCreateAccount(TestCase):
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

        self.client.post("/",
                         {"username": self.admin.getUsername(), "password": self.admin.getPassword()})

    def testInvalidPhoneNumber(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "Stephen", "last_name": "Doe", "user_type": "admin",
                                     "email": "stephenDoe@aol.com", "phone_number": "a234567890",
                                     "home_address": "2514 N Farewell Ave",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["message"],
                         "Changes were not submitted. A phone number needs to be 10 digits")

    def testInvalidPassword(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "Stephen", "last_name": "Doe", "user_type": "admin",
                                     "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                     "home_address": "2514 N Farewell Ave",
                                     "password": "123456"}, follow=True)

        self.assertEqual(response.context["message"],
                         "Changes were not submitted. A password needs to be a string")

    def testInvalidFirstName(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "123", "last_name": "Doe", "user_type": "admin",
                                     "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                     "home_address": "2514 N Farewell Ave",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["message"],
                         "Changes were not submitted. A first name needs to be a string")

    def testInvalidLastName(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "John", "last_name": "123", "user_type": "admin",
                                     "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                     "home_address": "2514 N Farewell Ave",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["message"],
                         "Changes were not submitted. A last name needs to be a string")

    def testInvalidAddress(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "John", "last_name": "Doe", "user_type": "admin",
                                     "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                     "home_address": "123",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["message"],
                         "Changes were not submitted. A home address needs to be a string")

    def testInvalidEmail(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "John", "last_name": "Doe", "user_type": "admin",
                                     "email": "123", "phone_number": "1234567890",
                                     "home_address": "2514 N Farewell Ave",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["message"],
                         "Changes were not submitted. A home address needs to be a string")

    def testInvalidUserType(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "John", "last_name": "Doe", "user_type": 123,
                                     "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                     "home_address": "2514 N Farewell Ave",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["message"],
                         "Changes were not submitted. A user type needs to be a string")

    def test_EditChangesAdmin(self):
        self.client.post("/EditMyUserProfile",
                         {"first_name": "John", "last_name": "Doe", "user_type": "admin",
                          "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                          "home_address": "2514 N Farewell Ave",
                          "password": "password"}, follow=True)

        self.assertNotEqual("Stephen_Doe", self.admin.getUsername(),
                            "Supervisor was not edit successfully")

    def testEmptyFirstNameProvided(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "", "last_name": "Doe", "user_type": "admin",
                                     "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                     "home_address": "2514 N Farewell Ave",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["error"], "User was not edited. First Name should not be left blank")

    def testEmptyLastNameProvided(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "John", "last_name": "", "user_type": "admin",
                                     "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                     "home_address": "2514 N Farewell Ave",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["error"], "User was not edited. Last Name should not be left blank")

    def testEmptyUserTypeProvided(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "John", "last_name": "Doe", "user_type": "",
                                     "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                     "home_address": "2514 N Farewell Ave",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["error"], "User was not edited. User Type should not be left blank")

    def testEmptyPhoneNumberProvided(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "John", "last_name": "Doe", "user_type": "admin",
                                     "email": "stephenDoe@aol.com", "phone_number": "",
                                     "home_address": "2514 N Farewell Ave",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["error"], "User was not edited. Phone Number should not be left blank")

    def testEmptyHomeAddressProvided(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "John", "last_name": "Doe", "user_type": "admin",
                                     "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                     "home_address": "",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["error"], "User was not edited. Home Address should not be left blank")

    def testEmptyEmailProvided(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "John", "last_name": "Doe", "user_type": "admin",
                                     "email": "", "phone_number": "1234567890",
                                     "home_address": "2514 N Farewell Ave",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["error"], "User was not edited. Home Address should not be left blank")


class TestEditMyUserProfile_to_Home(TestCase):

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

        self.client.post("/",
                         {"username": self.admin.getUsername(), "password": self.admin.getPassword()})

    def test_EditMyUserProfile_to_Home(self):
        # Make a GET request to //MyUserProfile
        response = self.client.get("/EditMyUserProfile")

        # Check that the response was a redirect to page /home
        self.assertRedirects(response, '/AdminHome', status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

        # Follow the redirect and check that the final URL is '/home'
        response = response.follow()
        self.assertEqual(response.url, '/AdminHome')


'''
SCENARIO: As an Instructor, I want to be able navigate the Edit My User Profile Page and Edit my Profile
-----------------------------------------------------------------------
SCENARIO: As an Instructor, I want to be able to change my profile information
GIVEN The user is an Instructor and is logged in and at the Edit My User Profile page
WHEN a user of type Instructor is to be edited
WHEN user can be found with valid fields in the list of all users
AND "Submit Changes" is clicked
THEN account can be edited
-----------------------------------------------------------------------
SCENARIO: As an Instructor, I want to be able navigate to the Home Page
-----------------------------------------------------------------------
Acceptance Criteria 1:
GIVEN: The user is a Instructor and is logged in and at the Edit My Profile page
AND:They can click on "Return to Home"
THEN: They will be navigated to the "Admin Home" page
'''


class TestInstructorEditMyUserProfile(TestCase):
    def setUp(self):
        self.client1 = Client()
        user_object2 = User.objects.filter(username='John_Doe')[0]
        user_model2 = Instructor.objects.create(account_ID=user_object2)
        self.instructor: InstructorUser = InstructorUser(user_model2)
        user_model2.save()

        self.client1.post("/",
                          {"username": self.instructor.getUsername(), "password": self.instructor.getPassword()})

    def testInvalidPhoneNumber(self):
        response = self.client1.post("/EditMyUserProfile",
                                     {"first_name": "Stephen", "last_name": "Doe", "user_type": "instructor",
                                      "email": "stephenDoe@aol.com", "phone_number": "a234567890",
                                      "home_address": "2514 N Farewell Ave",
                                      "password": "password"}, follow=True)

        self.assertEqual(response.context["message"],
                         "Changes were not submitted. A phone number needs to be 10 digits")

    def testInvalidPassword(self):
        response = self.client1.post("/EditMyUserProfile",
                                     {"first_name": "Stephen", "last_name": "Doe", "user_type": "instructor",
                                      "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                      "home_address": "2514 N Farewell Ave",
                                      "password": "123"}, follow=True)

        self.assertEqual(response.context["message"],
                         "Changes were not submitted. A password needs to be a string")

    def testInvalidFirstName(self):
        response = self.client1.post("/EditMyUserProfile",
                                     {"first_name": "123", "last_name": "Doe", "user_type": "instructor",
                                      "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                      "home_address": "2514 N Farewell Ave",
                                      "password": "password"}, follow=True)

        self.assertEqual(response.context["message"],
                         "Changes were not submitted. A first name needs to be a string")

    def testInvalidLastName(self):
        response = self.client1.post("/EditMyUserProfile",
                                     {"first_name": "John", "last_name": "123", "user_type": "instructor",
                                      "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                      "home_address": "2514 N Farewell Ave",
                                      "password": "password"}, follow=True)

        self.assertEqual(response.context["message"],
                         "Changes were not submitted. A last name needs to be a string")

    def testInvalidAddress(self):
        response = self.client1.post("/EditMyUserProfile",
                                     {"first_name": "John", "last_name": "Doe", "user_type": "instructor",
                                      "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                      "home_address": "123",
                                      "password": "password"}, follow=True)

        self.assertEqual(response.context["message"],
                         "Changes were not submitted. A home address needs to be a string")

    def testInvalidEmail(self):
        response = self.client1.post("/EditMyUserProfile",
                                     {"first_name": "John", "last_name": "Doe", "user_type": "instructor",
                                      "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                      "home_address": "2514 N Farewell Ave",
                                      "password": "password"}, follow=True)

        self.assertEqual(response.context["message"],
                         "Changes were not submitted. A home address needs to be a string")

    def testInvalidUserType(self):
        response = self.client1.post("/EditMyUserProfile",
                                     {"first_name": "John", "last_name": "Doe", "user_type": "123",
                                      "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                      "home_address": "2514 N Farewell Ave",
                                      "password": "password"}, follow=True)

        self.assertEqual(response.context["message"],
                         "Changes were not submitted. A user type needs to be a string")

    def test_EditChangesAdmin(self):
        self.client1.post("/EditMyUserProfile",
                          {"first_name": "John", "last_name": "Doe", "user_type": "instructor",
                           "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                           "home_address": "2514 N Farewell Ave",
                           "password": "password"}, follow=True)

        self.assertNotEqual("Stephen_Doe", self.instructor.getUsername(),
                            "Supervisor was not edit successfully")

    def testEmptyFirstNameProvided(self):
        response = self.client1.post("/EditMyUserProfile",
                                     {"first_name": "", "last_name": "Doe", "user_type": "instructor",
                                      "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                      "home_address": "2514 N Farewell Ave",
                                      "password": "password"}, follow=True)

        self.assertEqual(response.context["message"], "User was not edited. First Name should not be left blank")

    def testEmptyLastNameProvided(self):
        response = self.client1.post("/EditMyUserProfile",
                                     {"first_name": "John", "last_name": "", "user_type": "instructor",
                                      "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                      "home_address": "2514 N Farewell Ave",
                                      "password": "password"}, follow=True)

        self.assertEqual(response.context["message"], "User was not edited. Last Name should not be left blank")

    def testEmptyUserTypeProvided(self):
        response = self.client1.post("/EditMyUserProfile",
                                     {"first_name": "John", "last_name": "Doe", "user_type": "",
                                      "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                      "home_address": "2514 N Farewell Ave",
                                      "new password": "password"}, follow=True)

        self.assertEqual(response.context["message"], "User was not edited. User Type should not be left blank")

    def testEmptyPhoneNumberProvided(self):
        response = self.client1.post("/EditMyUserProfile",
                                     {"first_name": "John", "last_name": "Doe", "user_type": "instructor",
                                      "email": "stephenDoe@aol.com", "phone_number": "",
                                      "home_address": "2514 N Farewell Ave",
                                      "new password": "password"}, follow=True)

        self.assertEqual(response.context["message"], "User was not edited. Phone Number should not be left blank")

    def testEmptyHomeAddressProvided(self):
        response = self.client1.post("/EditMyUserProfile",
                                     {"first_name": "John", "last_name": "Doe", "user_type": "instructor",
                                      "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                      "home_address": "",
                                      "new password": "password"}, follow=True)

        self.assertEqual(response.context["message"], "User was not edited. Home Address should not be left blank")

    def testEmptyEmailProvided(self):
        response = self.client1.post("/EditMyUserProfile",
                                     {"first_name": "John", "last_name": "Doe", "user_type": "instructor",
                                      "email": "", "phone_number": "1234567890",
                                      "home_address": "2514 N Farewell Ave",
                                      "new password": "password"}, follow=True)

        self.assertEqual(response.context["message"], "User was not edited. Home Address should not be left blank")


class TestEditMyUserProfileInstructor_to_Home(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave',
                            user_type='Instructor',
                            email='johnDoe@aol.com')

        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.instructor: InstructorUser = InstructorUser(user_model)
        user_model.save()

        self.client.post("/",
                         {"username": self.instructor.getUsername(), "password": self.instructor.getPassword()})

    def test_EditMyUserProfile_to_Home(self):
        # Make a GET request to //MyUserProfile
        response = self.client.get("/EditMyUserProfile")

        # Check that the response was a redirect to page /home
        self.assertRedirects(response, '/InstructorHome', status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

        # Follow the redirect and check that the final URL is '/home'
        response = response.follow()
        self.assertEqual(response.url, '/InstructorHome')


'''
SCENARIO: As an TA, I want to be able navigate the Edit My User Profile Page and Edit my Profile
-----------------------------------------------------------------------
SCENARIO: As an TA, I want to be able to change my profile information
GIVEN The user is an TA and is logged in and at the Edit My User Profile page
WHEN a user of type Admin is to be edited
WHEN user can be found with valid fields in the list of all users
AND "Submit Changes" is clicked
THEN account can be edited
-----------------------------------------------------------------------
SCENARIO: As an TA, I want to be able navigate to the Home Page
-----------------------------------------------------------------------
Acceptance Criteria 1:
GIVEN: The user is a TA and is logged in and at the Edit My Profile page
AND:They can click on "Return to Home"
THEN: They will be navigated to the "Admin Home" page
'''


class TestEditMyUserProfileTA(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave',
                            user_type='Admin',
                            email='johnDoe@aol.com')

        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.ta: TAUser = TAUser(user_model)
        user_model.save()

        self.client.post("/",
                         {"username": self.ta.getUsername(), "password": self.ta.getPassword()})

    def testInvalidPhoneNumber(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "Stephen", "last_name": "Doe", "user_type": "ta",
                                     "email": "stephenDoe@aol.com", "phone_number": "a2345678901",
                                     "home_address": "2514 N Farewell Ave",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["message"],
                         "Changes were not submitted. A phone number needs to be 10 digits")

    def testInvalidPassword(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "Stephen", "last_name": "Doe", "user_type": "ta",
                                     "email": "stephenDoe@aol.com", "phone_number": "a234567890",
                                     "home_address": "2514 N Farewell Ave",
                                     "password": "123"}, follow=True)

        self.assertEqual(response.context["message"],
                         "Changes were not submitted. A password needs to be a string")

    def testInvalidFirstName(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "123", "last_name": "Doe", "user_type": "ta",
                                     "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                     "home_address": "2514 N Farewell Ave",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["message"],
                         "Changes were not submitted. A first name needs to be a string")

    def testInvalidLastName(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "John", "last_name": "123", "user_type": "ta",
                                     "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                     "home_address": "2514 N Farewell Ave",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["message"],
                         "Changes were not submitted. A last name needs to be a string")

    def testInvalidAddress(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "John", "last_name": "Doe", "user_type": "ta",
                                     "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                     "home_address": "123",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["message"],
                         "Changes were not submitted. A home address needs to be a string")

    def testInvalidEmail(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "John", "last_name": "Doe", "user_type": "ta",
                                     "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                     "home_address": "2514 N Farewell Ave",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["message"],
                         "Changes were not submitted. A home address needs to be a string")

    def testInvalidUserType(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "John", "last_name": "Doe", "user_type": "123",
                                     "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                     "home_address": "2514 N Farewell Ave",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["message"],
                         "Changes were not submitted. A user type needs to be a string")

    def test_EditChangesTA(self):
        self.client.post("/EditMyUserProfile",
                         {"first_name": "John", "last_name": "Doe", "user_type": "ta",
                          "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                          "home_address": "2514 N Farewell Ave",
                          "password": "password"}, follow=True)

        self.assertNotEqual("Stephen_Doe", self.ta.getUsername(),
                            "Supervisor was not edit successfully")

    def testEmptyFirstNameProvided(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "", "last_name": "Doe", "user_type": "ta",
                                     "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                     "home_address": "2514 N Farewell Ave",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["message"], "User was not edited. First Name should not be left blank")

    def testEmptyLastNameProvided(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "John", "last_name": "", "user_type": "ta",
                                     "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                     "home_address": "2514 N Farewell Ave",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["message"], "User was not edited. Last Name should not be left blank")

    def testEmptyUserTypeProvided(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "John", "last_name": "Doe", "user_type": "",
                                     "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                     "home_address": "2514 N Farewell Ave",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["message"], "User was not edited. User Type should not be left blank")

    def testEmptyPhoneNumberProvided(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "John", "last_name": "Doe", "user_type": "ta",
                                     "email": "stephenDoe@aol.com", "phone_number": "",
                                     "home_address": "2514 N Farewell Ave",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["message"], "User was not edited. Phone Number should not be left blank")

    def testEmptyHomeAddressProvided(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "John", "last_name": "Doe", "user_type": "ta",
                                     "email": "stephenDoe@aol.com", "phone_number": "1234567890",
                                     "home_address": "",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["message"], "User was not edited. Home Address should not be left blank")

    def testEmptyEmailProvided(self):
        response = self.client.post("/EditMyUserProfile",
                                    {"first_name": "John", "last_name": "Doe", "user_type": "ta",
                                     "email": "", "phone_number": "1234567890",
                                     "home_address": "2514 N Farewell Ave",
                                     "password": "password"}, follow=True)

        self.assertEqual(response.context["message"], "User was not edited. Home Address should not be left blank")


class TestEditMyUserProfileTA_to_Home(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave',
                            user_type='TA',
                            email='johnDoe@aol.com')

        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.instructor: InstructorUser = InstructorUser(user_model)
        user_model.save()

        self.client.post("/",
                         {"username": self.instructor.getUsername(), "password": self.instructor.getPassword()})

    def test_EditMyUserProfile_to_Home(self):
        # Make a GET request to //MyUserProfile
        response = self.client.get("/EditMyUserProfile")

        # Check that the response was a redirect to page /home
        self.assertRedirects(response, '/TAHome', status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

        # Follow the redirect and check that the final URL is '/home'
        response = response.follow()
        self.assertEqual(response.url, '/TAHome')

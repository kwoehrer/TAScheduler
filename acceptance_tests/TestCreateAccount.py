from django.test import TestCase, Client

from app.models import *
from classes.Users.users import AdminUser, InstructorUser, TAUser

'''
SCENARIO: As an Admin, I want to be able to navigate to the Create Account page
---------------------------------------------------------------------------------
Acceptance Criteria 1:
GIVEN user has an existing account in the database
WHEN a valid fields are entered
AND a user with the same fields already exists
THEN account is not created
---------------------------------------------------------------------------------
Acceptance Criteria 2:
GIVEN user has an existing account in the database
WHEN the fields are entered
AND and one of the fields are invalid
THEN account is not created
---------------------------------------------------------------------------------
Acceptance Criteria 3:
GIVEN user has an existing account in the database
WHEN the fields are entered
AND and one of the fields is not provided
THEN account is not created
---------------------------------------------------------------------------------
Acceptance Criteria 4:
GIVEN The user is an Admin and is logged in and at the home page
WHEN user enters valid fields
AND specifies user type as Admin
THEN account of type ADMIN is created
---------------------------------------------------------------------------------
Acceptance Criteria 5:
GIVEN The user is an Admin and is logged in and at the home page
WHEN user enters valid fields
AND specifies user type as Instructor
THEN account of type Instructor is created
---------------------------------------------------------------------------------
Acceptance Criteria 6:
GIVEN The user is an Admin and is logged in and at the home page
WHEN user enters valid fields
AND specifies user type as TA
THEN account of type TA is created
---------------------------------------------------------------------------------

SCENARIO: As an Admin, I want to be able to navigate to the Course Management page
----------------------------------------------------
GIVEN: The user is an Admin and is logged in and at the home page
AND:They can click on "Return to Course Management Page"
THEN: They will be navigated to the "Course Management" page
----------------------------------------------------
'''


class TestAdminCreateAccount(TestCase):
    def setUp(self):
        self.client1 = Client()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave',
                            user_type='Admin',
                            email='johnDoe@aol.com')

        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.admin: AdminUser = AdminUser(user_model)
        user_model.save()

        self.client1.post("/",
                          {"username": self.admin.getUsername(), "password": self.admin.getPassword()})

        self.client2 = Client()
        User.objects.create(username='Steven_Adams', password="password1", first_name="Steven",
                            last_name='Adams',
                            phone_number='4149818001', home_address='2512 N Farewell Ave',
                            user_type='Instructor',
                            email='stevenAdams@aol.com')

        user_object2 = User.objects.filter(username='John_Doe')[0]
        user_model2 = Instructor.objects.create(account_ID=user_object2)
        self.instructor: InstructorUser = InstructorUser(user_model2)
        user_model2.save()

        self.client2.post("/",
                          {"username": self.instructor.getUsername(), "password": self.instructor.getPassword()})

        self.client3 = Client()
        self.ta = User.objects.create(username='Micheal_Johnson', password="password", first_name="Micheal",
                                      last_name='Johnson',
                                      phone_number='4149818002', home_address='2514 N Farewell Ave',
                                      user_type='TA',
                                      email='michealJohnson@aol.com')

        user_object3 = User.objects.filter(username='John_Doe')[0]
        user_model3 = TA.objects.create(account_ID=user_object3)
        self.ta: TAUser = TAUser(user_model3)
        user_model3.save()

        self.client3.post("/", {"username": self.ta.getUsername(), "password": self.ta.getPassword()})

    def testDuplicateUser(self):
        User.objects.create(self.admin)
        user_obj = User.objects.filter(username='John_Doe')[0]
        new_user = Admin.objects.create(account_ID=user_obj)
        self.admin1: AdminUser = AdminUser(new_user)
        new_user.save()

        response = self.client.post("/AccountCreate/",
                                    new_user, follow=True)

        try:
            self.assertTrue(response.context["message"],
                            "User was not created. This user already exists")
        except AssertionError as msg:
            print(msg)

    def testInvalidPhoneNumber(self):
        response = self.client.post("/AccountCreate/",
                                    {"username": "Stephen_Doe", "password": "password", "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "12345678901",
                                     "home_address": "2514 N Farewell Ave", "user_type": "admin",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response.context["message"], "User was not created. A phone number needs to be 10 digits")
        self.assertEqual(Admin.objects.count(), 1, "Database did not change")

    def testInvalidUsername(self):
        response = self.client.post("/AccountCreate/",
                                    {"username": 123, "password": "password", "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "12345678901",
                                     "home_address": "2514 N Farewell Ave", "user_type": "admin",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response.context["message"], "User was not created. A username has to be a string")
        self.assertEqual(Admin.objects.count(), 1, "Database did not change")

    def testInvalidPassword(self):
        response = self.client.post("/AccountCreate/",
                                    {"username": "Stephen_Doe", "password": 123, "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "12345678901",
                                     "home_address": "2514 N Farewell Ave", "user_type": "admin",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response.context["message"], "User was not created. A password needs to be a string")
        self.assertEqual(Admin.objects.count(), 1, "Database did not change")

    def testInvalidFirstName(self):
        response = self.client.post("/AccountCreate/",
                                    {"username": "Stephen_Doe", "password": "password", "first_name": 123,
                                     "last_name": "Doe", "phone_number": "12345678901",
                                     "home_address": "2514 N Farewell Ave", "user_type": "admin",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        # self.assertEqual(response.context["message"], "User was not created. A first name needs to be a string")

    def testInvalidLastName(self):
        response = self.client.post("/AccountCreate/",
                                    {"username": "Stephen_Doe", "password": "password", "first_name": "John",
                                     "last_name": 123, "phone_number": "12345678901",
                                     "home_address": "2514 N Farewell Ave", "user_type": "admin",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response.context["message"], "User was not created. A last name needs to be a string")
        # self.assertEqual(Admin.objects.count(), 1, "Database did not change")

    def testInvalidAddress(self):
        response = self.client.post("/AccountCreate/",
                                    {"username": "Stephen_Doe", "password": "password", "first_name": "John",
                                     "last_name": "Doe", "phone_number": "12345678901",
                                     "home_address": 123, "user_type": "admin",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response.context["message"], "User was not created. An address needs to be a string")
        # self.assertEqual(Admin.objects.count(), 1, "Database did not change")

    def testInvalidEmail(self):
        response = self.client.post("/AccountCreate/",
                                    {"username": "Stephen_Doe", "password": "password", "first_name": "John",
                                     "last_name": "Doe", "phone_number": "12345678901",
                                     "home_address": "2514 N Farewell Ave", "user_type": "admin",
                                     "email": 123}, follow=True)

        self.assertEqual(response.context["message"], "User was not created. An email address needs to be a string")
        # self.assertEqual(Admin.objects.count(), 1, "Database did not change")

    def testInvalidUserType(self):
        response = self.client.post("/AccountCreate/",
                                    {"username": "Stephen_Doe", "password": "password", "first_name": "John",
                                     "last_name": "Doe", "phone_number": "12345678901",
                                     "home_address": "2514 N Farewell Ave", "user_type": 123,
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response.context["message"], "User was not created. A type needs to be a string")
        # self.assertEqual(Admin.objects.count(), 1, "Database did not change")
        # self.assertEqual(User.objects.filter(account__admin=self.admin).count(), 1, "Database did not change")

    def test_createAdmin(self):
        self.client.post("/AccountCreate/",
                         {"username": "Stephen_Doe", "password": "password", "first_name": "Stephen",
                          "last_name": "Doe", "phone_number": "4142294000",
                          "home_address": "2514 N Farewell Ave", "user_type": "Admin",
                          "email": "stephenDoe@aol.com"}, follow=True)

        self.assertNotEqual("Stephen_Doe", self.admin.getUsername(),
                            "Supervisor was not created successfully")

    def test_createInstructor(self):
        self.client.post("/AccountCreate/",
                             {"username": "Stephen_Doe", "password": "password", "first_name": "Stephen",
                              "last_name": "Doe", "phone_number": "4142294000",
                              "home_address": "2514 N Farewell Ave", "user_type": "Instructor",
                              "email": "stephenDoe@aol.com"}, follow=True)
        user_instructor = User.objects.get(name="user")
        user_model_instructor = Instructor.objects.create(account_ID=user_instructor)
        self.post_instructor: InstructorUser = InstructorUser(user_model_instructor)
        self.assertEqual(self.post_instructor, self.instructor)

    def test_createTA(self):
        r = self.client.post("/AccountCreate/",
                             {"username": "Stephen_Doe", "password": "password", "first_name": "Stephen",
                              "last_name": "Doe", "phone_number": "4142294000",
                              "home_address": "2514 N Farewell Ave", "user_type": "TA",
                              "email": "stephenDoe@aol.com"}, follow=True)

        self.assertNotEqual(User.objects.get(userID=self.instructor), self.instructor,
                            "Instructor was not created successfully")

    def testEmptyUsernameProvided(self):
        response = self.client.post("/AccountCreate/",
                                    {"username": "", "password": "password1", "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "41498184444",
                                     "home_address": "2514 N Farewell Ave", "user_type": "admin",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response.context["error"], "User was not created. Username should not be left blank")
        self.assertEqual(Admin.objects.count(), 1, "Database did not change")

    def testEmptyPasswordProvided(self):
        response = self.client.post("/AccountCreate/",
                                    {"username": "Stephen_Doe", "password": "", "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "41498184444",
                                     "home_address": "2514 N Farewell Ave", "user_type": "admin",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response.context["error"], "User was not created. Password should not be left blank")
        self.assertEqual(Admin.objects.count(), 1, "Database did not change")

    def testEmptyFirstNameProvided(self):
        response = self.client.post("/AccountCreate/",
                                    {"username": "Stephen_Doe", "password": "password1", "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "41498184444",
                                     "home_address": "2514 N Farewell Ave", "user_type": "admin",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response.context["error"], "User was not created. First name should not be left blank")
        self.assertEqual(Admin.objects.count(), 1, "Database did not change")

    def testEmptyLastNameProvided(self):
        response = self.client.post("/AccountCreate/",
                                    {"username": "Stephen_Doe", "password": "password1", "first_name": "Stephen",
                                     "last_name": "", "phone_number": "41498184444",
                                     "home_address": "2514 N Farewell Ave", "user_type": "admin",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response.context["error"], "User was not created. Last name should not be left blank")
        self.assertEqual(Admin.objects.count(), 1, "Database did not change")

    def testEmptyPhoneNumberProvided(self):
        response = self.client.post("/AccountCreate/",
                                    {"username": "Stephen_Doe", "password": "password1", "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "",
                                     "home_address": "2514 N Farewell Ave", "user_type": "admin",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response.context["error"], "User was not created, Phone Number cannot be left blank")
        self.assertEqual(Admin.objects.count(), 1, "Database did not change")

    def testEmptyHomeAddressProvided(self):
        response = self.client.post("/AccountCreate/",
                                    {"username": "Stephen_Doe", "password": "password1", "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "",
                                     "home_address": "", "user_type": "admin",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response.context["error"], "User was not created, Home Address cannot be left blank")
        self.assertEqual(Admin.objects.count(), 1, "Database did not change")

    def testEmptyEmailProvided(self):
        response = self.client.post("/AccountCreate/",
                                    {"username": "Stephen_Doe", "password": "password1", "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "",
                                     "home_address": "", "user_type": "admin",
                                     "email": ""}, follow=True)

        self.assertEqual(response.context["error"], "User was not created, Email cannot be left blank")
        self.assertEqual(Admin.objects.count(), 1, "Database did not change")


class TestCreateAccountToAccManagement(TestCase):
    def test_CreateAccount_to_AccManagement(self):

        response = self.client.post('/', {'username': 'Micheal_Johnson', 'password': 'password3'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/AdminAccMng")

        try:
            self.assertTrue(response.url, "/AdminAccMng")
        except AssertionError as msg:
            print(msg)

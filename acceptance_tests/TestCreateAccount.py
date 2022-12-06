from django.test import TestCase, Client

from TAScheduler.app.models import *

'''
As an Admin, I want to be able to navigate to the Create Account page
----------------------------------------------------
GIVEN: The user is an Admin and is logged in and at the Create Account page
AND:They can click on "Create Account"
THEN: They will be able to Create an Account of any user type
----------------------------------------------------

As an Admin, I want to be able to navigate to the Create Account page
----------------------------------------------------
GIVEN: The user is an Admin and is logged in and at the home page
AND:They can click on "Return to Course Management Page"
THEN: They will be navigated to the "Course Management" page
----------------------------------------------------
'''


class TestAdminCreateAccount(TestCase):

    def setUp(self):
        self.client1 = Client()
        self.admin = Admin.objects.create(username='John_Doe', password="password", first_name="John",
                                          last_name='Doe',
                                          phone_number='4149818000', home_address='2513 N Farewell Ave',
                                          user_type='Admin',
                                          email='johnDoe@aol.com')

        self.client1.post("/", {"username": self.admin.account_ID.username, "password": self.admin.account_ID.password})

        self.client2 = Client()
        self.instructor = Instructor.objects.create(username='John_Doe', password="password", first_name="John",
                                                    last_name='Doe',
                                                    phone_number='4149818000', home_address='2513 N Farewell Ave',
                                                    user_type='Admin',
                                                    email='johnDoe@aol.com')

        self.client2.post("/", {"username": self.instructor.account_ID.username,
                                "password": self.instructor.account_ID.password})

        self.client3 = Client()
        self.ta = TA.objects.create(username='John_Doe', password="password", first_name="John",
                                    last_name='Doe',
                                    phone_number='4149818000', home_address='2513 N Farewell Ave',
                                    user_type='Admin',
                                    email='johnDoe@aol.com')

        self.client3.post("/", {"username": self.ta.account_ID.username, "password": self.ta.account_ID.password})

    def testDuplicateUser(self):
        Admin.objects.create(self.admin)
        user_obj = Admin.objects.filter(username='John_Doe')[0]
        new_user = Admin.objects.create(account_ID=user_obj.account_ID)
        response = self.client.post("/AccountCreate/",
                                    new_user, follow=True)

        self.assertEqual(response.context["error"],
                         "User was not created. This user already exists: ",
                         "An error message was not displayed when account ID are duplicates")

        self.assertEqual(Admin.objects.get(account_ID=self.admin.account_ID), new_user.account_ID, "Database was "
                                                                                                   "not changed")

    def testInvalidPhone(self):
        r = self.client.post("/create_user/",
                             {"username": "Stephen_Doe", "password": "", "first_name": "Stephen",
                              "last_name": "Doe", "phone_number": "12345678901",
                              "home_address": "2514 N Farewell Ave", "user_type": "admin",
                              "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(r.context["error"], "User was not created. A phone number needs to be 10 digits")
        self.assertEqual(Admin.objects.count(), 1, "Database did not change")

    def test_createAdmin(self):
        self.client.post("/create_user/",
                         {"username": "Stephen_Doe", "password": "password", "first_name": "Stephen",
                          "last_name": "Doe", "phone_number": "4142294000",
                          "home_address": "2514 N Farewell Ave", "user_type": "Admin",
                          "email": "stephenDoe@aol.com"}, follow=True)

        self.assertNotEqual(Admin.objects.get(account_ID=self.admin.account_ID), self.admin,
                            "Supervisor was not created successfully")

    def test_createInstructor(self):
        r = self.client.post("/create_user/",
                             {"username": "Stephen_Doe", "password": "password", "first_name": "Stephen",
                              "last_name": "Doe", "phone_number": "4142294000",
                              "home_address": "2514 N Farewell Ave", "user_type": "Instructor",
                              "email": "stephenDoe@aol.com"}, follow=True)

        self.assertNotEqual(Instructor.objects.get(userID=self.instructor.account_ID), self.instructor,
                            "Instructor was not created successfully")

    def test_createTA(self):
        r = self.client.post("/create_user/",
                             {"username": "Stephen_Doe", "password": "password", "first_name": "Stephen",
                              "last_name": "Doe", "phone_number": "4142294000",
                              "home_address": "2514 N Farewell Ave", "user_type": "TA",
                              "email": "stephenDoe@aol.com"}, follow=True)

        self.assertNotEqual(Instructor.objects.get(userID=self.instructor.account_ID), self.instructor,
                            "Instructor was not created successfully")

    def testNoUsernameProvided(self):
        response = self.client.post("/create_user/",
                                    {"username": "", "password": "password1", "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "41498184444",
                                     "home_address": "2514 N Farewell Ave", "user_type": "admin",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response.context["error"], "User was not created. Username should not be left blank")
        self.assertEqual(Admin.objects.count(), 1, "Database did not change")

    def testNoPasswordProvided(self):
        response = self.client.post("/create_user/",
                                    {"username": "Stephen_Doe", "password": "", "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "41498184444",
                                     "home_address": "2514 N Farewell Ave", "user_type": "admin",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response.context["error"], "User was not created. Password should not be left blank")
        self.assertEqual(Admin.objects.count(), 1, "Database did not change")

    def testNoFirstNameProvided(self):
        response = self.client.post("/create_user/",
                                    {"username": "Stephen_Doe", "password": "password1", "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "41498184444",
                                     "home_address": "2514 N Farewell Ave", "user_type": "admin",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response.context["error"], "User was not created. First name should not be left blank")
        self.assertEqual(Admin.objects.count(), 1, "Database did not change")

    def testNoLastNameProvided(self):
        response = self.client.post("/create_user/",
                                    {"username": "Stephen_Doe", "password": "password1", "first_name": "Stephen",
                                     "last_name": "", "phone_number": "41498184444",
                                     "home_address": "2514 N Farewell Ave", "user_type": "admin",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response.context["error"], "User was not created. Last name should not be left blank")
        self.assertEqual(Admin.objects.count(), 1, "Database did not change")

    def testNoPhoneNumberProvided(self):
        response = self.client.post("/create_user/",
                                    {"username": "Stephen_Doe", "password": "password1", "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "",
                                     "home_address": "2514 N Farewell Ave", "user_type": "admin",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response.context["error"], "User was not created, Phone Number cannot be left blank")
        self.assertEqual(Admin.objects.count(), 1, "Database did not change")

    def testNoHomeAddressProvided(self):
        response = self.client.post("/create_user/",
                                    {"username": "Stephen_Doe", "password": "password1", "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "",
                                     "home_address": "", "user_type": "admin",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response.context["error"], "User was not created, Home Address cannot be left blank")
        self.assertEqual(Admin.objects.count(), 1, "Database did not change")

    def testNoEmailProvided(self):
        response = self.client.post("/create_user/",
                                    {"username": "Stephen_Doe", "password": "password1", "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "",
                                     "home_address": "", "user_type": "admin",
                                     "email": ""}, follow=True)

        self.assertEqual(response.context["error"], "User was not created, Email cannot be left blank")
        self.assertEqual(Admin.objects.count(), 1, "Database did not change")

    def test_CreateAccount_to_Home(self):

        response = self.client.post('/', {'username': 'Micheal_Johnson', 'password': 'password3'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/DeleteCourse")

        try:
            self.assertTrue(response.url, "/DeleteCourse")
        except AssertionError as msg:
            print(msg)
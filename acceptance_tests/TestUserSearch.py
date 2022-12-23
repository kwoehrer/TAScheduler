from django.test import TestCase, Client
from app.models import *
from classes.Users.users import AdminUser, InstructorUser, TAUser

'''
As an Admin, I want to be able navigate the Users Page and Query a User
-----------------------------------------------------------------------
SCENARIO: As an Admin, I want to be able to navigate to the User Search page
GIVEN The user is an Admin and is logged in and at the User Search page
WHEN a user of type Admin is to be queried
WHEN user can be found with valid fields in the list of all users
AND "Search for account" is clicked
THEN account can be viewed
-----------------------------------------------------------------------
SCENARIO: As an Admin, I want to be able to navigate to the User Search page
GIVEN The user is an Admin and is logged in and at User Search page
WHEN a user of type Instructor is to be queried
WHEN user can be found with valid fields in the list of all users
AND "Search for account" is clicked
THEN account can be viewed
-----------------------------------------------------------------------
SCENARIO: As an Admin, I want to be able to navigate to the User Search page
GIVEN The user is an Admin and is logged in and at the User Search page
WHEN a user of type TA is to be queried
WHEN user can be found with valid fields in the list of all users
AND "Search for account" is clicked
THEN account can be viewed
-----------------------------------------------------------------------
As an Admin, I want to be able navigate to the Search Home Page
-----------------------------------------------------------------------
Scenario: As an Admin, I am currently in the User Search Page
GIVEN: The user is a Admin and is logged in and at the User Search page
AND:They can click on "Return to Search Page"
THEN: They will be navigated to the "SearchHome" page
'''


class TestUserSearchAdmin(TestCase):
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

    # def test_UserExists(self):
    #     User.objects.create(self.admin)
    #     user_obj = Admin.objects.filter(username='John_Doe')[0]
    #     new_user = Admin.objects.create(account_ID=user_obj)
    #     self.admin1: AdminUser = AdminUser(new_user)
    #     new_user.save()
    #
    #     self.client.post({"/searchStates/UserSearch",
    #                       self.admin1})
    #
    #     self.assertEqual(self.admin1.getID(), User.objects.get(account_ID=self.admin.getID()), "User exists in "
    #                                                                                             "Database")

    def testEmptyUsernameProvided(self):
        response = self.client.post("/searchStates/UserSearch",
                                    {"username": "", "password": "password1", "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "41498184444",
                                     "home_address": "2514 N Farewell Ave", "user_type": "admin",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response, "User was not found. Username should not be left blank")

    def testEmptyFirstNameProvided(self):
        response = self.client.post("/searchStates/UserSearch",
                                    {"username": "Stephen_Doe", "password": "password1", "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "41498184444",
                                     "home_address": "2514 N Farewell Ave", "user_type": "admin",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response, "User was not created. First name should not be left blank")

    def testEmptyLastNameProvided(self):
        response = self.client.post("/searchStates/UserSearch",
                                    {"username": "Stephen_Doe", "password": "password1", "first_name": "Stephen",
                                     "last_name": "", "phone_number": "41498184444",
                                     "home_address": "2514 N Farewell Ave", "user_type": "admin",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response, "User was not created. Last name should not be left blank")

    def testEmptyEmailProvided(self):
        response = self.client.post("/searchStates/UserSearch",
                                    {"username": "Stephen_Doe", "password": "password1", "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "",
                                     "home_address": "", "user_type": "admin",
                                     "email": ""}, follow=True)

        self.assertEqual(response, "User was not created, Email cannot be left blank")


class TestUserSearchNavigateAdmin(TestCase):

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

    def test_UserSearch_to_HomeSearch(self):
        # Make a GET request to /searchStates/UserSearch
        response = self.client.get("/searchStates/UserSearch")

        # Check that the response was a redirect to page /searchStates/SearchHome
        self.assertRedirects(response, '/searchStates/SearchHome', status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

        # Follow the redirect and check that the final URL is '/searchStates/SearchHome'
        response = response.follow()
        self.assertEqual(response.url, '/searchStates/SearchHome')


'''
As an Instructor, I want to be able navigate the Users Page and Query a User
-----------------------------------------------------------------------
SCENARIO: As an Instructor, I want to be able to navigate to the User Search page
GIVEN The user is an Instructor and is logged in and at User Search page
WHEN a user of type Instructor is to be queried
WHEN user can be found with valid fields in the list of all users
AND "Search for account" is clicked
THEN account can be viewed
-----------------------------------------------------------------------
SCENARIO: As an Instructor, I want to be able to navigate to the User Search page
GIVEN The user is an Instructor and is logged in and at the User Search page
WHEN a user of type TA is to be queried
WHEN user can be found with valid fields in the list of all users
AND "Search for account" is clicked
THEN account can be viewed
-----------------------------------------------------------------------
As an Instructor, I want to be able navigate to the Search Home Page
-----------------------------------------------------------------------
Scenario: As an Instructor, I am currently in the User Search Page
GIVEN: The user is a Admin and is logged in and at the User Search page
AND:They can click on "Return to Search Page"
THEN: They will be navigated to the "SearchHome" page
'''


class TestUserSearchInstructor(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj)

        self.instructor: InstructorUser = InstructorUser(user_model)

        self.client.post("/",
                         {"username": self.instructor.getUsername(), "password": self.instructor.getPassword()})

    # def test_UserExists(self):
    #     User.objects.create(self.instructor)
    #     user_obj = User.objects.filter(username='John_Doe')[0]
    #     new_user = Instructor.objects.create(account_ID=user_obj)
    #     self.instructor1: InstructorUser = InstructorUser(new_user)
    #     new_user.save()
    #
    #     self.client.post({"/searchStates/UserSearch",
    #                       self.instructor1})
    #
    #     self.assertEqual(self.instructor1.getID(), User.objects.get(account_ID=self.instructor.getID()),
    #                      "User exists in "
    #                      "Database")

    def testEmptyUsernameProvided(self):
        response = self.client.post("/searchStates/UserSearch",
                                    {"username": "", "password": "password1", "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "41498184444",
                                     "home_address": "2514 N Farewell Ave", "user_type": "instructor",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response, "User was not found. Username should not be left blank")

    def testEmptyFirstNameProvided(self):
        response = self.client.post("/searchStates/UserSearch",
                                    {"username": "Stephen_Doe", "password": "password1", "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "41498184444",
                                     "home_address": "2514 N Farewell Ave", "user_type": "instructor",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response, "User was not created. First name should not be left blank")

    def testEmptyLastNameProvided(self):
        response = self.client.post("/searchStates/UserSearch",
                                    {"username": "Stephen_Doe", "password": "password1", "first_name": "Stephen",
                                     "last_name": "", "phone_number": "41498184444",
                                     "home_address": "2514 N Farewell Ave", "user_type": "instructor",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response, "User was not created. Last name should not be left blank")

    def testEmptyEmailProvided(self):
        response = self.client.post("/searchStates/UserSearch",
                                    {"username": "Stephen_Doe", "password": "password1", "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "",
                                     "home_address": "", "user_type": "instructor",
                                     "email": ""}, follow=True)

        self.assertEqual(response, "User was not created, Email cannot be left blank")


class TestUserSearchNavigateInstructor(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj)

        self.instructor: InstructorUser = InstructorUser(user_model)

        self.client.post("/",
                         {"username": self.instructor.getUsername(), "password": self.instructor.getPassword()})

    def test_UserSearch_to_HomeSearch(self):
        # Make a GET request to /searchStates/UserSearch
        response = self.client.get("/searchStates/UserSearch")

        # Check that the response was a redirect to page /searchStates/SearchHome
        self.assertRedirects(response, '/searchStates/SearchHome', status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

        # Follow the redirect and check that the final URL is '/searchStates/SearchHome'
        response = response.follow()
        self.assertEqual(response.url, '/searchStates/SearchHome')


'''
As an TA, I want to be able navigate the Users Page and Query a User
-----------------------------------------------------------------------
SCENARIO: As an TA, I want to be able to navigate to the User Search page
GIVEN The user is an Instructor and is logged in and at User Search page
WHEN a user of type TA is to be queried
WHEN user can be found with valid fields in the list of all users
AND "Search for account" is clicked
THEN account can be viewed
-----------------------------------------------------------------------
As an Instructor, I want to be able navigate to the Search Home Page
-----------------------------------------------------------------------
Scenario: As an TA, I am currently in the User Search Page
GIVEN: The user is a TA and is logged in and at the User Search page
AND:They can click on "Return to Search Page"
THEN: They will be navigated to the "SearchHome" page
'''


class TestUserSearchTA(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj)

        self.admin: TAUser = TAUser(user_model)

        self.client.post("/",
                         {"username": self.admin.getUsername(), "password": self.admin.getPassword()})

    # def test_UserExists(self):
    #     User.objects.create(self.admin)
    #     user_obj = User.objects.filter(username='John_Doe')[0]
    #     new_user = TA.objects.create(account_ID=user_obj)
    #     self.ta1: TAUser = TAUser(new_user)
    #     new_user.save()
    #
    #     self.client.post({"/searchStates/UserSearch",
    #                       self.ta1})
    #
    #     self.assertEqual(self.ta1.getID(), User.objects.get(account_ID=self.ta1.getID()), "User exists in "
    #                                                                                     "Database")

    def testEmptyUsernameProvided(self):
        response = self.client.post("/searchStates/UserSearch",
                                    {"username": "", "password": "password1", "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "41498184444",
                                     "home_address": "2514 N Farewell Ave", "user_type": "ta",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response, "User was not found. Username should not be left blank")

    def testEmptyFirstNameProvided(self):
        response = self.client.post("/searchStates/UserSearch",
                                    {"username": "Stephen_Doe", "password": "password1", "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "41498184444",
                                     "home_address": "2514 N Farewell Ave", "user_type": "ta",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response, "User was not created. First name should not be left blank")

    def testEmptyLastNameProvided(self):
        response = self.client.post("/searchStates/UserSearch",
                                    {"username": "Stephen_Doe", "password": "password1", "first_name": "Stephen",
                                     "last_name": "", "phone_number": "41498184444",
                                     "home_address": "2514 N Farewell Ave", "user_type": "ta",
                                     "email": "stephenDoe@aol.com"}, follow=True)

        self.assertEqual(response, "User was not created. Last name should not be left blank")

    def testEmptyEmailProvided(self):
        response = self.client.post("/searchStates/UserSearch",
                                    {"username": "Stephen_Doe", "password": "password1", "first_name": "Stephen",
                                     "last_name": "Doe", "phone_number": "",
                                     "home_address": "", "user_type": "ta",
                                     "email": ""}, follow=True)

        self.assertEqual(response, "User was not created, Email cannot be left blank")


class TestUserSearchNavigateTA(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj)

        self.admin: TAUser = TAUser(user_model)

        self.client.post("/",
                         {"username": self.admin.getUsername(), "password": self.admin.getPassword()})

    def test_UserSearch_to_HomeSearch(self):
        # Make a GET request to /searchStates/UserSearch
        response = self.client.get("/searchStates/UserSearch")

        # Check that the response was a redirect to page /searchStates/SearchHome
        self.assertRedirects(response, '/searchStates/SearchHome', status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

        # Follow the redirect and check that the final URL is '/searchStates/SearchHome'
        response = response.follow()
        self.assertEqual(response.url, '/searchStates/SearchHome')

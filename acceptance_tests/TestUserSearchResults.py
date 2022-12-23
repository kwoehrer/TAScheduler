from django.test import TestCase, Client
from app.models import *
from classes.Users.users import AdminUser, InstructorUser, TAUser

'''
As an Admin, I want to be able to navigate to the Search Home page
----------------------------------------------------
Scenario: Navigate to the User Search Page
GIVEN: GIVEN: The user is an Admin and is logged in and at the User Search Results Page
AND: They can click on "Return to Search Page"
THEN: They will be navigated to the "Search Home"
----------------------------------------------------
'''


class TestAdminSearchHomePage(TestCase):
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

    def test_UserSearch_to_HomeSearch(self):
        # Make a GET request to /searchStates/UserSearch
        response = self.client.get("/searchStates/UserSearchResults")

        # Check that the response was a redirect to page /searchStates/SearchHome
        self.assertRedirects(response, '/searchStates/SearchHome', status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

        # Follow the redirect and check that the final URL is '/searchStates/SearchHome'
        response = response.follow()
        self.assertEqual(response.url, '/searchStates/SearchHome')


'''
As an Instructor, I want to be able to navigate to the Search Home page
----------------------------------------------------
Scenario: Navigate to the User Search Page
GIVEN: The user is an Instructor and is logged in and at the Search Home Page view
AND: They can click on "Return to Search Page"
THEN: They will be navigated to the "Search Home"
----------------------------------------------------
'''


class TestInstructorSearchHomePage(TestCase):
    client = None
    admin = None

    def setUp(self):
        self.client = Client()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave',
                            user_type='Instructor',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_object)
        self.instructor: InstructorUser = InstructorUser(user_model)

        self.client.login(username='John_Doe', password='password')

    def test_UserSearch_to_HomeSearch(self):
        # Make a GET request to /searchStates/UserSearch
        response = self.client.get("/searchStates/UserSearchResults")

        # Check that the response was a redirect to page /searchStates/SearchHome
        self.assertRedirects(response, '/searchStates/SearchHome', status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

        # Follow the redirect and check that the final URL is '/searchStates/SearchHome'
        response = response.follow()
        self.assertEqual(response.url, '/searchStates/SearchHome')


'''
As a TA, I want to be able to navigate to the Search Home page
----------------------------------------------------
Scenario: Navigate to the User Search Page
GIVEN: The user is an TA and is logged in and at the Search Home Page view
AND: They can click on "Return to Search Page"
THEN: They will be navigated to the "Search Home"
----------------------------------------------------
'''


class TestATASearchHomePage(TestCase):
    client = None
    admin = None

    def setUp(self):
        self.client = Client()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave',
                            user_type='TA',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_object)
        self.admin: TAUser = TAUser(user_model)

        self.client.login(username='John_Doe', password='password')

    def test_UserSearch_to_HomeSearch(self):
        # Make a GET request to /searchStates/UserSearch
        response = self.client.get("/searchStates/UserSearchResults")

        # Check that the response was a redirect to page /searchStates/SearchHome
        self.assertRedirects(response, '/searchStates/SearchHome', status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

        # Follow the redirect and check that the final URL is '/searchStates/SearchHome'
        response = response.follow()
        self.assertEqual(response.url, '/searchStates/SearchHome')

from django.test import TestCase, Client
from app.models import *
from classes.Users.users import TAUser

'''
As an Instructor, I want to be able navigate the Instructor View State Page
-----------------------------------------------------------------------
SCENARIO: As an Instructor, I want to be able to correctly view course information if I log into the Instructor 
View State Page
GIVEN The user is an Admin and is logged in and at the Admin View State page
THEN all profile information should be correctly displayed
-----------------------------------------------------------------------
'''


class TestCourseSearchAdmin(TestCase):
    def setUp(self):
        self.client = Client()

        User.objects.create(username='John_Doe', password="password123", first_name="John",
                            last_name='Doe',
                            phone_number='4149818008', home_address='2516 N Farewell Ave',
                            user_type='TA',
                            email='johnDoe1@aol.com')

        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_object)
        self.ta: TAUser = TAUser(user_model)
        user_model.save()

    def testTAProfileInfo(self):
        response = self.client.get('/ProfileStates/AdminViewState')
        self.assertContains(response, self.ta.getFirstName())
        self.assertContains(response, self.ta.getLastName())
        self.assertContains(response, self.ta.getUserType())
        self.assertContains(response, self.ta.getEmail())
        self.assertContains(response, self.ta.getCourses())
        self.assertContains(response, self.ta.getPhoneNumber())
        self.assertContains(response, self.ta.getHomeAddress())

    def test_AdminViewState_to_SearchPage(self):
        # Make a GET request to /searchStates/UserSearch
        response = self.client.get("/ProfileStates/InstrViewState")

        # Check that the response was a redirect to page /searchStates/SearchHome
        self.assertRedirects(response, '/searchStates/UserSearch', status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

        # Follow the redirect and check that the final URL is '/searchStates/SearchHome'
        response = response.follow()
        self.assertEqual(response.url, '/searchStates/SearchHome')

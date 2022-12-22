from django.test import TestCase, Client
from app.models import *
from classes.Users.users import AdminUser, InstructorUser, TAUser

'''
As an Admin, I want to be able navigate the Admin View State Page
-----------------------------------------------------------------------
SCENARIO: As an Admin, I want to be able to correctly view course information if I log into the Admin View State Page
GIVEN The user is an Admin and is logged in and at the Admin View State page
THEN all profile information should be correctly displayed
-----------------------------------------------------------------------
'''


class TestCourseSearchAdmin(TestCase):
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
        user_model.save()

        self.client = Client()

        User.objects.create(username='John_Doe1', password="password123", first_name="John",
                            last_name='Doe1',
                            phone_number='4149818008', home_address='2516 N Farewell Ave',
                            user_type='TA',
                            email='johnDoe1@aol.com')

        user_object = User.objects.filter(username='John_Doe1')[0]
        user_model = TA.objects.create(account_ID=user_object)
        self.ta: TAUser = TAUser(user_model)
        user_model.save()

    def testInstructorProfileInfo(self):
        response = self.client.get('/ProfileStates/AdminViewState')
        self.assertContains(response, self.instructor.getFirstName())
        self.assertContains(response, self.instructor.getLastName())
        self.assertContains(response, self.instructor.getUserType())
        self.assertContains(response, self.instructor.getEmail())
        self.assertContains(response, self.instructor.getCourses())
        self.assertContains(response, self.instructor.getPhoneNumber())
        self.assertContains(response, self.instructor.getHomeAddress())

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
        response = self.client.get("/ProfileStates/AdminViewState")

        # Check that the response was a redirect to page /searchStates/SearchHome
        self.assertRedirects(response, '/searchStates/UserSearch', status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

        # Follow the redirect and check that the final URL is '/searchStates/SearchHome'
        response = response.follow()
        self.assertEqual(response.url, '/searchStates/SearchHome')

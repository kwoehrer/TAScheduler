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


class TestAdminViewState(TestCase):
    def setUp(self):
        self.client1 = Client()

        User.objects.create(username='Micheal_Owen', password="password123", first_name="Micheal",
                            last_name='Owen',
                            phone_number='4149828004', home_address='2513 N Farewell Ave',
                            user_type='Admin',
                            email='johnDoe1@aol.com')

        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.instructor: AdminUser = AdminUser(user_model)
        user_model.save()

        self.client2 = Client()

        User.objects.create(username='John_Doe', password="password", first_name="John",
                            last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave',
                            user_type='Instructor',
                            email='johnDoe@aol.com')

        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_object)
        self.instructor: InstructorUser = InstructorUser(user_model)
        user_model.save()

        self.client3 = Client()

        User.objects.create(username='Steven_Adams', password="password123", first_name="John",
                            last_name='Adams',
                            phone_number='4149818008', home_address='2516 N Farewell Ave',
                            user_type='TA',
                            email='johnDoe1@aol.com')

        user_object = User.objects.filter(username='Steven_Adams')[0]
        user_model = TA.objects.create(account_ID=user_object)
        self.ta: TAUser = TAUser(user_model)
        user_model.save()

    def testAdminProfileInfo(self):
        response = self.client1.get('/ProfileStates/AdminViewState')
        self.assertContains(response, self.instructor.getFirstName())
        self.assertContains(response, self.instructor.getLastName())
        self.assertContains(response, self.instructor.getUserType())
        self.assertContains(response, self.instructor.getEmail())
        self.assertContains(response, self.instructor.getCourses())
        self.assertContains(response, self.instructor.getPhoneNumber())
        self.assertContains(response, self.instructor.getHomeAddress())

    def testInstructorProfileInfo(self):
        response = self.client2.get('/ProfileStates/AdminViewState')
        self.assertContains(response, self.instructor.getFirstName())
        self.assertContains(response, self.instructor.getLastName())
        self.assertContains(response, self.instructor.getUserType())
        self.assertContains(response, self.instructor.getEmail())
        self.assertContains(response, self.instructor.getCourses())
        self.assertContains(response, self.instructor.getPhoneNumber())
        self.assertContains(response, self.instructor.getHomeAddress())

    def testTAProfileInfo(self):
        response = self.client3.get('/ProfileStates/AdminViewState')
        self.assertContains(response, self.ta.getFirstName())
        self.assertContains(response, self.ta.getLastName())
        self.assertContains(response, self.ta.getUserType())
        self.assertContains(response, self.ta.getEmail())
        self.assertContains(response, self.ta.getCourses())
        self.assertContains(response, self.ta.getPhoneNumber())
        self.assertContains(response, self.ta.getHomeAddress())

    def test_AdminViewState_to_SearchPage(self):
        # Make a GET request to /searchStates/UserSearch
        response = self.client1.get("/ProfileStates/AdminViewState")

        # Check that the response was a redirect to page /searchStates/SearchHome
        self.assertRedirects(response, '/searchStates/UserSearch', status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

        # Follow the redirect and check that the final URL is '/searchStates/SearchHome'
        response = response.follow()
        self.assertEqual(response.url, '/searchStates/SearchHome')
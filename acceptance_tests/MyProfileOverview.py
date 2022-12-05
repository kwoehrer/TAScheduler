from django.test import TestCase, Client

from TAScheduler.app.models import *

'''
As a TA, I want to be able to navigate to the View my profile info page
----------------------------------------------------
GIVEN: The user is a TA and is logged in and at the My Profile Overview
AND:They can click on "Edit My Information"
THEN: They will be navigated to the "Edit My Information" page
As a user, I want to be able to navigate to the Edit My Information page
----------------------------------------------------
GIVEN: The user is a TA and is logged in and at the My Profile Overview
AND:They can click on "Home Page"
THEN: They will be navigated to the "Home Page" page
As a user, I want to be able to navigate to the Home page
----------------------------------------------------
'''


class TestTAProfileOverview(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.user_ta = TA.objects.create(username='John_Doe', password="password", first_name="John",
                                         last_name='Doe',
                                         phone_number='4149818000', home_address='2513 N Farewell Ave',
                                         user_type='TA',
                                         email='johnDoe@aol.com')

    def test_MyProfileView_to_Edit_My_Information(self):

        r = self.client.post('/', {'username': 'John_Doe', 'password': 'password'})
        self.assertTrue(r.context is None)

        try:
            self.assertTrue(r.url, "MyProfileOverview")
        except AssertionError as msg:
            print(msg)

        r = self.client.get("/EditMyInformation")

        try:
            self.assertTrue(r.url, "/EditMyInformation")
        except AssertionError as msg:
            print(msg)

    def test_MyProfileView_to_home(self):

        r = self.client.post('/', {'username': 'John_Doe', 'password': 'password'})
        self.assertTrue(r.context is None)

        try:
            self.assertTrue(r.url, "MyProfileOverview")
        except AssertionError as msg:
            print(msg)

        r = self.client.get("/home")

        try:
            self.assertTrue(r.url, "/home")
        except AssertionError as msg:
            print(msg)


'''
As an Instructor, I want to be able to navigate to the View my profile info page
----------------------------------------------------
GIVEN: The user is an Instructor and is logged in and at the My Profile Overview
AND:They can click on "Edit My Information"
THEN: They will be navigated to the "Edit My Information" page
As a user, I want to be able to navigate to the Edit My Information page
----------------------------------------------------
GIVEN: The user is an Instructor and is logged in and at the My Profile Overview
AND:They can click on "Home Page"
THEN: They will be navigated to the "Home Page" page
As a user, I want to be able to navigate to the Home page
----------------------------------------------------
'''


class TestInstructorProfileOverview(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.user_instructor = Instructor.objects.create(username='Steven_Adams', password="passwordNew",
                                                         first_name="Steven",
                                                         last_name='Adams',
                                                         phone_number='4149818222', home_address='2512 N Kenwood Ave',
                                                         user_type='Instructor',
                                                         email='stevenAdams@aol.com')

    def test_MyProfileView_to_Edit_My_Information(self):

        r = self.client.post('/', {'username': 'Steven_Adams', 'password': 'passwordNew'})
        self.assertTrue(r.context is None)

        try:
            self.assertTrue(r.url, "MyProfileOverview")
        except AssertionError as msg:
            print(msg)

        r = self.client.get("/EditMyInformation")

        try:
            self.assertTrue(r.url, "/EditMyInformation")
        except AssertionError as msg:
            print(msg)

    def test_MyProfileView_to_home(self):

        r = self.client.post('/', {'username': 'Steven_Adams', 'password': 'passwordNew'})
        self.assertTrue(r.context is None)

        try:
            self.assertTrue(r.url, "MyProfileOverview")
        except AssertionError as msg:
            print(msg)

        r = self.client.get("/home")

        try:
            self.assertTrue(r.url, "/home")
        except AssertionError as msg:
            print(msg)


'''
As an Admin, I want to be able to navigate to the View my profile info page
----------------------------------------------------
GIVEN: The user is a Admin and is logged in and at the My Profile Overview
AND:They can click on "Edit My Information"
THEN: They will be navigated to the "Edit My Information" page
As a user, I want to be able to navigate to the Edit My Information page
----------------------------------------------------
GIVEN: The user is a Admin and is logged in and at the My Profile Overview
AND:They can click on "Home Page"
THEN: They will be navigated to the "Home Page" page
As a user, I want to be able to navigate to the Home page
----------------------------------------------------
'''


class TestAdminProfileOverview(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.user_admin = Admin.objects.create(username='Micheal_Johnson', password="password3", first_name="Micheal",
                                               last_name='Johnson',
                                               phone_number='4149824444', home_address='2264 N Bradford Ave',
                                               user_type='Admin',
                                               email='michealJohnson@aol.com')

    def test_MyProfileView_to_Edit_My_Information(self):

        r = self.client.post('/', {'username': 'Micheal_Johnson', 'password': 'password3'})
        self.assertTrue(r.context is None)

        try:
            self.assertTrue(r.url, "MyProfileOverview")
        except AssertionError as msg:
            print(msg)

        r = self.client.get("/EditMyInformation")

        try:
            self.assertTrue(r.url, "/EditMyInformation")
        except AssertionError as msg:
            print(msg)

    def test_MyProfileView_to_home(self):

        r = self.client.post('/', {'username': 'Micheal_Johnson', 'password': 'password3'})
        self.assertTrue(r.context is None)

        try:
            self.assertTrue(r.url, "MyProfileOverview")
        except AssertionError as msg:
            print(msg)

        r = self.client.get("/home")

        try:
            self.assertTrue(r.url, "/home")
        except AssertionError as msg:
            print(msg)

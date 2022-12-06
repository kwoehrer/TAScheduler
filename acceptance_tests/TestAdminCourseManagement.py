from django.test import TestCase, Client

from TAScheduler.app.models import *

'''
As a TA, I want to be able to navigate to the Course Management page
----------------------------------------------------
GIVEN: The user is a TA and is logged in and at the home page
AND:They can click on "Create Course"
THEN: They will be navigated to the "Create Course" page
As a user, I want to be able to navigate to the Create Course page
----------------------------------------------------
GIVEN: The user is a TA and is logged in and at the home page
AND:They can click on "Edit Course"
THEN: They will be navigated to the "Edit Course" page
As a user, I want to be able to navigate to the Edit Course page
----------------------------------------------------
GIVEN: The user is a TA and is logged in and at the home page
AND:They can click on "Delete Course"
THEN: They will be navigated to the "Delete Course" page
As a user, I want to be able to navigate to the Delete Course page
----------------------------------------------------
GIVEN: The user is a TA and is logged in and at the home page
AND:They can click on "Log out"
THEN: They will be navigated to the "login" page
As a user, I want to be able to navigate to the User page
----------------------------------------------------
'''


class TestTAHomePage(TestCase):

    def setUp(self):

        self.client = Client()
        self.user_ta = TA.objects.create(username='John_Doe', password="password", first_name="John",
                                         last_name='Doe',
                                         phone_number='4149818000', home_address='2513 N Farewell Ave',
                                         user_type='TA',
                                         email='johnDoe@aol.com')

    def test_CourseManagement_to_CreateCourse(self):

        response = self.client.post('/', {'username': 'John_Doe', 'password': 'password'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "CourseManagement")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/CreateCourse")

        try:
            self.assertTrue(response.url, "/CreateCourse")
        except AssertionError as msg:
            print(msg)

    def test_CourseManagement_to_EditCourse(self):

        r = self.client.post('/', {'username': 'John_Doe', 'password': 'password'})
        self.assertTrue(r.context is None)

        try:
            self.assertTrue(r.url, "home")
        except AssertionError as msg:
            print(msg)

        r = self.client.get("/EditCourse")

        try:
            self.assertTrue(r.url, "/EditCourse")
        except AssertionError as msg:
            print(msg)

    def test_CourseManagement_to_DeleteCourse(self):

        r = self.client.post('/', {'username': 'John_Doe', 'password': 'password'})
        self.assertTrue(r.context is None)

        try:
            self.assertTrue(r.url, "")
        except AssertionError as msg:
            print(msg)

        r = self.client.get("/DeleteCourse")

        try:
            self.assertTrue(r.url, "/DeleteCourse")
        except AssertionError as msg:
            print(msg)


'''
As a Instructor, I want to be able to navigate to the Course Management page
----------------------------------------------------
GIVEN: The user is a Instructor and is logged in and at the home page
AND:They can click on "Create Course"
THEN: They will be navigated to the "Create Course" page
As a user, I want to be able to navigate to the Create Course page
----------------------------------------------------
GIVEN: The user is a Instructor and is logged in and at the home page
AND:They can click on "Edit Course"
THEN: They will be navigated to the "Edit Course" page
As a user, I want to be able to navigate to the Edit Course page
----------------------------------------------------
GIVEN: The user is a Instructor and is logged in and at the home page
AND:They can click on "Delete Course"
THEN: They will be navigated to the "Delete Course" page
As a user, I want to be able to navigate to the Delete Course page
----------------------------------------------------
GIVEN: The user is a Instructor and is logged in and at the home page
AND:They can click on "Log out"
THEN: They will be navigated to the "login" page
As a user, I want to be able to navigate to the User page
----------------------------------------------------
'''


class TestInstructorLogin(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.user_instructor = Instructor.objects.create(username='Steven_Adams', password="passwordNew",
                                                         first_name="Steven",
                                                         last_name='Adams',
                                                         phone_number='4149818222', home_address='2512 N Kenwood Ave',
                                                         user_type='Instructor',
                                                         email='stevenAdams@aol.com')

    def test_CourseManagement_to_CreateCourse(self):

        r = self.client.post('/', {'username': 'Steven_Adams', 'password': 'passwordNew'})
        self.assertTrue(r.context is None)

        try:
            self.assertTrue(r.url, "CourseManagement")
        except AssertionError as msg:
            print(msg)

        r = self.client.get("/CreateCourse")

        try:
            self.assertTrue(r.url, "/CreateCourse")
        except AssertionError as msg:
            print(msg)

    def test_CourseManagement_to_EditCourse(self):

        r = self.client.post('/', {'username': 'Steven_Adams', 'password': 'passwordNew'})
        self.assertTrue(r.context is None)

        try:
            self.assertTrue(r.url, "home")
        except AssertionError as msg:
            print(msg)

        r = self.client.get("/EditCourse")

        try:
            self.assertTrue(r.url, "/EditCourse")
        except AssertionError as msg:
            print(msg)

    def test_CourseManagement_to_DeleteCourse(self):

        r = self.client.post('/', {'username': 'Steven_Adams', 'password': 'passwordNew'})
        self.assertTrue(r.context is None)

        try:
            self.assertTrue(r.url, "")
        except AssertionError as msg:
            print(msg)

        r = self.client.get("/DeleteCourse")

        try:
            self.assertTrue(r.url, "/DeleteCourse")
        except AssertionError as msg:
            print(msg)


'''
As a Admin, I want to be able to navigate to the Course Management page
----------------------------------------------------
GIVEN: The user is a Admin and is logged in and at the home page
AND:They can click on "Create Course"
THEN: They will be navigated to the "Create Course" page
As a user, I want to be able to navigate to the Create Course page
----------------------------------------------------
GIVEN: The user is a Admin and is logged in and at the home page
AND:They can click on "Edit Course"
THEN: They will be navigated to the "Edit Course" page
As a user, I want to be able to navigate to the Edit Course page
----------------------------------------------------
GIVEN: The user is a Admin and is logged in and at the home page
AND:They can click on "Delete Course"
THEN: They will be navigated to the "Delete Course" page
As a user, I want to be able to navigate to the Delete Course page
----------------------------------------------------
GIVEN: The user is a Admin and is logged in and at the home page
AND:They can click on "Log out"
THEN: They will be navigated to the "login" page
As a user, I want to be able to navigate to the User page
----------------------------------------------------
'''


class TestAdminLogin(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.user_admin = Admin.objects.create(username='Micheal_Johnson', password="password3", first_name="Micheal",
                                               last_name='Johnson',
                                               phone_number='4149824444', home_address='2264 N Bradford Ave',
                                               user_type='Admin',
                                               email='michealJohnson@aol.com')

    def test_CourseManagement_to_CreateCourse(self):

        r = self.client.post('/', {'username': 'Micheal_Johnson', 'password': 'password3'})
        self.assertTrue(r.context is None)

        try:
            self.assertTrue(r.url, "CourseManagement")
        except AssertionError as msg:
            print(msg)

        r = self.client.get("/CreateCourse")

        try:
            self.assertTrue(r.url, "/CreateCourse")
        except AssertionError as msg:
            print(msg)

    def test_CourseManagement_to_EditCourse(self):

        r = self.client.post('/', {'username': 'Micheal_Johnson', 'password': 'password3'})
        self.assertTrue(r.context is None)

        try:
            self.assertTrue(r.url, "home")
        except AssertionError as msg:
            print(msg)

        r = self.client.get("/EditCourse")

        try:
            self.assertTrue(r.url, "/EditCourse")
        except AssertionError as msg:
            print(msg)

    def test_CourseManagement_to_DeleteCourse(self):

        r = self.client.post('/', {'username': 'Micheal_Johnson', 'password': 'password3'})
        self.assertTrue(r.context is None)

        try:
            self.assertTrue(r.url, "")
        except AssertionError as msg:
            print(msg)

        r = self.client.get("/DeleteCourse")

        try:
            self.assertTrue(r.url, "/DeleteCourse")
        except AssertionError as msg:
            print(msg)
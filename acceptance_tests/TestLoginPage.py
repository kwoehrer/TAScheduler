from django.test import TestCase, Client

from app.models import *
from classes.Users.users import AdminUser, TAUser, InstructorUser

'''
Scenario: As a TA, I want to be able to navigate to the Login Page
-------------------------------------------------------------
Acceptance Criteria 1:
GIVEN user is a TA and has a existing account in database
WHEN a valid username is entered
AND a valid password is entered
THEN account is accessed
-------------------------------------------------------------
Acceptance Criteria 2:
GIVEN user is a TA and has a existing account in database
WHEN an invalid username is entered
AND a valid password is entered
THEN account is not accessed
-------------------------------------------------------------
Acceptance Criteria 3:
GIVEN user is a TA has existing account in database
WHEN a valid username is entered
AND an invalid password is entered
THEN account is not accessed
-------------------------------------------------------------
Acceptance Criteria 4:
GIVEN user is a TA has existing account in database
WHEN a valid username entered
AND an empty password is entered
THEN account is not accessed
-------------------------------------------------------------
Acceptance Criteria 5:
GIVEN user is a TA has existing account in database
WHEN a valid password entered
AND an empty username is entered
THEN account is not accessed
-------------------------------------------------------------
Acceptance Criteria 6:
GIVEN user is a TA has existing account in database
WHEN an invalid username entered
AND an invalid password is entered
THEN account is not accessed
-------------------------------------------------------------
Acceptance Criteria 7:
GIVEN user is a TA has existing account in database
WHEN an empty username entered
AND an empty password is entered
THEN account is not accessed
-------------------------------------------------------------
'''


class TestTALogin(TestCase):

    def setUp(self):

        self.client = Client()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave',
                            user_type='TA',
                            email='johnDoe@aol.com')

        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.ta: TAUser = TAUser(user_model)
        user_model.save()

    # Successful login test
    def testSuccessfulLogin(self):

        response = self.client.post('/', {'username': 'John_Doe', 'password': 'password'})
        try:
            self.assertTrue(response.context is None)
        except AssertionError as msg:
            print(msg)
        pass

    # Incorrect Username test
    def testLoginIncorrectUserName(self):

        response = self.client.post('/', {'username': 'Steven_Adams', 'password': 'password'}, follow=True)
        try:
            self.assertTrue(response.context["message"], "Incorrect Username")
        except AssertionError as msg:
            print(msg)

        pass

    # Incorrect Password test
    def testLoginIncorrectPassword(self):

        response = self.client.post('/', {'username': 'John_Doe', 'password': 'password1'}, follow=True)
        try:
            self.assertTrue(response.context["message"], "Invalid Username or Password")
        except AssertionError as msg:
            print(msg)

        pass

    # Empty Username test
    def testLoginEmptyUsername(self):

        response = self.client.post('/', {'username': ' ', 'password': 'password'}, follow=True)
        try:
            self.assertTrue(response.context["message"], "Invalid Username or Password")
        except AssertionError as msg:
            print(msg)

    # Empty Password test
    def testLoginEmptyPassword(self):

        response = self.client.post('/', {'username': 'John_Doe', 'password': ' '}, follow=True)
        try:
            self.assertTrue(response.context["message"], "Invalid Username or Password")
        except AssertionError as msg:
            print(msg)

    # Incorrect Username and Password test
    def testLoginIncorrectUserAndPass(self):

        response = self.client.post('/', {'username': 'testAdmin', 'password': 'testAdmin1'})
        try:
            self.assertTrue(response.context["message"], "Invalid Username or Password")
            self.assertTrue(response.context["message"], "Invalid Username or Password")
        except AssertionError as msg:
            print(msg)

    # Empty Username and Password test
    def testLoginEmptyUsernameAndPassword(self):

        response = self.client.post('/', {'username': ' ', 'password': ' '})
        try:
            self.assertTrue(response.context["message"], "Invalid Username or Password")
            self.assertTrue(response.context["message"], "Invalid Username or Password")
        except AssertionError as msg:
            print(msg)


'''
Scenario: As an Instructor, I want to be able to navigate to the Login Page
-------------------------------------------------------------
Acceptance Criteria 1:
GIVEN user is an Instructor and has a existing account in database
WHEN a valid username is entered
AND a valid password is entered
THEN account is accessed
-------------------------------------------------------------
Acceptance Criteria 2:
GIVEN user is an Instructor and has a existing account in database
WHEN an invalid username is entered
AND a valid password is entered
THEN account is not accessed
-------------------------------------------------------------
Acceptance Criteria 3:
GIVEN user is an Instructor has existing account in database
WHEN a valid username is entered
AND an invalid password is entered
THEN account is not accessed
-------------------------------------------------------------
Acceptance Criteria 4:
GIVEN user is an Instructor has existing account in database
WHEN a valid username entered
AND an empty password is entered
THEN account is not accessed
-------------------------------------------------------------
Acceptance Criteria 5:
GIVEN user is an Instructor has existing account in database
WHEN a valid password entered
AND an empty username is entered
THEN account is not accessed
-------------------------------------------------------------
Acceptance Criteria 6:
GIVEN user is an Instructor has existing account in database
WHEN an invalid username entered
AND an invalid password is entered
THEN account is not accessed
-------------------------------------------------------------
Acceptance Criteria 7:
GIVEN user is an Instructor has existing account in database
WHEN an empty username entered
AND an empty password is entered
THEN account is not accessed
-------------------------------------------------------------
'''


class TestInstructorLogin(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        User.objects.create(username='Steven_Adams', password="passwordNew",
                            first_name="Steven",
                            last_name='Adams',
                            phone_number='4149818222', home_address='2512 N Kenwood Ave',
                            user_type='Instructor',
                            email='stevenAdams@aol.com')
        user_object = User.objects.filter(username='Steven_Adams')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.instructor: InstructorUser = InstructorUser(user_model)
        user_model.save()

    # Successful login test
    def testSuccessfulLogin(self):

        response = self.client.post('/', {'username': 'Steven_Adams', 'password': 'passwordNew'})
        try:
            self.assertTrue(response.context is None)
        except AssertionError as msg:
            print(msg)
        pass

    # Incorrect Username test
    def testLoginIncorrectUserName(self):

        response = self.client.post('/', {'username': 'Steven_Adams1', 'password': 'passwordNew'}, follow=True)
        try:
            self.assertTrue(response.context["message"], "Invalid Username or Password")
        except AssertionError as msg:
            print(msg)

        pass

    # Incorrect Password test
    def testLoginIncorrectPassword(self):

        response = self.client.post('/', {'username': 'Steven_Adams', 'password': 'password1'}, follow=True)
        try:
            self.assertTrue(response.context["message"], "Invalid Username or Password")
        except AssertionError as msg:
            print(msg)

        pass

    # Empty Username test
    def testLoginEmptyUsername(self):

        response = self.client.post('/', {'username': ' ', 'password': 'passwordNew'}, follow=True)
        try:
            self.assertTrue(response.context["message"], "Invalid Username or Password")
        except AssertionError as msg:
            print(msg)

    # Empty Password test
    def testLoginEmptyPassword(self):

        response = self.client.post('/', {'username': 'Steven_Adams', 'password': ' '}, follow=True)
        try:
            self.assertTrue(response.context["message"], "Invalid Username or Password")
        except AssertionError as msg:
            print(msg)

    # Incorrect Username and Password test
    def testLoginIncorrectUsernameAndPassword(self):

        response = self.client.post('/', {'username': 'testAdmin', 'password': 'testAdmin1'})
        try:
            self.assertTrue(response.context["message"], "Invalid Username or Password")
            self.assertTrue(response.context["message"], "Invalid Username or Password")
        except AssertionError as msg:
            print(msg)

    # Empty Username and Password test
    def testLoginEmptyUsernameAndPassword(self):

        response = self.client.post('/', {'username': ' ', 'password': ' '})
        try:
            self.assertTrue(response.context["message"], "Invalid Username or Password")
            self.assertTrue(response.context["message"], "Invalid Username or Password")
        except AssertionError as msg:
            print(msg)


'''
Scenario: As an Admin, I want to be able to navigate to the Login Page
-------------------------------------------------------------
Acceptance Criteria 1:
GIVEN user is an Admin and has a existing account in database
WHEN a valid username is entered
AND a valid password is entered
THEN account is accessed
-------------------------------------------------------------
Acceptance Criteria 2:
GIVEN user is an Admin and has a existing account in database
WHEN an invalid username is entered
AND a valid password is entered
THEN account is not accessed
-------------------------------------------------------------
Acceptance Criteria 3:
GIVEN user is an Admin has existing account in database
WHEN a valid username is entered
AND an invalid password is entered
THEN account is not accessed
-------------------------------------------------------------
Acceptance Criteria 4:
GIVEN user is an Admin has existing account in database
WHEN a valid username entered
AND an empty password is entered
THEN account is not accessed
-------------------------------------------------------------
Acceptance Criteria 5:
GIVEN user is an Admin has existing account in database
WHEN a valid password entered
AND an empty username is entered
THEN account is not accessed
-------------------------------------------------------------
Acceptance Criteria 6:
GIVEN user is an Admin has existing account in database
WHEN an invalid username entered
AND an invalid password is entered
THEN account is not accessed
-------------------------------------------------------------
Acceptance Criteria 7:
GIVEN user is an Admin has existing account in database
WHEN an empty username entered
AND an empty password is entered
THEN account is not accessed
-------------------------------------------------------------
'''


class TestAdminLogin(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        User.objects.create(username='Micheal_Johnson', password="password3", first_name="Micheal",
                            last_name='Johnson',
                            phone_number='4149824444', home_address='2264 N Bradford Ave',
                            user_type='Admin',
                            email='michealJohnson@aol.com')

        user_object = User.objects.filter(username='Micheal_Johnson')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.admin: AdminUser = AdminUser(user_model)
        user_model.save()

    # Successful login test
    def testSuccessfulLogin(self):

        response = self.client.post('/', {'username': 'Micheal_Johnson', 'password': 'password3'})
        try:
            self.assertTrue(response.context is None)
        except AssertionError as msg:
            print(msg)
        pass

    # Incorrect Username test
    def testLoginIncorrectUserName(self):

        response = self.client.post('/', {'username': 'Steven_Adams1', 'password': 'password3'}, follow=True)
        try:
            self.assertTrue(response.context["message"], "Invalid Username or Password")
        except AssertionError as msg:
            print(msg)

        pass

    # Incorrect Password test
    def testLoginIncorrectPassword(self):

        response = self.client.post('/', {'username': 'Micheal_Johnson', 'password': 'password1'}, follow=True)
        try:
            self.assertTrue(response.context["message"], "Invalid Username or Password")
        except AssertionError as msg:
            print(msg)

        pass

    # Empty Username test
    def testLoginEmptyUsername(self):

        response = self.client.post('/', {'username': ' ', 'password': 'password3'}, follow=True)
        try:
            self.assertTrue(response.context["message"], "Invalid Username or Password")
        except AssertionError as msg:
            print(msg)

    # Empty Password test
    def testLoginEmptyPassword(self):

        response = self.client.post('/', {'username': 'Micheal_Johnson', 'password': ' '}, follow=True)
        try:
            self.assertTrue(response.context["message"], "Invalid Username or Password")
        except AssertionError as msg:
            print(msg)

    # Incorrect Username and Password test
    def testLoginIncorrectUsernameAndPassword(self):

        response = self.client.post('/', {'username': 'testAdmin', 'password': 'testAdmin1'})
        try:
            self.assertTrue(response.context["message"], "Invalid Username or Password")
            self.assertTrue(response.context["message"], "Invalid Username or Password")
        except AssertionError as msg:
            print(msg)

    # Empty Username and Password test
    def testLoginEmptyUsernameAndPassword(self):

        response = self.client.post('/', {'username': ' ', 'password': ' '})
        try:
            self.assertTrue(response.context["message"], "Invalid Username or Password")
            self.assertTrue(response.context["message"], "Invalid Username or Password")
        except AssertionError as msg:
            print(msg)

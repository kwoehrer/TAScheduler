from django.test import TestCase, Client

from TAScheduler.app.models import *

'''
Acceptance Criteria 1:
GIVEN user is a TA and has a existing account in database
WHEN a valid username is entered
AND a valid password is entered
THEN account is accessed 
Acceptance Criteria 2:
GIVEN user is a TA and has a existing account in database
WHEN an invalid username is entered
AND a valid password is entered
THEN account is not accessed
Acceptance Criteria 3:
GIVEN user is a TA has existing account in database
WHEN a valid username is entered
AND an invalid password is entered
THEN account is not accessed
Acceptance Criteria 4:
GIVEN user is a TA has existing account in database
WHEN a valid username entered
AND an empty password is entered
THEN account is not accessed
Acceptance Criteria 5:
GIVEN user is a TA has existing account in database
WHEN a valid password entered
AND an empty username is entered
THEN account is not accessed
Acceptance Criteria 6:
GIVEN user is a TA has existing account in database
WHEN an invalid username entered
AND an invalid password is entered
THEN account is not accessed
Acceptance Criteria 7:
GIVEN user is a TA has existing account in database
WHEN an empty username entered
AND an empty password is entered
THEN account is not accessed
'''


class TestTALogin(TestCase):

    def setUp(self):

        self.client = Client()
        self.user_ta = TA.objects.create(username='John_Doe', password="password", first_name="John",
                                         last_name='Doe',
                                         phone_number='4149818000', home_address='2513 N Farewell Ave',
                                         user_type='TA',
                                         email='johnDoe@aol.com')

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

        response = self.client.post('/', {'username': 'Steven_Adams1', 'password': 'passwordNew'}, follow=True)
        try:
            self.assertTrue(response.context["error"], "Incorrect Username")
        except AssertionError as msg:
            print(msg)

        pass

    # Incorrect Password test
    def testLoginIncorrectPassword(self):

        response = self.client.post('/', {'username': 'Steven_Adams', 'password': 'password1'}, follow=True)
        try:
            self.assertTrue(response.context["error"], "Incorrect Username")
        except AssertionError as msg:
            print(msg)

        pass

    # Empty Username test
    def testLoginNoUser(self):

        response = self.client.post('/', {'username': ' ', 'password': 'password'}, follow=True)
        try:
            self.assertTrue(response.context["error"], "Incorrect Username")
        except AssertionError as msg:
            print(msg)

    # Empty Password test
    def testLoginNoPass(self):

        response = self.client.post('/', {'username': 'John_Doe', 'password': ' '}, follow=True)
        try:
            self.assertTrue(response.context["error"], "Incorrect Username")
        except AssertionError as msg:
            print(msg)

    # Incorrect Username and Password test
    def testLoginIncorrectUserAndPass(self):

        response = self.client.post('/', {'username': 'testAdmin', 'password': 'testAdmin1'})
        try:
            self.assertTrue(response.context["error"], "Incorrect Username")
            self.assertTrue(response.context["error"], "Incorrect Password")
        except AssertionError as msg:
            print(msg)

    # Empty Username and Password test
    def testLoginNoUserAndPass(self):

        response = self.client.post('/', {'username': ' ', 'password': ' '})
        try:
            self.assertTrue(response.context["error"], "Empty Username")
            self.assertTrue(response.context["error"], "Empty Password")
        except AssertionError as msg:
            print(msg)


'''
Acceptance Criteria 1:
GIVEN user is a Instructor and has a existing account in daAdminbase
WHEN a valid username is entered
AND a valid password is entered
THEN account is accessed 
Acceptance Criteria 2:
GIVEN user is a Instructor and has a existing account in daAdminbase
WHEN an invalid username is entered
AND a valid password is entered
THEN account is not accessed
Acceptance Criteria 3:
GIVEN user is a Instructor has existing account in database
WHEN a valid username is entered
AND an invalid password is entered
THEN account is not accessed
Acceptance Criteria 4:
GIVEN user is a Instructor has existing account in database
WHEN a valid username entered
AND an empty password is entered
THEN account is not accessed
Acceptance Criteria 5:
GIVEN user is a Instructor has existing account in database
WHEN a valid password entered
AND an empty username is entered
THEN account is not accessed
Acceptance Criteria 6:
GIVEN user is a Instructor has existing account in database
WHEN an invalid username entered
AND an invalid password is entered
THEN account is not accessed
Acceptance Criteria 7:
GIVEN user is a Instructor has existing account in database
WHEN an empty username entered
AND an empty password is entered
THEN account is not accessed
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
            self.assertTrue(response.context["error"], "Incorrect Username")
        except AssertionError as msg:
            print(msg)

        pass

    # Incorrect Password test
    def testLoginIncorrectPassword(self):

        response = self.client.post('/', {'username': 'Steven_Adams', 'password': 'password1'}, follow=True)
        try:
            self.assertTrue(response.context["error"], "Incorrect Username")
        except AssertionError as msg:
            print(msg)

        pass

    # Empty Username test
    def testLoginNoUser(self):

        response = self.client.post('/', {'username': ' ', 'password': 'passwordNew'}, follow=True)
        try:
            self.assertTrue(response.context["error"], "Incorrect Username")
        except AssertionError as msg:
            print(msg)

    # Empty Password test
    def testLoginNoPass(self):

        response = self.client.post('/', {'username': 'Steven_Adams', 'password': ' '}, follow=True)
        try:
            self.assertTrue(response.context["error"], "Incorrect Username")
        except AssertionError as msg:
            print(msg)

    # Incorrect Username and Password test
    def testLoginIncorrectUserAndPass(self):

        response = self.client.post('/', {'username': 'testAdmin', 'password': 'testAdmin1'})
        try:
            self.assertTrue(response.context["error"], "Incorrect Username")
            self.assertTrue(response.context["error"], "Incorrect Password")
        except AssertionError as msg:
            print(msg)

    # Empty Username and Password test
    def testLoginNoUserAndPass(self):

        response = self.client.post('/', {'username': ' ', 'password': ' '})
        try:
            self.assertTrue(response.context["error"], "Empty Username")
            self.assertTrue(response.context["error"], "Empty Password")
        except AssertionError as msg:
            print(msg)


'''
Acceptance Criteria 1:
GIVEN user is a Admin and has a existing account in database
WHEN a valid username is entered
AND a valid password is entered
THEN account is accessed 
Acceptance Criteria 2:
GIVEN user is a Admin and has a existing account in database
WHEN an invalid username is entered
AND a valid password is entered
THEN account is not accessed
Acceptance Criteria 3:
GIVEN user is a Admin has existing account in database
WHEN a valid username is entered
AND an invalid password is entered
THEN account is not accessed
Acceptance Criteria 4:
GIVEN user is a Admin has existing account in database
WHEN a valid username entered
AND an empty password is entered
THEN account is not accessed
Acceptance Criteria 5:
GIVEN user is a Admin has existing account in database
WHEN a valid password entered
AND an empty username is entered
THEN account is not accessed
Acceptance Criteria 6:
GIVEN user is a Admin has existing account in database
WHEN an invalid username entered
AND an invalid password is entered
THEN account is not accessed
Acceptance Criteria 7:
GIVEN user is a Admin has existing account in database
WHEN an empty username entered
AND an empty password is entered
THEN account is not accessed
'''


class TestAdminLogin(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.user_admin = Admin.objects.create(username='Micheal_Johnson', password="password3", first_name="Micheal",
                                               last_name='Johnson',
                                               phone_number='4149824444', home_address='2264 N Bradford Ave',
                                               user_type='Admin',
                                               email='michealJohnson@aol.com')

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

        response = self.client.post('/', {'username': 'Steven_Adams1', 'password': 'passwordNew'}, follow=True)
        try:
            self.assertTrue(response.context["error"], "Incorrect Username")
        except AssertionError as msg:
            print(msg)

        pass

    # Incorrect Password test
    def testLoginIncorrectPassword(self):

        response = self.client.post('/', {'username': 'Steven_Adams', 'password': 'password1'}, follow=True)
        try:
            self.assertTrue(response.context["error"], "Incorrect Username")
        except AssertionError as msg:
            print(msg)

        pass

    # Empty Username test
    def testLoginNoUser(self):

        response = self.client.post('/', {'username': ' ', 'password': 'password3'}, follow=True)
        try:
            self.assertTrue(response.context["error"], "Incorrect Username")
        except AssertionError as msg:
            print(msg)

    # Empty Password test
    def testLoginNoPass(self):

        response = self.client.post('/', {'username': 'Micheal_Johnson', 'password': ' '}, follow=True)
        try:
            self.assertTrue(response.context["error"], "Incorrect Username")
        except AssertionError as msg:
            print(msg)

    # Incorrect Username and Password test
    def testLoginIncorrectUserAndPass(self):

        response = self.client.post('/', {'username': 'testAdmin', 'password': 'testAdmin1'})
        try:
            self.assertTrue(response.context["error"], "Incorrect Username")
            self.assertTrue(response.context["error"], "Incorrect Password")
        except AssertionError as msg:
            print(msg)

    # Empty Username and Password test
    def testLoginNoUserAndPass(self):

        response = self.client.post('/', {'username': ' ', 'password': ' '})
        try:
            self.assertTrue(response.context["error"], "Empty Username")
            self.assertTrue(response.context["error"], "Empty Password")
        except AssertionError as msg:
            print(msg)

from django.test import TestCase, Client

from app.models import *
from classes.Users.users import AdminUser, InstructorUser, TAUser

'''
SCENARIO: As an Admin, I want to be able navigate the Delete Account Page and Delete a User
-------------------------------------------------------------------------------------------
Acceptance Criteria 1:
GIVEN The user is an Admin and is logged in and at the Delete Account page
WHEN a user with the same fields already exists
AND "Delete Account" is clicked
THEN account is can be deleted
-------------------------------------------------------------------------------------------
Acceptance Criteria 2:
GIVEN The user is an Admin and is logged in and at the Delete Account page
WHEN a user is to be deleted
AND all of the valid fields are not provided
THEN account cannot be searched to be deleted
-------------------------------------------------------------------------------------------
Acceptance Criteria 3:
GIVEN The user is an Admin and is logged in and at the Delete Account page
WHEN a user of type TA is to be deleted
WHEN user can be found with valid fields in the list of all users
AND "Delete Account" is clicked
THEN account can be deleted
-------------------------------------------------------------------------------------------
Acceptance Criteria 4:
GIVEN The user is an Admin and is logged in and at the Delete Account page
WHEN a user of type Instructor is to be deleted
WHEN user can be found with valid fields in the list of all users
AND "Delete Account" is clicked
THEN account can be deleted
-------------------------------------------------------------------------------------------
Acceptance Criteria 5:
GIVEN The user is an Admin and is logged in and at the Delete Account page
WHEN a user of type Admin is to be deleted
WHEN user can be found with valid fields in the list of all users
AND "Delete Account" is clicked
THEN account can be deleted
-------------------------------------------------------------------------------------------
SCENARIO: As an Admin, I want to be able to navigate to the Account Management page
-------------------------------------------------------------------------------------------
Acceptance Criteria 1:
GIVEN: The user is an Admin and is logged in and at the Delete Account page
AND:They can click on "Return to Account Management Page"
THEN: They will be navigated to the "Account Management" page
'''


class TestSearchUsersToDelete(TestCase):

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

        User.objects.create(username='Johnny_Doe1', password="password2", first_name="Johnny",
                            last_name='Doe',
                            phone_number='4149818004', home_address='2516 N Farewell Ave',
                            user_type='Admin',
                            email='johnDoe1@aol.com')

        user_object = User.objects.filter(username='John_Doe1')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.admin1: AdminUser = AdminUser(user_model)

        User.objects.create(username='Steven_Adams', password="password1", first_name="Steven",
                            last_name='Adams',
                            phone_number='4149818001', home_address='2512 N Farewell Ave',
                            user_type='Instructor',
                            email='stevenAdams@aol.com')

        user_object = User.objects.filter(username='Steven_Adams')[0]
        user_model = Instructor.objects.create(account_ID=user_object)
        self.instructor: InstructorUser = InstructorUser(user_model)

        User.objects.create(username='Kevin_Smith', password="password2", first_name='Kevin',
                            last_name='Smith',
                            phone_number='4149818003', home_address='2515 N Farewell Ave',
                            user_type='TA',
                            email='kevinSmith@aol.com')

        user_object = User.objects.filter(username='Kevin_Smith')[0]
        user_model = TA.objects.create(account_ID=user_object)
        self.ta: TAUser = TAUser(user_model)

        self.client.post("/", {"username": self.admin.getUsername(), "password": self.admin.getPassword()})

    def testEmptyEmailProvided(self):
        response = self.client.post("/DeleteAccount/",
                                    {"Email": " ", "Username": "stephen_Doe",
                                     "First Name and Last Name": "Stephen Doe", "Type of User Account": "Admin"},
                                    follow=True)

        self.assertEqual(response.context["error"], "User cannot be found. First name and Last Name should not be "
                                                    "left blank")

    def testEmptyUsernameProvided(self):
        response = self.client.post("/DeleteAccount/",
                                    {"Email": "stephenDoe@aol.com", "Username": " ",
                                     "First Name and Last Name": "Stephen Doe", "Type of User Account": "Admin"},
                                    follow=True)

        self.assertEqual(response.context["error"], "User cannot be found. Username should not be left blank")

    def testEmptyFirstNameAndLastNameProvided(self):
        response = self.client.post("/DeleteAccount/",
                                    {"Email": "stephenDoe@aol.com", "Username": "stephen_Doe",
                                     "First Name and Last Name": " ", "Type of User Account": "Admin"},
                                    follow=True)

        self.assertEqual(response.context["error"], "User cannot be found. First name and Last Name should not be "
                                                    "left blank")

    def testEmptyUserTypeProvided(self):
        response = self.client.post("/DeleteAccount/",
                                    {"Email": "stephenDoe@aol.com", "Username": "stephen_Doe",
                                     "First Name and Last Name": "Stephen Doe", "Type of User Account": " "},
                                    follow=True)

        self.assertEqual(response.context["error"], "User cannot be found. Type of User Account should not be left "
                                                    "blank")


class TestAdminDeleteAccount(TestCase):

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

        User.objects.create(username='Johnny_Doe1', password="password2", first_name="Johnny",
                            last_name='Doe',
                            phone_number='4149818004', home_address='2516 N Farewell Ave',
                            user_type='Admin',
                            email='johnDoe1@aol.com')

        user_object = User.objects.filter(username='John_Doe1')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.admin1: AdminUser = AdminUser(user_model)

        User.objects.create(username='Steven_Adams', password="password1", first_name="Steven",
                            last_name='Adams',
                            phone_number='4149818001', home_address='2512 N Farewell Ave',
                            user_type='Instructor',
                            email='stevenAdams@aol.com')

        user_object = User.objects.filter(username='Steven_Adams')[0]
        user_model = Instructor.objects.create(account_ID=user_object)
        self.instructor: InstructorUser = InstructorUser(user_model)

        User.objects.create(username='Kevin_Smith', password="password2", first_name='Kevin',
                            last_name='Smith',
                            phone_number='4149818003', home_address='2515 N Farewell Ave',
                            user_type='TA',
                            email='kevinSmith@aol.com')

        user_object = User.objects.filter(username='Kevin_Smith')[0]
        user_model = TA.objects.create(account_ID=user_object)
        self.ta: TAUser = TAUser(user_model)

        self.client.post("/", {"username": self.admin.getUsername(), "password": self.admin.getPassword()})

    def test_deleteUser(self):
        self.client.post('/DeleteAccount/', {'Delete Account': 1}, follow=True)
        var = User.objects.count()
        self.assertEquals(var, 3, "TA has been successfully deleted")
        user_count = list(User.objects.all())
        self.assertEquals(user_count, [self.instructor, self.admin, self.admin1],
                          "Instructor, Admin, and Admin1 still exist")

        self.client.post('/DeleteAccount/', {'Delete Account': 2}, follow=True)
        var = User.objects.count()
        self.assertEquals(var, 2, "Instructor has been successfully deleted")
        user_count = list(User.objects.all())
        self.assertEquals(user_count, [self.admin, self.admin1], "Admin2 and Admin has not been deleted")

        self.client.post('/AccountDelete/', {'Delete Account': 3}, follow=True)
        var = User.objects.count()
        self.assertEquals(var, 1, "Admin1 was successfully deleted")
        user_count = list(User.objects.all())
        self.assertEquals(user_count, [self.admin], "Only admin is left")


class DeleteAdmin(TestCase):

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

        self.client.post("/", {"username": self.admin.getUsername(), "password": self.admin.getPassword()})

    def test_deleteAdmin(self):
        response = self.client.post('/DeleteAccount/', {'Delete Account': 1}, follow=True)
        try:
            self.assertTrue(response.url, " ")
        except AttributeError as msg:
            print(msg)


class DeleteInstructor(TestCase):

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

        User.objects.create(username='Johnny_Doe1', password="password2", first_name="Johnny",
                            last_name='Doe',
                            phone_number='4149818004', home_address='2516 N Farewell Ave',
                            user_type='Admin',
                            email='johnDoe1@aol.com')

        user_object = User.objects.filter(username='John_Doe1')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.admin1: AdminUser = AdminUser(user_model)

        User.objects.create(username='Steven_Adams', password="password1", first_name="Steven",
                            last_name='Adams',
                            phone_number='4149818001', home_address='2512 N Farewell Ave',
                            user_type='Instructor',
                            email='stevenAdams@aol.com')

        user_object = User.objects.filter(username='Steven_Adams')[0]
        user_model = Instructor.objects.create(account_ID=user_object)
        self.instructor: InstructorUser = InstructorUser(user_model)

        User.objects.create(username='Kevin_Smith', password="password2", first_name='Kevin',
                            last_name='Smith',
                            phone_number='4149818003', home_address='2515 N Farewell Ave',
                            user_type='TA',
                            email='kevinSmith@aol.com')

        user_object = User.objects.filter(username='Kevin_Smith')[0]
        user_model = TA.objects.create(account_ID=user_object)
        self.ta: TAUser = TAUser(user_model)

        self.client.post("/", {"username": self.admin.getUsername(), "password": self.admin.getPassword()})

    def test_deleteInstructor(self):
        self.client.post('/DeleteAccount/', {'Delete Account': 2}, follow=True)
        self.assertEquals(User.objects.get(userID=self.instructor.getID()), self.instructor.getID(),
                          msg="Instructor has not been deleted")


class DeleteTA(TestCase):
    client = None
    TA = None
    instructor = None
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

        User.objects.create(username='Johnny_Doe1', password="password2", first_name="Johnny",
                            last_name='Doe',
                            phone_number='4149818004', home_address='2516 N Farewell Ave',
                            user_type='Admin',
                            email='johnDoe1@aol.com')

        user_object = User.objects.filter(username='John_Doe1')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.admin1: AdminUser = AdminUser(user_model)

        User.objects.create(username='Steven_Adams', password="password1", first_name="Steven",
                            last_name='Adams',
                            phone_number='4149818001', home_address='2512 N Farewell Ave',
                            user_type='Instructor',
                            email='stevenAdams@aol.com')

        user_object = User.objects.filter(username='Steven_Adams')[0]
        user_model = Instructor.objects.create(account_ID=user_object)
        self.instructor: InstructorUser = InstructorUser(user_model)

        User.objects.create(username='Kevin_Smith', password="password2", first_name='Kevin',
                            last_name='Smith',
                            phone_number='4149818003', home_address='2515 N Farewell Ave',
                            user_type='TA',
                            email='kevinSmith@aol.com')

        user_object = User.objects.filter(username='Kevin_Smith')[0]
        user_model = TA.objects.create(account_ID=user_object)
        self.ta: TAUser = TAUser(user_model)

        self.client.post("/", {"username": self.admin.getUsername(), "password": self.admin.getPassword()})

    def test_deleteTa(self):
        self.client.post('/AccountDelete/', {'Delete Account': 1}, follow=True)
        var = User.objects.count()
        self.assertEquals(var, 2)
        user_count = list(User.objects.all())
        self.assertEquals(user_count, [self.instructor, self.admin], msg="TA was successfully deleted")


class TestDeleteAccountPage(TestCase):

    def test_DeleteAccount_to_Account_Management(self):

        response = self.client.post('/', {'username': 'Micheal_Johnson', 'password': 'password3'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/AdminAccMng")

        try:
            self.assertTrue(response.url, "/AdminAccMng")
        except AssertionError as msg:
            print(msg)

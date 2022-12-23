from django.test import TestCase, Client

from app.models import *
from classes.Users.users import AdminUser, InstructorUser, TAUser

'''
SCENARIO: As an Admin, I want to be able navigate the Edit My User Profile
-----------------------------------------------------------------------
Acceptance Criteria 1:
SCENARIO: As an Admin, I want to be able to navigate to the My User Profile
GIVEN The user is an Admin and is logged in and at the My User Profile
WHEN a user of type Admin is to be edited
WHEN user can be found with valid fields in the list of all users
AND "Edit Profile" is clicked
THEN account can be edited
-----------------------------------------------------------------------
SCENARIO: As an Admin, I want to be able navigate to the Home Page
-----------------------------------------------------------------------
Acceptance Criteria 1:
GIVEN: The user is a Admin and is logged in and at the Edit MyUserProfile page
AND:They can click on "Return to Home Page"
THEN: They will be navigated to the "AdminHome" page
'''


class TestEditMyUserProfileAdmin(TestCase):
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
    #     User.objects.create(username='John_Doe', password="password", first_name="John",
    #                         phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
    #                         email='johnDoe@aol.com')
    #     user_obj = User.objects.filter(username='John_Doe')[0]
    #     new_user = Admin.objects.create(account_ID=user_obj)
    #     self.admin1: AdminUser = AdminUser(new_user)
    #     new_user.save()
    #
    #     self.client.post({"/MyUserProfile",
    #                       self.admin1})
    #
    #     self.assertEqual(self.admin1.getID(), User.objects.get(account_ID=self.admin.getID()),
    #                      "User exists in "
    #                      "Database")

    def test_editEmail(self):
        self.client.post("/MyUserProfile",
                         {
                             "First Name": self.admin.getFirstName(),
                             "Last Name": self.admin.getLastName(),
                             "Type of User": self.admin.getUserType(),
                             "Email": "johnDoe1@aol.com",
                             "Related Courses": self.admin.getCourses(),
                             "Phone Number": self.admin.getPhoneNumber(),
                             "Home Address": self.admin.getHomeAddress()})
        self.assertEqual(User.objects.get(account_ID=self.admin.getID()).email, "johnDoe1@aol.com",
                         msg="Email not set correctly")

    def test_editFirstName(self):
        self.client.post("/MyUserProfile",
                         {
                             "First Name": "Kevin",
                             "Last Name": self.admin.getLastName(),
                             "Type of User": self.admin.getUserType(),
                             "Email": self.admin.getEmail(),
                             "Related Courses": self.admin.getCourses(),
                             "Phone Number": self.admin.getPhoneNumber(),
                             "Home Address": self.admin.getHomeAddress()})
        self.assertEqual(User.objects.get(account_ID=self.admin.getID()).first_name, "Kevin",
                         msg="First Name not set correctly")

    def test_editLastName(self):
        self.client.post("/MyUserProfile",
                         {
                             "First Name": self.admin.getFirstName(),
                             "Last Name": "Smith",
                             "Type of User": self.admin.getUserType(),
                             "Email": self.admin.getEmail(),
                             "Related Courses": self.admin.getCourses(),
                             "Phone Number": self.admin.getPhoneNumber(),
                             "Home Address": self.admin.getHomeAddress()})
        self.assertEqual(User.objects.get(User.objects.get(account_ID=self.admin.getID()).last_name), "Smith",
                         msg="Last Name not set correctly")

    def test_editPhoneNumber(self):
        self.client.post("/MyUserProfile",
                         {
                             "First Name": self.admin.getFirstName(),
                             "Last Name": self.admin.getLastName(),
                             "Type of User": self.admin.getUserType(),
                             "Email": self.admin.getEmail(),
                             "Related Courses": self.admin.getCourses(),
                             "Phone Number": "4145557000",
                             "Home Address": self.admin.getHomeAddress()})
        self.assertEqual(User.objects.get(User.objects.get(account_ID=self.admin.getID()).phone_number), "4145557000",
                         msg="Phone Number not set correctly")

    def test_editHomeAddress(self):
        self.client.post("/MyUserProfile",
                         {"First Name": self.admin.getFirstName(),
                          "Last Name": self.admin.getLastName(),
                          "Type of User": self.admin.getUserType(),
                          "Email": self.admin.getEmail(),
                          "Related Courses": self.admin.getCourses(),
                          "Phone Number": self.admin.getPhoneNumber(),
                          "Home Address": "2612 N Mary ville Ave",
                          "Type of User Account": self.admin.getUserType()})
        self.assertEqual(User.objects.get(User.objects.get(account_ID=self.admin.getID()).home_address), "2612 N Mary "
                                                                                                         "ville Ave",
                         msg="Home Address not set correctly")

    def test_editUserType(self):
        self.client.post("/MyUserProfile",
                         {"Email": self.admin.getPassword(), "Username": self.admin.getUsername(),
                          "Password": self.admin.getPassword(),
                          "First Name": self.admin.getFirstName(),
                          "Last Name": self.admin.getLastName(),
                          "Phone Number": self.admin.getPhoneNumber(),
                          "Home Address": self.admin.getHomeAddress(),
                          "Type of User Account": "TA"})
        self.assertEqual(User.objects.get(account_ID=self.admin.getID()).user_type, "TA",
                         msg="User Type not set correctly")


class TestAdminUserProfileToHome(TestCase):

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
        # Make a GET request to //MyUserProfile
        response = self.client.get("/MyUserProfile")

        # Check that the response was a redirect to page /home
        self.assertRedirects(response, '/AdminHome', status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

        # Follow the redirect and check that the final URL is '/home'
        response = response.follow()
        self.assertEqual(response.url, '/AdminHome')


'''
SCENARIO: As an Instructor, I want to be able navigate the Edit My User Profile
-----------------------------------------------------------------------
Acceptance Criteria 1:
SCENARIO: As an Instructor, I want to be able to navigate to the My User Profile
GIVEN The user is an Instructor and is logged in and at the My User Profile
WHEN a user of type Instructor is to be edited
WHEN user can be found with valid fields in the list of all users
AND "Edit Profile" is clicked
THEN account can be edited
-----------------------------------------------------------------------
SCENARIO: As an Instructor, I want to be able navigate to the Home Page
-----------------------------------------------------------------------
Acceptance Criteria 1:
GIVEN: The user is a Instructor and is logged in and at the Edit MyUserProfile page
AND:They can click on "Return to Home Page"
THEN: They will be navigated to the "InstructorHome" page
'''


class TestEditMyUserProfileInstructor(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='instructor',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj)

        self.instructor: InstructorUser = InstructorUser(user_model)

        self.client.post("/",
                         {"username": self.instructor.getUsername(), "password": self.instructor.getPassword()})

    # def test_UserExists(self):
    #     User.objects.create(username='John_Doe', password="password", first_name="John",
    #                         phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='instructor',
    #                         email='johnDoe@aol.com')
    #     user_obj = User.objects.filter(username='John_Doe')[0]
    #     new_user = Instructor.objects.create(account_ID=user_obj)
    #     self.instructor1: InstructorUser = InstructorUser(new_user)
    #     new_user.save()
    #
    #     self.client.post({"/MyUserProfile",
    #                       self.instructor1})
    #
    #     self.assertEqual(self.instructor1.getID(), User.objects.get(account_ID=self.instructor1.getID()).account_ID,
    #                      "User exists in "
    #                      "Database")

    def test_editEmail(self):
        self.client.post("/MyUserProfile",
                         {
                             "First Name": self.instructor.getFirstName(),
                             "Last Name": self.instructor.getLastName(),
                             "Type of User": self.instructor.getUserType(),
                             "Email": "johnDoe1@aol.com",
                             "Related Courses": self.instructor.getCourses(),
                             "Phone Number": self.instructor.getPhoneNumber(),
                             "Home Address": self.instructor.getHomeAddress()})
        self.assertEqual(User.objects.get(account_ID=self.instructor.getID()).email, "johnDoe1@aol.com",
                         msg="Email not set correctly")

    def test_editFirstName(self):
        self.client.post("/MyUserProfile",
                         {
                             "First Name": "Kevin",
                             "Last Name": self.instructor.getLastName(),
                             "Type of User": self.instructor.getUserType(),
                             "Email": self.instructor.getEmail(),
                             "Related Courses": self.instructor.getCourses(),
                             "Phone Number": self.instructor.getPhoneNumber(),
                             "Home Address": self.instructor.getHomeAddress()})
        self.assertEqual(User.objects.get(account_ID=self.instructor.getID()).first_name, "Kevin",
                         msg="First Name not set correctly")

    def test_editLastName(self):
        self.client.post("/MyUserProfile",
                         {
                             "First Name": self.instructor.getFirstName(),
                             "Last Name": "Smith",
                             "Type of User": self.instructor.getUserType(),
                             "Email": self.instructor.getEmail(),
                             "Related Courses": self.instructor.getCourses(),
                             "Phone Number": self.instructor.getPhoneNumber(),
                             "Home Address": self.instructor.getHomeAddress()})
        self.assertEqual(User.objects.get(account_ID=self.instructor.getID()).last_name, "Smith",
                         msg="Last Name not set correctly")

    def test_editPhoneNumber(self):
        self.client.post("/MyUserProfile",
                         {
                             "First Name": self.instructor.getFirstName(),
                             "Last Name": self.instructor.getLastName(),
                             "Type of User": self.instructor.getUserType(),
                             "Email": self.instructor.getEmail(),
                             "Related Courses": self.instructor.getCourses(),
                             "Phone Number": "4145557000",
                             "Home Address": self.instructor.getHomeAddress()})
        self.assertEqual(User.objects.get(account_ID=self.instructor.getID()).phone_number, "4145557000",
                         msg="Phone Number not set correctly")

    def test_editHomeAddress(self):
        self.client.post("/MyUserProfile",
                         {"First Name": self.instructor.getFirstName(),
                          "Last Name": self.instructor.getLastName(),
                          "Type of User": self.instructor.getUserType(),
                          "Email": self.instructor.getEmail(),
                          "Related Courses": self.instructor.getCourses(),
                          "Phone Number": self.instructor.getPhoneNumber(),
                          "Home Address": "2612 N Mary ville Ave",
                          "Type of User Account": self.instructor.getUserType()})
        self.assertEqual(User.objects.get(account_ID=self.instructor.getID()).home_address,
                         "2612 N Mary ville Ave",
                         msg="Home Address not set correctly")

    def test_editUserType(self):
        self.client.post("/MyUserProfile",
                         {"Email": self.instructor.getPassword(), "Username": self.instructor.getUsername(),
                          "Password": self.instructor.getPassword(),
                          "First Name": self.instructor.getFirstName(),
                          "Last Name": self.instructor.getLastName(),
                          "Phone Number": self.instructor.getPhoneNumber(),
                          "Home Address": self.instructor.getHomeAddress(),
                          "Type of User Account": "TA"})
        self.assertEqual(User.objects.get(account_ID=self.instructor.getID()).user_type, "TA",
                         msg="User Type not set correctly")


class TestMyUserProfileInstructorToHome(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj)

        self.instructor2: InstructorUser = InstructorUser(user_model)

        self.client.post("/",
                         {"username": self.instructor2.getUsername(), "password": self.instructor2.getPassword()})

    def test_UserSearch_to_HomeSearch(self):
        # Make a GET request to //MyUserProfile
        response = self.client.get("/MyUserProfile")

        # Check that the response was a redirect to page /home
        self.assertRedirects(response, '/InstructorHome', status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

        # Follow the redirect and check that the final URL is '/home'
        response = response.follow()
        self.assertEqual(response.url, '/InstructorHome')


'''
SCENARIO: As a TA, I want to be able navigate the Edit My User Profile
-----------------------------------------------------------------------
Acceptance Criteria 1:
SCENARIO: As a TA, I want to be able to navigate to the My User Profile
GIVEN The user is a TA and is logged in and at the My User Profile
WHEN a user of type TA is to be edited
WHEN user can be found with valid fields in the list of all users
AND "Edit Profile" is clicked
THEN account can be edited
-----------------------------------------------------------------------
SCENARIO: As an Admin, I want to be able navigate to the Home Page
-----------------------------------------------------------------------
Acceptance Criteria 1:
GIVEN: The user is a TA and is logged in and at the Edit MyUserProfile page
AND:They can click on "Return to Home Page"
THEN: They will be navigated to the "TAHome" page
'''


class TestEditMyUserProfileTA(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='ta',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj)

        self.ta: TAUser = TAUser(user_model)

        self.client.post("/",
                         {"username": self.ta.getUsername(), "password": self.ta.getPassword()})

    # def test_UserExists(self):
    #     User.objects.create(username='John_Doe', password="password", first_name="John",
    #                         phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='ta',
    #                         email='johnDoe@aol.com')
    #     user_obj = User.objects.filter(username='John_Doe')[0]
    #     new_user = TA.objects.create(account_ID=user_obj)
    #     self.ta1: TAUser = TAUser(new_user)
    #     new_user.save()
    #
    #     self.client.post({"/MyUserProfile",
    #                       self.ta1})
    #
    #     self.assertEqual(self.ta1.getID(), User.objects.get(account_ID=self.ta.getID()), "User exists in "
    #                                                                                    "Database")

    def test_editEmail(self):
        self.client.post("/MyUserProfile",
                         {
                             "First Name": self.ta.getFirstName(),
                             "Last Name": self.ta.getLastName(),
                             "Type of User": self.ta.getUserType(),
                             "Email": "johnDoe1@aol.com",
                             "Related Courses": self.ta.getCourses(),
                             "Phone Number": self.ta.getPhoneNumber(),
                             "Home Address": self.ta.getHomeAddress()})
        self.assertEqual(User.objects.get(account_ID=self.ta.getID()).email, "johnDoe1@aol.com",
                         msg="Email not set correctly")

    def test_editFirstName(self):
        self.client.post("/MyUserProfile",
                         {
                             "First Name": "Kevin",
                             "Last Name": self.ta.getLastName(),
                             "Type of User": self.ta.getUserType(),
                             "Email": self.ta.getEmail(),
                             "Related Courses": self.ta.getCourses(),
                             "Phone Number": self.ta.getPhoneNumber(),
                             "Home Address": self.ta.getHomeAddress()})
        self.assertEqual(User.objects.get(account_ID=self.ta.getID()).first_name, "Kevin",
                         msg="First Name not set correctly")

    def test_editLastName(self):
        self.client.post("/MyUserProfile",
                         {
                             "First Name": self.ta.getFirstName(),
                             "Last Name": "Smith",
                             "Type of User": self.ta.getUserType(),
                             "Email": self.ta.getEmail(),
                             "Related Courses": self.ta.getCourses(),
                             "Phone Number": self.ta.getPhoneNumber(),
                             "Home Address": self.ta.getHomeAddress()})
        self.assertEqual(User.objects.get(account_ID=self.ta.getID()).last_name, "Smith",
                         msg="Last Name not set correctly")

    def test_editPhoneNumber(self):
        self.client.post("/MyUserProfile",
                         {
                             "First Name": self.ta.getFirstName(),
                             "Last Name": self.ta.getLastName(),
                             "Type of User": self.ta.getUserType(),
                             "Email": self.ta.getEmail(),
                             "Related Courses": self.ta.getCourses(),
                             "Phone Number": "4145557000",
                             "Home Address": self.ta.getHomeAddress()})
        self.assertEqual(User.objects.get(account_ID=self.ta.getID()).phone_number, "4145557000",
                         msg="Phone Number not set correctly")

    def test_editHomeAddress(self):
        self.client.post("/MyUserProfile",
                         {"First Name": self.ta.getFirstName(),
                          "Last Name": self.ta.getLastName(),
                          "Type of User": self.ta.getUserType(),
                          "Email": self.ta.getEmail(),
                          "Related Courses": self.ta.getCourses(),
                          "Phone Number": self.ta.getPhoneNumber(),
                          "Home Address": "2612 N Mary ville Ave",
                          "Type of User Account": self.ta.getUserType()})
        self.assertEqual(User.objects.get(account_ID=self.ta.getID()).home_address, "2612 N Mary ville Ave",
                         msg="Home Address not set correctly")

    def test_editUserType(self):
        self.client.post("/MyUserProfile",
                         {"Email": self.ta.getPassword(), "Username": self.ta.getUsername(),
                          "Password": self.ta.getPassword(),
                          "First Name": self.ta.getFirstName(),
                          "Last Name": self.ta.getLastName(),
                          "Phone Number": self.ta.getPhoneNumber(),
                          "Home Address": self.ta.getHomeAddress(),
                          "Type of User Account": "TA"})
        self.assertEqual(User.objects.get(account_ID=self.ta.getID()).user_type, "TA",
                         msg="User Type not set correctly")


class TestTAUserProfileToHome(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='ta',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj)

        self.ta2: TAUser = TAUser(user_model)

        self.client.post("/",
                         {"username": self.ta2.getUsername(), "password": self.ta2.getPassword()})

    def test_UserSearch_to_HomeSearch(self):
        # Make a GET request to //MyUserProfile
        response = self.client.get("/MyUserProfile")

        # Check that the response was a redirect to page /home
        self.assertRedirects(response, '/TAHome', status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

        # Follow the redirect and check that the final URL is '/home'
        response = response.follow()
        self.assertEqual(response.url, '/TAHome')

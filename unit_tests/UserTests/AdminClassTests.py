from django.test import TestCase
from app.models import Admin, User
from classes.Users.users import AdminUser


# New Branch
class TestGetIDAdmin(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password="password", first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj)
        self.admin: AdminUser = AdminUser(user_model)

    def testID(self):
        account_id = self.admin.getID()
        self.assertEqual(self.admin.getID(), account_id,
                         msg="Admin User ID was not correctly "
                             "set up when creating a Admin")

    def testIDInstance(self):
        self.assertIsInstance(self.admin.getID(), int, msg="Correct Type was not stored in Database")


class TestGetAdminFirstName(TestCase):

    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj)

        self.admin: AdminUser = AdminUser(user_model)

    def testFirstNameExists(self):
        name = self.admin.getFirstName()
        self.assertNotEqual(name, None, msg="A first name exists")

    def testFirstName(self):
        first_name = self.admin.getFirstName()
        self.assertEqual(first_name, 'John',
                         msg="Incorrect First Name when setting up a admin")

    def testFirstNameTypeInstance(self):
        self.assertIsInstance(self.admin.getLastName(), str, msg="Correct Type was not stored in Database")


class TestSetAdminFirstName(TestCase):

    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj)

        self.admin: AdminUser = AdminUser(user_model)

    def testSetFirstName(self):
        # Set up the test data
        new_first_name = "Steven"

        # Exercise the system
        self.admin.setFirstName(new_first_name)

        # Retrieve the updated data from the database
        updated_admin = User.objects.get(account_ID=self.admin.getID())

        # Verify that the changes were stored in the database
        self.assertEqual(updated_admin.first_name, new_first_name, msg="Change was not reflected in Database")


class TestGetAdminLastName(TestCase):

    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password="password", first_name="John", last_name="Doe",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj)

        self.admin: AdminUser = AdminUser(user_model)

    def testLastName(self):
        name = self.admin.getLastName()
        self.assertEqual(name, 'Doe', msg="Incorrect Last Name when setting up a admin")

    def testLastNameExists(self):
        last_name = self.admin.getLastName()
        self.assertNotEqual(last_name, None, msg="A last name exists")

    def testLastNameTypeInstance(self):
        self.assertIsInstance(self.admin.getLastName(), str, msg="Correct Type was not stored in Database")


class TestSetAdminLastName(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password="password", first_name="John", last_name="Doe",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj)

        self.admin: AdminUser = AdminUser(user_model)

    def testNoArg(self):
        with self.assertRaises(TypeError, msg="Add ta - more than one arg is required"):
            self.admin.setLastName()

    def testSetLastName(self):
        # Set up the test data
        new_last_name = "Adams"

        # Exercise the system
        self.admin.setLastName(new_last_name)

        # Retrieve the updated data from the database
        updated_admin = User.objects.get(account_ID=self.admin.getID())

        # Verify that the changes were stored in the database
        self.assertEqual(updated_admin.first_name, new_last_name, msg="Change was not reflected in Database")


class TestGetAdminPhoneNumber(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj)

        self.admin: AdminUser = AdminUser(user_model)

    def testPhoneNumberExists(self):
        phone_number = self.admin.getPhoneNumber()
        self.assertNotEqual(phone_number, None, msg="A phone number exists")

    def testPhoneNumber(self):
        phone_number = self.admin.getPhoneNumber()
        self.assertEqual(phone_number, '4149818000',
                         "Phone was not set correctly when creating a Admin.")

    def testPhoneNumberTypeInstance(self):
        self.assertIsInstance(self.admin.getPhoneNumber(), str, msg="Invalid Phone Number Type stored in Database")

    def testPhoneNumberLength(self):
        phone_number_length = len(self.admin.getPhoneNumber())
        self.assertEqual(phone_number_length, 10, msg="Invalid Phone Number Length")


class TestSetAdminPhoneNumber(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj)

        self.admin: AdminUser = AdminUser(user_model)

    def testNoArg(self):
        with self.assertRaises(TypeError, msg="more than one arg is required"):
            self.admin.setPhoneNumber()

    def testSetPhoneNumber(self):
        # Set up the test data
        new_phone_number = "4149828002"

        # Exercise the system
        self.admin.setPhoneNumber(new_phone_number)

        # Retrieve the updated data from the database
        updated_admin = User.objects.get(account_ID=self.admin.getID())

        # Verify that the changes were stored in the database
        self.assertEqual(updated_admin.phone_number, new_phone_number, msg="Change was not reflected in Database")


class TestGetAdminAddress(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj)
        self.admin: AdminUser = AdminUser(user_model)

    def testHomeAddressExists(self):
        home_address = self.admin.getHomeAddress()
        self.assertNotEqual(home_address, None, msg="A home address exists")

    def testHomeAddress(self):
        home_address = self.admin.getHomeAddress()
        self.assertEqual(home_address, "2513 N Farewell Ave",
                         msg="Home Address was not set correctly when creating a Admin.")

    def testHomeAddressTypeInstance(self):
        self.assertIsInstance(self.admin.getHomeAddress(), str, msg="Incorrect type")


class TestSetAdminHomeAddress(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj)
        self.admin: AdminUser = AdminUser(user_model)

    def testNoArg(self):
        with self.assertRaises(TypeError, msg="more than one arg is required"):
            self.admin.setHomeAddress()

    def testSetHomeAddress(self):
        new_home_address = "2514 N Brady Ave"
        self.admin.setHomeAddress(new_home_address)
        # Retrieve the updated data from the database
        updated_admin = User.objects.get(account_ID=self.admin.getID())

        # Verify that the changes were stored in the database
        self.assertEqual(updated_admin.home_address, new_home_address, msg="Change was not reflected in Database")


class TestGetAdminUserType(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj)

        self.admin: AdminUser = AdminUser(user_model)

    def testUserType(self):
        user_type_admin = self.admin.getUserType()
        self.assertEqual(user_type_admin, "Admin",
                         msg="User type was not correctly set up when creating an Admin")


class TestSetAdminUserType(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj)

        self.admin: AdminUser = AdminUser(user_model)

    def testNoArg(self):
        with self.assertRaises(TypeError, msg="more than one arg is required"):
            self.admin.setUserType()

    def testSetUserType(self):
        new_type = "Admin"
        self.admin.setUserType(new_type)
        # Retrieve the updated data from the database
        updated_admin = User.objects.get(account_ID=self.admin.getID())

        # Verify that the changes were stored in the database
        self.assertEqual(updated_admin.user_type, new_type, msg="Change was not reflected in Database")


class TestGetAdminUserPassword(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj)

        self.admin: AdminUser = AdminUser(user_model)

    def testAdminPasswordExists(self):
        password = self.admin.getPassword()
        self.assertNotEqual(password, None, msg="A password cannot exist when the field is not "
                                                "declared")

    def testAdminPassword(self):
        password = self.admin.getPassword()
        self.assertEqual(password, "password", msg="Password was not set correctly when creating a "
                                                   "Admin.")

    def testAdminPasswordTypeInstance(self):
        password = self.admin.getPassword()
        self.assertIsInstance(password, str, msg="Incorrect Password Type in Database")


class TestSetAdminUserPassword(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj)

        self.admin: AdminUser = AdminUser(user_model)

    def testNoArg(self):
        with self.assertRaises(TypeError, msg="more than one arg is required"):
            self.admin.setPassword()

    def testSetUserPassword(self):
        new_password = 'new_password'
        self.admin.setPassword(new_password)
        # Retrieve the updated data from the database
        updated_admin = User.objects.get(account_ID=self.admin.getID())

        # Verify that the changes were stored in the database
        self.assertEqual(updated_admin.password, new_password, msg="Change was not reflected in Database")

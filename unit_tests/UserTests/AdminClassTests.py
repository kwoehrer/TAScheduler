from django.test import TestCase
from app.models import Admin, User
from classes.Users.users import AdminUser


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
        self.admin.setFirstName('Steven')
        name = self.admin.getFirstName()
        self.assertNotEqual(name, 'Adams',
                            msg="New changes were not reflected in Database")


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
        with self.assertRaises(TypeError, msg="Add ta - one arg is required"):
            self.admin.setLastName()

    def testSetLastName(self):
        self.admin.setLastName('Adams')
        name = self.admin.getLastName()
        self.assertNotEqual(name, 'Adams',
                            msg="New changes were not reflected in Database")


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
                         "Phone was not set correctly when creating a admin.")

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
        with self.assertRaises(TypeError, msg="one arg is required"):
            self.admin.setPhoneNumber()

    def testSetPhoneNumber(self):
        self.admin.setPhoneNumber("4149828002")
        phone_number = self.admin.getPhoneNumber()
        self.assertNotEqual(phone_number, "4149828002",
                            msg="New changes were not reflected in Database")


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
        with self.assertRaises(TypeError, msg="one arg is required"):
            self.admin.setHomeAddress()

    def testSetHomeAddress(self):
        self.admin.setHomeAddress("2514 N Brady Ave")
        home_address = self.admin.getHomeAddress()
        self.assertNotEqual(home_address, "2514 N Brady Ave",
                            msg="New changes were not reflected in Database")


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
        with self.assertRaises(TypeError, msg="one arg is required"):
            self.admin.setUserType()

    def testSetUserType(self):
        self.admin.setUserType('TA')
        user_type = self.admin.getUserType()
        self.assertNotEqual(user_type, 'TA',
                            msg="New changes were not reflected in Database")


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
        with self.assertRaises(TypeError, msg="one arg is required"):
            self.admin.setPassword()

    def testSetUserPassword(self):
        self.admin.setPassword('new_password')
        new_user_password = self.admin.getPassword()
        self.assertNotEqual(new_user_password, 'new_password',
                            msg="New changes were not reflected in Database")

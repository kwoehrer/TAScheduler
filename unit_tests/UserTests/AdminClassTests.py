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

    def testIDExists(self):
        User.objects.create(username='John_Doe', password="password", first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_model_new = Admin.objects.create(account_ID=user_object.account_ID)
        self.new_admin: AdminUser = AdminUser(user_model_new)
        self.assertNotEqual(None, self.new_admin.getID(), msg="AN ID cannot exist when the field is not "
                                                              "declared")

    def testID(self):
        self.assertEqual(User.objects.get(account_ID=self.admin.getID()), self.admin.getID(),
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
        self.assertNotEqual(None, self.admin.getFirstName(), msg="A password cannot exist when the field is not "
                                                                 "declared")

    def testFirstName(self):
        self.assertEqual("John", self.admin.getFirstName(), msg="Incorrect First Name when setting up a Admin")

    def testFirstNameType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when create was passed a first_name type with an "
                                   "invalid type"):
            User.objects.createUser(username='John_Doe', password="password", first_name=123,
                                    phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                                    email='johnDoe@aol.com')

    def testFirstNameTypeInstance(self):
        self.assertIsInstance(self.admin.getLastName(), str, msg="Correct Type was not stored in Database")


class TestSetAdminFirstName(TestCase):

    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj.account_ID)

        self.admin: AdminUser = AdminUser(user_model)

    def testNoArg(self):
        with self.assertRaises(TypeError, msg="Add ta - more than one arg is required"):
            self.admin.setFirstName()

    def testSetFirstName(self):
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_new_model = User.objects.create(account_ID=user_object.account_ID)
        self.new_admin: AdminUser = AdminUser(user_new_model)

        new_first_name = self.new_admin.setFirstName("Steven")
        self.assertEqual(new_first_name, self.admin.setFirstName(new_first_name),
                         msg="New changes were not reflected in Database")


class TestGetAdminLastName(TestCase):

    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj.account_ID)

        self.admin: AdminUser = AdminUser(user_model)

    def testLastName(self):
        self.assertEqual("Doe", self.admin.getLastName(), msg="Incorrect Last Name when setting up a Admin")

    def testLastNameExists(self):
        User.objects.create(username='John_Doe', password="password", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_model_new = Admin.objects.create(account_ID=user_object.account_ID)
        self.new_admin: AdminUser = AdminUser(user_model_new)
        self.assertNotEqual(None, self.new_admin.getLastName(), msg="A last name cannot exist when the field is not "
                                                                    "declared")

    def testLastNameType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when create was passed a last_name with an "
                                   "invalid type"):
            User.objects.createUser(username='John_Doe', password="password", first_name="John", last_name=123,
                                    phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                                    email='johnDoe@aol.com')

    def testLastNameTypeInstance(self):
        self.assertIsInstance(self.admin.getLastName(), str, msg="Correct Type was not stored in Database")


class TestSetAdminLastName(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj.account_ID)

        self.admin: AdminUser = AdminUser(user_model)

    def testNoArg(self):
        with self.assertRaises(TypeError, msg="Add ta - more than one arg is required"):
            self.admin.setLastName()

    def testSetLastName(self):
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_new_model = Admin.objects.create(account_ID=user_object.account_ID)
        self.new_admin: AdminUser = AdminUser(user_new_model)

        new_last_name = self.new_admin.setLastName("Adams")
        self.assertEqual(new_last_name, self.admin.setLastName(new_last_name),
                         msg="New changes were not reflected in Database")


class TestGetAdminPhoneNumber(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj.account_ID)

        self.admin: AdminUser = AdminUser(user_model)

    def testPhoneNumberExists(self):
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_model_new = Admin.objects.create(account_ID=user_object.account_ID)
        self.new_admin: AdminUser = AdminUser(user_model_new)
        self.assertNotEqual(None, self.new_admin.getPhoneNumber(),
                            msg="A phone number cannot exist when the field is not "
                                "declared")

    def testPhoneNumber(self):
        self.assertEqual("4149818000", self.admin.getPhoneNumber(),
                         "Phone was not set correctly when creating a Admin.")

    def testPhoneNumberType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createUser was passed a phone number with an "
                                   "invalid type"):
            User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                                email='johnDoe@aol.com')

    def testPhoneNumberTypeInstance(self):
        self.assertIsInstance(self.admin.getPhoneNumber(), str, msg="Invalid Phone Number Type stored in Database")

    def testPhoneNumberLength(self):
        with self.assertRaises(ValueError, msg="incorrect length for User Admin phone number"):
            self.assertEqual(10, len(self.admin.getPhoneNumber()))


class TestSetAdminPhoneNumber(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj.account_ID)

        self.admin: AdminUser = AdminUser(user_model)

    def testNoArg(self):
        with self.assertRaises(TypeError, msg="Add ta - more than one arg is required"):
            self.admin.setPhoneNumber()

    def testSetPhoneNumber(self):
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_new_model = Admin.objects.create(account_ID=user_object.account_ID)
        self.new_admin: AdminUser = AdminUser(user_new_model)

        new_phone_number = self.new_admin.setPhoneNumber("4149818001")
        self.assertEqual(new_phone_number, self.admin.getPhoneNumber(),
                         msg="New changes were not reflected in Database")


class TestGetAdminAddress(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj.account_ID)
        self.admin: AdminUser = AdminUser(user_model)

    def testHomeAddressExists(self):
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', user_type='Admin',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_model_new = Admin.objects.create(account_ID=user_object.account_ID)
        self.new_admin: AdminUser = AdminUser(user_model_new)
        self.assertNotEqual(None, self.new_admin.getHomeAddress(), msg="A password cannot exist when the field is not "
                                                                       "declared")

    def testHomeAddress(self):
        self.assertEqual("2513 N Farewell Ave", self.admin.getHomeAddress(),
                         "Home Address was not set correctly when creating a Admin.")

    def testHomeAddressType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createUser was passed an address with an "
                                   "invalid type"):
            User.objects.createUser(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                    phone_number='4149818000', home_address=2513, user_type='Admin',
                                    email='johnDoe@aol.com')

    def testHomeAddressTypeInstance(self):
        with self.assertRaises(TypeError, msg="incorrect User Admin home address Type"):
            self.assertIsInstance(self.admin.getHomeAddress(), str, msg="Incorrect type")


class TestSetAdminHomeAddress(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj.account_ID)
        self.admin: AdminUser = AdminUser(user_model)

    def testNoArg(self):
        with self.assertRaises(TypeError, msg="Add ta - more than one arg is required"):
            self.admin.setHomeAddress()

    def testSetHomeAddress(self):
        User.objects.create(username='John_Doe', last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_new_model = Admin.objects.create(account_ID=user_object.account_ID)
        self.new_admin: AdminUser = AdminUser(user_new_model)

        new_password = self.new_admin.setHomeAddress("2512 N Farewell Ave")
        self.assertEqual(new_password, self.admin.getHomeAddress(), msg="New changes were not reflected in Database")


class TestGetAdminUserType(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj.account_ID)

        self.admin: AdminUser = AdminUser(user_model)

    def testInvalidUserType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when create was passed a user type with an "
                                   "invalid type"):
            User.objects.createUser(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                    phone_number='4149818000', home_address='2513 N Farewell Ave', user_type=123,
                                    email='johnDoe@aol.com')

    def testUserType(self):
        self.assertEqual("Admin", self.admin.getUserType(),
                         msg="User type was not correctly set up when creating a Admin")


class TestSetAdminUserType(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj.account_ID)

        self.admin: AdminUser = AdminUser(user_model)

    def testNoArg(self):
        with self.assertRaises(TypeError, msg="Add ta - more than one arg is required"):
            self.admin.setUserType()

    def testSetUserType(self):
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type=None,
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_new_model = Admin.objects.create(account_ID=user_object.account_ID)
        self.new_admin: AdminUser = AdminUser(user_new_model)
        new_user_type = self.new_admin.setUserType("Admin")

        self.assertEqual(new_user_type, self.admin.getUserType(), msg="New changes were not reflected in Database")


class TestGetAdminUserPassword(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj.account_ID)

        self.admin: AdminUser = AdminUser(user_model)

    def testAdminPassword(self):
        self.assertEqual("password", self.admin.getPassword(), msg="Password was not set correctly when creating a "
                                                                   "Admin.")

    def testPasswordExists(self):
        User.objects.create(username='John_Doe', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model_new = User.objects.create(account_ID=user_obj.account_ID)
        self.new_admin: AdminUser = AdminUser(user_model_new)
        self.assertNotEqual(None, self.new_admin.getPassword(), msg="A password cannot exist when the field is not "
                                                                    "declared")

    def testAdminPasswordType(self):
        with self.assertRaises(TypeError, msg="An exception was not raised when create was passed a user type with an "
                                              "invalid type"):
            User.objects.create(username='John_Doe', password=123, first_name="John", last_name='Doe',
                                phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                                email='johnDoe@aol.com')

    def testAdminPasswordTypeInstance(self):
        self.assertIsInstance(self.admin.getPassword(), str, msg="Incorrect Password Type in Database")


class TestSetAdminUserPassword(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = User.objects.create(account_ID=user_obj.account_ID)

        self.admin: AdminUser = AdminUser(user_model)

    def testNoArg(self):
        with self.assertRaises(TypeError, msg="Add ta - more than one arg is required"):
            self.admin.setHomeAddress()

    def testSetPassword(self):
        User.objects.create(username='John_Doe', password=12345, first_name="John",
                            last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Admin',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_new_model = Admin.objects.create(account_ID=user_object.account_ID)
        self.new_admin: AdminUser = AdminUser(user_new_model)

        new_password = self.new_admin.setPassword("password2")
        self.assertEqual(new_password, self.admin.getPassword(), msg="New changes were not reflected in DaAdminbase")

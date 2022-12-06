from django.test import TestCase
from app.models import TA, User
from classes.Users.users import TAUser


class TestGetIDTA(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password="password", first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj)
        self.ta: TAUser = TAUser(user_model)

    def testID(self):
        account_id = self.ta.getID()
        self.assertEqual(self.ta.getID(), account_id,
                         msg="TA User ID was not correctly "
                             "set up when creating a TA")

    def testIDInstance(self):
        self.assertIsInstance(self.ta.getID(), int, msg="Correct Type was not stored in Database")


class TestGetTAFirstName(TestCase):

    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj)

        self.ta: TAUser = TAUser(user_model)

    def testFirstNameExists(self):
        name = self.ta.getFirstName()
        self.assertNotEqual(name, None, msg="A first name exists")

    def testFirstName(self):
        first_name = self.ta.getFirstName()
        self.assertEqual(first_name, 'John',
                         msg="Incorrect First Name when setting up a ta")

    def testFirstNameTypeInstance(self):
        self.assertIsInstance(self.ta.getLastName(), str, msg="Correct Type was not stored in Database")


class TestSetTAFirstName(TestCase):

    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj)

        self.ta: TAUser = TAUser(user_model)

    def testSetFirstName(self):
        self.ta.setFirstName('Steven')
        name = self.ta.getFirstName()
        self.assertNotEqual(name, 'Adams',
                            msg="New changes were not reflected in Database")


class TestGetTALastName(TestCase):

    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password="password", first_name="John", last_name="Doe",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj)

        self.ta: TAUser = TAUser(user_model)

    def testLastName(self):
        name = self.ta.getLastName()
        self.assertEqual(name, 'Doe', msg="Incorrect Last Name when setting up a ta")

    def testLastNameExists(self):
        last_name = self.ta.getLastName()
        self.assertNotEqual(last_name, None, msg="A last name exists")

    def testLastNameTypeInstance(self):
        self.assertIsInstance(self.ta.getLastName(), str, msg="Correct Type was not stored in Database")


class TestSetTALastName(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password="password", first_name="John", last_name="Doe",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj)

        self.ta: TAUser = TAUser(user_model)

    def testNoArg(self):
        with self.assertRaises(TypeError, msg="Add ta - one arg is required"):
            self.ta.setLastName()

    def testSetLastName(self):
        self.ta.setLastName('Adams')
        name = self.ta.getLastName()
        self.assertNotEqual(name, 'Adams',
                            msg="New changes were not reflected in Database")


class TestGetTAPhoneNumber(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj)

        self.ta: TAUser = TAUser(user_model)

    def testPhoneNumberExists(self):
        phone_number = self.ta.getPhoneNumber()
        self.assertNotEqual(phone_number, None, msg="A phone number exists")

    def testPhoneNumber(self):
        phone_number = self.ta.getPhoneNumber()
        self.assertEqual(phone_number, '4149818000',
                         "Phone was not set correctly when creating a TA.")

    def testPhoneNumberTypeInstance(self):
        self.assertIsInstance(self.ta.getPhoneNumber(), str, msg="Invalid Phone Number Type stored in Database")

    def testPhoneNumberLength(self):
        phone_number_length = len(self.ta.getPhoneNumber())
        self.assertEqual(phone_number_length, 10, msg="Invalid Phone Number Length")


class TestSetTAPhoneNumber(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj)

        self.ta: TAUser = TAUser(user_model)

    def testNoArg(self):
        with self.assertRaises(TypeError, msg="one arg is required"):
            self.ta.setPhoneNumber()

    def testSetPhoneNumber(self):
        self.ta.setPhoneNumber("4149828002")
        phone_number = self.ta.getPhoneNumber()
        self.assertNotEqual(phone_number, "4149828002",
                            msg="New changes were not reflected in Database")


class TestGetTAAddress(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj)
        self.ta: TAUser = TAUser(user_model)

    def testHomeAddressExists(self):
        home_address = self.ta.getHomeAddress()
        self.assertNotEqual(home_address, None, msg="A home address exists")

    def testHomeAddress(self):
        home_address = self.ta.getHomeAddress()
        self.assertEqual(home_address, "2513 N Farewell Ave",
                         msg="Home Address was not set correctly when creating a Admin.")

    def testHomeAddressTypeInstance(self):
        self.assertIsInstance(self.ta.getHomeAddress(), str, msg="Incorrect type")


class TestSetTAHomeAddress(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj)
        self.ta: TAUser = TAUser(user_model)

    def testNoArg(self):
        with self.assertRaises(TypeError, msg="one arg is required"):
            self.ta.setHomeAddress()

    def testSetHomeAddress(self):
        self.ta.setHomeAddress("2514 N Brady Ave")
        home_address = self.ta.getHomeAddress()
        self.assertNotEqual(home_address, "2514 N Brady Ave",
                            msg="New changes were not reflected in Database")


class TestGetTAUserType(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj)

        self.ta: TAUser = TAUser(user_model)

    def testUserType(self):
        user_type_admin = self.ta.getUserType()
        self.assertEqual(user_type_admin, "TA",
                         msg="User type was not correctly set up when creating an TA")


class TestSetTAUserType(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj)

        self.ta: TAUser = TAUser(user_model)

    def testNoArg(self):
        with self.assertRaises(TypeError, msg="one arg is required"):
            self.ta.setUserType()

    def testSetUserType(self):
        self.ta.setUserType("Instructor")
        user_type = self.ta.getUserType()
        self.assertNotEqual(user_type, "Instructor",
                            msg="New changes were not reflected in Database")


class TestGetTAUserPassword(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj)

        self.ta: TAUser = TAUser(user_model)

    def testTAPasswordExists(self):
        password = self.ta.getPassword()
        self.assertNotEqual(password, None, msg="A password cannot exist when the field is not "
                                                "declared")

    def testTAPassword(self):
        password = self.ta.getPassword()
        self.assertEqual(password, "password", msg="Password was not set correctly when creating a "
                                                   "TA.")

    def testTAPasswordTypeInstance(self):
        password = self.ta.getPassword()
        self.assertIsInstance(password, str, msg="Incorrect Password Type in Database")


class TestSetTAUserPassword(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj)

        self.ta: TAUser = TAUser(user_model)

    def testNoArg(self):
        with self.assertRaises(TypeError, msg="one arg is required"):
            self.ta.setPassword()

    def testSetUserPassword(self):
        self.ta.setPassword('new_password')
        new_user_password = self.ta.getPassword()
        self.assertNotEqual(new_user_password, 'new_password',
                            msg="New changes were not reflected in Database")

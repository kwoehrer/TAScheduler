from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from app.models import TA
from classes.Users.users import AbstractUser, TAUser


class TestGetIDTaName(TestCase):
    def setUp(self) -> None:
        TA.objects.create(account_ID=1000, username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)
        self.ta: TAUser = TAUser(user_model)

    def testIDExists(self):
        with self.assertRaises(ObjectDoesNotExist, msg="User TA first name does not exist"):
            self.assertEqual(None, self.ta.getFirstName())

    def testID(self):
        self.assertEqual(1000, self.ta.getID(), msg="TA User ID was not correctly set up when creating a TA")

    def testIDType(self):
        with self.assertRaises(TypeError, msg="An exception was not raised when createUser was passed a courseID with "
                                              "an "
                                              "invalid type"):
            TA.objects.create(account_ID=1001, username='John_Doe', password='password', first_name="John",
                              last_name='Doe',
                              phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='TA',
                              email='johnDoe@aol.com')


class TestGetTaName(TestCase):

    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)

        self.ta: TAUser = TAUser(user_model)

    def testFirstNameExists(self):
        with self.assertRaises(ObjectDoesNotExist, msg="User TA first name does not exist"):
            TA.objects.createUser(account_ID=1001, username='John_Doe', password='password',
                                  last_name='Doe',
                                  phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='TA',
                                  email='johnDoe@aol.com')

    def testLastNameExists(self):
        with self.assertRaises(ObjectDoesNotExist, msg="User TA last name does not exist"):
            TA.objects.createUser(account_ID=1001, username='John_Doe', password='password', first_name='John',
                                  phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='TA',
                                  email='johnDoe@aol.com')

    def testBadFirstName(self):
        # ta_first_name = TA.objects.filter(first_name="John")
        self.assertEqual("John", self.ta.getFirstName(), msg="Incorrect First Name when setting up a TA")
        # self.assertEqual(ta_first_name, self.ta.getFirstName())

    def testBadLastName(self):
        ta_last_name = TA.objects.create()
        self.assertEqual("Doe", self.ta.getLastName(), msg="Incorrect Last Name when setting up a TA")

    def testBadFirstNameType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createUser was passed a user type with an "
                                   "invalid type"):
            TA.objects.createUser(account_ID=1001, username='John_Doe', password='password', first_name=123,
                                  last_name='Doe',
                                  phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='TA',
                                  email='johnDoe@aol.com')

    def testBadLastNameType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createUser was passed a user type with an "
                                   "invalid type"):
            TA.objects.createUser(account_ID=1001, username='John_Doe', password='password', first_name="John",
                                  last_name=123,
                                  phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='TA',
                                  email='johnDoe@aol.com')


class TestSetTaName(TestCase):

    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)

        self.ta: TAUser = TAUser(user_model)

    def testNoArgsFirstName(self):
        with self.assertRaises(TypeError, msg="No Arguments provided for function requiring params"):
            self.ta.setFirstName()

    def testNoArgsLastName(self):
        with self.assertRaises(TypeError, msg="No Arguments provided for function requiring params"):
            self.ta.setLastName()

    def testSetFirstNameCorrectType(self):
        first_name = TA.objects.filter(first_name="John")

        # with self.assertRaises(ValueError, msg="Bad First Name"):
        #    self.assertEqual(1, self.ta.setFirstName(first_name), msg='First name was not correctly set up in '
        #                                                              'database')

        def checkIsDigit(string):
            res = [int(i) for i in string.split() if i.isdigit()]
            for i in res:
                if len(res) > 0:
                    return True
                return False

        with self.assertRaises(TypeError, msg="Bad First Name"):
            self.assertEqual(checkIsDigit(first_name), True, msg='There cannot be a digit in a name')

    def testSetLastNameCorrectType(self):
        last_name = TA.objects.filter(last_name="Doe")

        # with self.assertRaises(ValueError, msg="Bad Last Name"):
        #    self.assertEqual(1, self.ta.setFirstName(last_name), msg='Last name was not correctly set up in '
        #                                                             'database')

        def checkIsDigit(string):
            res = [int(i) for i in string.split() if i.isdigit()]
            for i in res:
                if len(res) > 0:
                    return True
                return False

        with self.assertRaises(TypeError, msg="Bad Last Name"):
            self.assertEqual(checkIsDigit(last_name), True, msg='There cannot be a digit in a name')

    def testSetBadFirstName(self):
        first_name = TA.objects.filter(first_name="John")
        first_new_name = self.ta.setFirstName("Steven")
        with self.assertRaises(ValueError, msg="Bad First Name"):
            self.assertEqual(1, self.ta.setFirstName(first_new_name), msg='First name was not correctly set up in '
                                                                          'database')
            self.assertEqual(first_name, self.ta.getFirstName(), msg='Incorrect First Name')

    def testSetBadLastName(self):
        last_name = TA.objects.filter(first_name="John")
        first_new_name = self.ta.setFirstName("Steven")
        with self.assertRaises(ValueError, msg="Bad Last Name"):
            self.assertEqual(1, self.ta.setFirstName(first_new_name), msg='Last name was not correctly set up in '
                                                                          'database')
            self.assertEqual(last_name, self.ta.getFirstName(), msg='Incorrect Last Name')


class TestGetTaPhoneNumber(TestCase):
    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)

        self.ta: TAUser = TAUser(user_model)

    def testPhoneNumberExists(self):
        with self.assertRaises(ObjectDoesNotExist, msg="User TA last name does not exist"):
            TA.objects.createUser(account_ID=1001, username='John_Doe', password='password', first_name='John',
                                  home_address='2513 N Farewell Ave', user_type='TA',
                                  email='johnDoe@aol.com')

    def testPhoneNumberCorrectType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createUser was passed a phone number with an "
                                   "invalid type"):
            TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                              phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='TA',
                              email='johnDoe@aol.com')

    def testBadPhoneNumberLength(self):
        with self.assertRaises(ValueError, msg="incorrect length for User TA phone number"):
            self.assertEqual(10, len(self.ta.getPhoneNumber()))

    def testBadPhoneNumber(self):
        self.assertEqual("4149818000", self.ta.getPhoneNumber(),
                         "User Phone was not set correctly when creating a User.")


class TestSetTaPhoneNumber(TestCase):
    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='ta')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)

        self.ta: TAUser = TAUser(user_model)

    def testNoArgs(self):
        with self.assertRaises(TypeError, msg="No Arguments provided for function requiring params"):
            self.ta.setPhoneNumber()

    def testSetPhoneNumberCorrectType(self):
        phone_number = TA.objects.filter(phone_number="4149818000")
        with self.assertRaises(TypeError, msg="Bad Phone Type"):
            self.assertIsInstance(self.ta.setPhoneNumber(phone_number), int, msg='Only integers allowed')

    def testSetBadPhoneNumber(self):
        phone_number = TA.objects.filter(phone_number="4149818000")
        first_new_name = self.ta.setPhoneNumber("4149818222")
        with self.assertRaises(ValueError, msg="Bad Phone Number"):
            self.assertEqual(1, self.ta.setFirstName(first_new_name), msg='Phone number was not correctly set up in '
                                                                          'database')
            self.assertEqual(phone_number, self.ta.getPhoneNumber(), msg='Incorrect Phone number')


class TestGetTaAddress(TestCase):
    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='ta')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)

        self.ta: AbstractUser = TAUser(user_model)

    def testHomeAddressExists(self):
        with self.assertRaises(ObjectDoesNotExist, msg="User TA home address does not exist"):
            self.ta.getHomeAddress()

    def testHomeAddressType(self):
        with self.assertRaises(TypeError, msg="incorrect User TA home address Type"):
            self.assertIsInstance(self.ta.getHomeAddress(), str, msg="Incorrect type")

    def testBadHomeAddress(self):
        home_address = TA.objects.filter(home_address="2513 N Farewell Ave")
        with self.assertRaises(ValueError, msg="incorrect user TA home address"):
            self.assertEqual(home_address, self.ta.getHomeAddress())


class TestGetTaHomeAddress(TestCase):
    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)

        self.ta: AbstractUser = TAUser(user_model)

    def testNoArgs(self):
        with self.assertRaises(TypeError, msg="No Arguments provided for function requiring params"):
            self.ta.setPhoneNumber()

    def testSetHomeAddressType(self):
        home_address = TA.objects.filter(home_address='2513 N Farewell Ave')
        with self.assertRaises(TypeError, msg="Bad Home Address Type"):
            self.assertIsInstance(self.ta.setHomeAddress(home_address), int, msg='Only integers allowed')

    def testSetBadHomeNumber(self):
        home_address = TA.objects.filter(home_address='12513 N Farewell Ave')
        new_home_address = self.ta.setHomeAddress('2513 N Farewell Ave')
        with self.assertRaises(ValueError, msg="Bad Phone Number"):
            self.assertEqual(1, self.ta.setHomeAddress(new_home_address), msg='Phone Number was not correctly set up '
                                                                              'in '
                                                                              'database')
            self.assertEqual(home_address, self.ta.getHomeAddress(), msg='Incorrect User TA Phone Number')


class TestGetTaUserType(TestCase):
    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)

        self.ta: AbstractUser = TAUser(user_model)

    def test_InvalidUserType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createUser was passed a user type with an "
                                   "invalid type"):
            TA.objects.createUser(account_ID=1001, username='John_Doe', password='password', first_name="John",
                                  last_name='Doe',
                                  phone_number=4149818000, home_address='2513 N Farewell Ave', user_type=100,
                                  email='johnDoe@aol.com')

    def testUserType(self):
        self.assertEqual("TA", self.ta.getUserType(), msg="User type was not correctly set up when creating a user")


class TestSetTaUserType(TestCase):
    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)

        self.ta: TAUser = TAUser(user_model)

    def testNoArgs(self):
        with self.assertRaises(TypeError, msg="No Arguments provided for function requiring params"):
            self.ta.setPhoneNumber()

    def testSetUserCorrectType(self):
        user_type = TA.objects.filter(user_type='TA')
        with self.assertRaises(TypeError, msg="Bad User Type"):
            self.assertIsInstance(self.ta.setUserType(user_type), str, msg='This is a TA object')


class TestGetTaUserPassword(TestCase):
    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)

        self.ta: TAUser = TAUser(user_model)

    def testUserTaPassword(self):
        self.assertEqual("password", self.ta.getP, "User Password was not set correctly when creating a "
                                                             "User.")

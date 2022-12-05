from django.test import TestCase
from app.models import TA
from classes.Users.users import TAUser


class TestGetIDTa(TestCase):
    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password="password", first_name="John", last_name='Doe',
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)
        self.ta: TAUser = TAUser(user_model)

    def testIDExists(self):
        TA.objects.create(username='John_Doe', password="password", first_name="John", last_name='Doe',
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_object = TA.objects.filter(username='John_Doe')[0]
        user_model_new = TA.objects.create(account_ID=user_object.account_ID)
        self.new_ta: TAUser = TAUser(user_model_new)
        self.assertNotEqual(None, self.new_ta.getID(), msg="AN ID cannot exist when the field is not "
                                                           "declared")

    def testID(self):
        self.assertEqual(TA.objects.get(account_ID=TA.account_ID), self.ta.getID(),
                         msg="TA User ID was not correctly "
                             "set up when creating a TA")

    def testIDInstance(self):
        self.assertIsInstance(self.ta.getID(), int, msg="Correct Type was not stored in Database")


class TestGetTaFirstName(TestCase):

    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password="password", first_name="John",
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)

        self.ta: TAUser = TAUser(user_model)

    def testFirstNameExists(self):
        TA.objects.create(username='John_Doe', password="password", last_name='Doe',
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_object = TA.objects.filter(username='John_Doe')[0]
        user_model_new = TA.objects.create(account_ID=user_object.account_ID)
        self.new_ta: TAUser = TAUser(user_model_new)
        self.assertNotEqual(None, self.new_ta.getFirstName(), msg="A password cannot exist when the field is not "
                                                                  "declared")

    def testFirstName(self):
        # ta_first_name = TA.objects.filter(first_name="John")
        self.assertEqual("John", self.ta.getFirstName(), msg="Incorrect First Name when setting up a TA")
        # self.assertEqual(ta_first_name, self.ta.getFirstName())

    def testFirstNameType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when create was passed a first_name type with an "
                                   "invalid type"):
            TA.objects.createUser(username='John_Doe', password="password", first_name=123,
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                                  email='johnDoe@aol.com')

    def testFirstNameTypeInstance(self):
        self.assertIsInstance(self.ta.getLastName(), str, msg="Correct Type was not stored in Database")


class TestSetTaFirstName(TestCase):

    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password="password", first_name="John",
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)

        self.ta: TAUser = TAUser(user_model)

    def testNoArgs(self):
        with self.assertRaises(TypeError, msg="atleast one argument needs to be provided"):
            self.ta.setFirstName()

    def testSetFirstName(self):
        TA.objects.create(username='John_Doe', password="password", first_name="John",
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_object = TA.objects.filter(username='John_Doe')[0]
        user_new_model = TA.objects.create(account_ID=user_object.account_ID)
        self.new_ta: TAUser = TAUser(user_new_model)

        new_first_name = self.new_ta.setFirstName("Steven")
        self.assertEqual(new_first_name, self.ta.setFirstName(new_first_name),
                         msg="New changes were not reflected in Database")


class TestGetTaLastName(TestCase):

    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password="password", first_name="John",
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)

        self.ta: TAUser = TAUser(user_model)

    def testLastName(self):
        self.assertEqual("Doe", self.ta.getLastName(), msg="Incorrect Last Name when setting up a TA")

    def testLastNameExists(self):
        TA.objects.create(username='John_Doe', password="password", last_name='Doe',
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_object = TA.objects.filter(username='John_Doe')[0]
        user_model_new = TA.objects.create(account_ID=user_object.account_ID)
        self.new_ta: TAUser = TAUser(user_model_new)
        self.assertNotEqual(None, self.new_ta.getLastName(), msg="A last name cannot exist when the field is not "
                                                                 "declared")

    def testLastNameType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when create was passed a last_name with an "
                                   "invalid type"):
            TA.objects.createUser(username='John_Doe', password="password", first_name="John", last_name=123,
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                                  email='johnDoe@aol.com')

    def testLastNameTypeInstance(self):
        self.assertIsInstance(self.ta.getLastName(), str, msg="Correct Type was not stored in Database")


class TestSetTaLastName(TestCase):
    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password="password", first_name="John",
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)

        self.ta: TAUser = TAUser(user_model)

    def testNoArgs(self):
        with self.assertRaises(TypeError, msg="atleast one argument needs to be provided"):
            self.ta.setLastName()

    def testSetLastName(self):
        TA.objects.create(username='John_Doe', password="password", first_name="John",
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_object = TA.objects.filter(username='John_Doe')[0]
        user_new_model = TA.objects.create(account_ID=user_object.account_ID)
        self.new_ta: TAUser = TAUser(user_new_model)

        new_last_name = self.new_ta.setLastName("Adams")
        self.assertEqual(new_last_name, self.ta.setLastName(new_last_name),
                         msg="New changes were not reflected in Database")


class TestGetTaPhoneNumber(TestCase):
    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)

        self.ta: TAUser = TAUser(user_model)

    def testPhoneNumberExists(self):
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_object = TA.objects.filter(username='John_Doe')[0]
        user_model_new = TA.objects.create(account_ID=user_object.account_ID)
        self.new_ta: TAUser = TAUser(user_model_new)
        self.assertNotEqual(None, self.new_ta.getPhoneNumber(), msg="A phone number cannot exist when the field is not "
                                                                    "declared")

    def testPhoneNumber(self):
        self.assertEqual("4149818000", self.ta.getPhoneNumber(),
                         "Phone was not set correctly when creating a TA.")

    def testPhoneNumberType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createUser was passed a phone number with an "
                                   "invalid type"):
            TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                              phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                              email='johnDoe@aol.com')

    def testPhoneNumberTypeInstance(self):
        self.assertIsInstance(self.ta.getPhoneNumber(), str, msg="Invalid Phone Number Type stored in Database")

    def testPhoneNumberLength(self):
        with self.assertRaises(ValueError, msg="incorrect length for User TA phone number"):
            self.assertEqual(10, len(self.ta.getPhoneNumber()))


class TestSetTaPhoneNumber(TestCase):
    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='ta')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)

        self.ta: TAUser = TAUser(user_model)

    def testNoArgs(self):
        with self.assertRaises(TypeError, msg="atleast one argument needs to be provided"):
            self.ta.setPhoneNumber()

    def testSetPhoneNumber(self):
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_object = TA.objects.filter(username='John_Doe')[0]
        user_new_model = TA.objects.create(account_ID=user_object.account_ID)
        self.new_ta: TAUser = TAUser(user_new_model)

        new_phone_number = self.new_ta.setPhoneNumber("4149818001")
        self.assertEqual(new_phone_number, self.ta.getPhoneNumber(), msg="New changes were not reflected in Database")


class TestGetTaAddress(TestCase):
    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)
        self.ta: TAUser = TAUser(user_model)

    def testHomeAddressExists(self):
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number='4149818000', user_type='TA',
                          email='johnDoe@aol.com')
        user_object = TA.objects.filter(username='John_Doe')[0]
        user_model_new = TA.objects.create(account_ID=user_object.account_ID)
        self.new_ta: TAUser = TAUser(user_model_new)
        self.assertNotEqual(None, self.new_ta.getHomeAddress(), msg="A password cannot exist when the field is not "
                                                                    "declared")

    def testHomeAddress(self):
        self.assertEqual("2513 N Farewell Ave", self.ta.getHomeAddress(),
                         "Home Address was not set correctly when creating a TA.")

    def testHomeAddressType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createUser was passed an address with an "
                                   "invalid type"):
            TA.objects.createUser(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number='4149818000', home_address=2513, user_type='TA',
                                  email='johnDoe@aol.com')

    def testHomeAddressTypeInstance(self):
        with self.assertRaises(TypeError, msg="incorrect User TA home address Type"):
            self.assertIsInstance(self.ta.getHomeAddress(), str, msg="Incorrect type")


class TestSetTaHomeAddress(TestCase):
    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', last_name='Doe',
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)
        self.ta: TAUser = TAUser(user_model)

    def testNoArgs(self):
        with self.assertRaises(TypeError, msg="atleast one argument needs to be provided"):
            self.ta.setHomeAddress()

    def testSetHomeAddress(self):
        TA.objects.create(username='John_Doe', last_name='Doe',
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_object = TA.objects.filter(username='John_Doe')[0]
        user_new_model = TA.objects.create(account_ID=user_object.account_ID)
        self.new_ta: TAUser = TAUser(user_new_model)

        new_password = self.new_ta.setHomeAddress("2512 N Farewell Ave")
        self.assertEqual(new_password, self.ta.getHomeAddress(), msg="New changes were not reflected in Database")


class TestGetTaUserType(TestCase):
    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)

        self.ta: TAUser = TAUser(user_model)

    def testUserTypeInstance(self):
        self.assertEqual("TA", self.ta.getUserType(), msg="User type was not correctly set up when creating a TA")


class TestSetTaUserType(TestCase):
    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)

        self.ta: TAUser = TAUser(user_model)

    def testNoArgs(self):
        with self.assertRaises(TypeError, msg="atleast one argument needs to be provided"):
            self.ta.setUserType()

    def testSetUserType(self):
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type=None,
                          email='johnDoe@aol.com')
        user_object = TA.objects.filter(username='John_Doe')[0]
        user_new_model = TA.objects.create(account_ID=user_object.account_ID)
        self.new_ta: TAUser = TAUser(user_new_model)
        new_user_type = self.new_ta.setUserType("TA")

        self.assertEqual(new_user_type, self.ta.getUserType(), msg="New changes were not reflected in Database")


class TestGetTaUserPassword(TestCase):
    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)

        self.ta: TAUser = TAUser(user_model)

    def testTaPassword(self):
        self.assertEqual("password", self.ta.getPassword(), msg="Password was not set correctly when creating a "
                                                                "TA.")

    def testPasswordExists(self):
        TA.objects.create(username='John_Doe', first_name="John", last_name='Doe',
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model_new = TA.objects.create(account_ID=user_obj.account_ID)
        self.new_ta: TAUser = TAUser(user_model_new)
        self.assertNotEqual(None, self.new_ta.getPassword(), msg="A password cannot exist when the field is not "
                                                                 "declared")

    def testTaPasswordType(self):
        with self.assertRaises(TypeError, msg="An exception was not raised when create was passed a user type with an "
                                              "invalid type"):
            TA.objects.create(username='John_Doe', password=123, first_name="John", last_name='Doe',
                              phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                              email='johnDoe@aol.com')

    def testTaPasswordTypeInstance(self):
        self.assertIsInstance(self.ta.getPassword(), str, msg="Incorrect Password Type in Database")


class TestSetTaUserPassword(TestCase):
    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)

        self.ta: TAUser = TAUser(user_model)

    def testNoArgs(self):
        with self.assertRaises(TypeError, msg="atleast one argument needs to be provided"):
            self.ta.setUserType()

    def testSetPassword(self):
        TA.objects.create(username='John_Doe', password=12345, first_name="John",
                          last_name='Doe',
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_object = TA.objects.filter(username='John_Doe')[0]
        user_new_model = TA.objects.create(account_ID=user_object.account_ID)
        self.new_ta: TAUser = TAUser(user_new_model)

        new_password = self.new_ta.setPassword("password2")
        self.assertEqual(new_password, self.ta.getPassword(), msg="New changes were not reflected in Database")


class TestGetTaEmail(TestCase):
    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)
        self.ta: TAUser = TAUser(user_model)

    def testEmailExists(self):
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number='4149818000', user_type='TA')
        user_object = TA.objects.filter(username='John_Doe')[0]
        user_model_new = TA.objects.create(account_ID=user_object.account_ID)
        self.new_ta: TAUser = TAUser(user_model_new)
        self.assertNotEqual(None, self.new_ta.getEmail(), msg="An email cannot exist when the field is not "
                                                              "declared")

    def testEmailAddress(self):
        self.assertEqual("johnDoe@aol.com", self.ta.getEmail(),
                         "Email Address was not set correctly when creating a TA.")

    def testEmailAddressType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when create was passed an email with an "
                                   "invalid type"):
            TA.objects.createUser(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number='4149818000', home_address=2513, user_type='TA',
                                  email=12345)

    def testEmailTypeInstance(self):
        with self.assertRaises(TypeError, msg="incorrect User TA home address Type"):
            self.assertIsInstance(self.ta.getEmail(), str, msg="Incorrect type")


class TestSetEmail(TestCase):
    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)

        self.ta: TAUser = TAUser(user_model)

    def testNoArgs(self):
        with self.assertRaises(TypeError, msg="atleast one argument needs to be provided"):
            self.ta.setEmail()

    def testSetEmail(self):
        TA.objects.create(username='John_Doe', password=12345, first_name="John",
                          last_name='Doe',
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_object = TA.objects.filter(username='John_Doe')[0]
        user_new_model = TA.objects.create(account_ID=user_object.account_ID)
        self.new_ta: TAUser = TAUser(user_new_model)

        new_email = self.new_ta.setEmail('johnDoe1@aol.com')
        self.assertEqual(new_email, self.ta.getEmail(), msg="New changes were not reflected in Database")


class TestGetTaUsername(TestCase):
    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)
        self.ta: TAUser = TAUser(user_model)

    def testUsernameExists(self):
        TA.objects.create(password='password', first_name="John", last_name='Doe',
                          phone_number='4149818000', user_type='TA', email='johnDoe@aol.com')
        user_object = TA.objects.filter(username='John_Doe')[0]
        user_model_new = TA.objects.create(account_ID=user_object.account_ID)
        self.new_ta: TAUser = TAUser(user_model_new)
        self.assertNotEqual(None, self.new_ta.getEmail(), msg="An email cannot exist when the field is not "
                                                              "declared")

    def testUsername(self):
        self.assertEqual("John_Doe", self.ta.getUsername(),
                         "Username was not set correctly when creating a TA.")

    def testUsernameType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when create was passed a username with an "
                                   "invalid type"):
            TA.objects.createUser(username=12345, password='password', first_name="John", last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                                  email='johnDoe@aol.com')

    def testHomeAddressTypeInstance(self):
        with self.assertRaises(TypeError, msg="incorrect User TA home address Type"):
            self.assertIsInstance(self.ta.getEmail(), str, msg="Incorrect type")


class TestSetUsername(TestCase):
    def setUp(self) -> None:
        TA.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_obj = TA.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_obj.account_ID)

        self.ta: TAUser = TAUser(user_model)

    def testNoArgs(self):
        with self.assertRaises(TypeError, msg="atleast one argument needs to be provided"):
            self.ta.setUsername()

    def testSetUsername(self):
        TA.objects.create(username='John_Doe', password=12345, first_name="John",
                          last_name='Doe',
                          phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='TA',
                          email='johnDoe@aol.com')
        user_object = TA.objects.filter(username='John_Doe')[0]
        user_new_model = TA.objects.create(account_ID=user_object.account_ID)
        self.new_ta: TAUser = TAUser(user_new_model)

        new_username = self.new_ta.setUsername('Steven_Adams')
        self.assertEqual(new_username, self.ta.getUsername(), msg="New changes were not reflected in Database")

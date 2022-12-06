from django.test import TestCase
from app.models import Instructor
from classes.Users.users import InstructorUser


class TestGetIDInstructor(TestCase):
    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password="password", first_name="John", last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)
        self.instructor: InstructorUser = InstructorUser(user_model)

    def testIDExists(self):
        Instructor.objects.create(username='John_Doe', password="password", first_name="John", last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_object = Instructor.objects.filter(username='John_Doe')[0]
        user_model_new = Instructor.objects.create(account_ID=user_object.account_ID)
        self.new_instructor: InstructorUser = InstructorUser(user_model_new)
        self.assertNotEqual(None, self.new_instructor.getID(), msg="AN ID cannot exist when the field is not "
                                                                   "declared")

    def testID(self):
        self.assertEqual(Instructor.objects.get(account_ID=Instructor.account_ID), self.instructor.getID(),
                         msg="Instructor User ID was not correctly "
                             "set up when creating a Instructor")

    def testIDInstance(self):
        self.assertIsInstance(self.instructor.getID(), int, msg="Correct Type was not stored in Database")


class TestGetInstructorFirstName(TestCase):

    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password="password", first_name="John",
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testFirstNameExists(self):
        Instructor.objects.create(username='John_Doe', password="password", last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_object = Instructor.objects.filter(username='John_Doe')[0]
        user_model_new = Instructor.objects.create(account_ID=user_object.account_ID)
        self.new_instructor: InstructorUser = InstructorUser(user_model_new)
        self.assertNotEqual(None, self.new_instructor.getFirstName(),
                            msg="A password cannot exist when the field is not "
                                "declared")

    def testFirstName(self):
        self.assertEqual("John", self.instructor.getFirstName(),
                         msg="Incorrect First Name when setting up a Instructor")

    def testFirstNameType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when create was passed a first_name type with an "
                                   "invalid type"):
            Instructor.objects.createUser(username='John_Doe', password="password", first_name=123,
                                          phone_number='4149818000', home_address='2513 N Farewell Ave',
                                          user_type='Instructor',
                                          email='johnDoe@aol.com')

    def testFirstNameTypeInstance(self):
        self.assertIsInstance(self.instructor.getLastName(), str, msg="Correct Type was not stored in Database")


class TestSetInstructorFirstName(TestCase):

    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password="password", first_name="John",
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testSetFirstName(self):
        Instructor.objects.create(username='John_Doe', password="password", first_name="John",
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_object = Instructor.objects.filter(username='John_Doe')[0]
        user_new_model = Instructor.objects.create(account_ID=user_object.account_ID)
        self.new_instructor: InstructorUser = InstructorUser(user_new_model)

        new_first_name = self.new_instructor.setFirstName("Steven")
        self.assertEqual(new_first_name, self.instructor.setFirstName(new_first_name),
                         msg="New changes were not reflected in Database")


class TestGetInstructorLastName(TestCase):

    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password="password", first_name="John",
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testLastName(self):
        self.assertEqual("Doe", self.instructor.getLastName(), msg="Incorrect Last Name when setting up a Instructor")

    def testLastNameExists(self):
        Instructor.objects.create(username='John_Doe', password="password", last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_object = Instructor.objects.filter(username='John_Doe')[0]
        user_model_new = Instructor.objects.create(account_ID=user_object.account_ID)
        self.new_instructor: InstructorUser = InstructorUser(user_model_new)
        self.assertNotEqual(None, self.new_instructor.getLastName(),
                            msg="A last name cannot exist when the field is not "
                                "declared")

    def testLastNameType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when create was passed a last_name with an "
                                   "invalid type"):
            Instructor.objects.createUser(username='John_Doe', password="password", first_name="John", last_name=123,
                                          phone_number='4149818000', home_address='2513 N Farewell Ave',
                                          user_type='Instructor',
                                          email='johnDoe@aol.com')

    def testLastNameTypeInstance(self):
        self.assertIsInstance(self.instructor.getLastName(), str, msg="Correct Type was not stored in Database")


class TestSetInstructorLastName(TestCase):
    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password="password", first_name="John",
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testSetLastName(self):
        Instructor.objects.create(username='John_Doe', password="password", first_name="John",
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_object = Instructor.objects.filter(username='John_Doe')[0]
        user_new_model = Instructor.objects.create(account_ID=user_object.account_ID)
        self.new_instructor: InstructorUser = InstructorUser(user_new_model)

        new_last_name = self.new_instructor.setLastName("Adams")
        self.assertEqual(new_last_name, self.instructor.setLastName(new_last_name),
                         msg="New changes were not reflected in Database")


class TestGetInstructorPhoneNumber(TestCase):
    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testPhoneNumberExists(self):
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_object = Instructor.objects.filter(username='John_Doe')[0]
        user_model_new = Instructor.objects.create(account_ID=user_object.account_ID)
        self.new_instructor: InstructorUser = InstructorUser(user_model_new)
        self.assertNotEqual(None, self.new_instructor.getPhoneNumber(),
                            msg="A phone number cannot exist when the field is not "
                                "declared")

    def testPhoneNumber(self):
        self.assertEqual("4149818000", self.instructor.getPhoneNumber(),
                         "Phone was not set correctly when creating a Instructor.")

    def testPhoneNumberType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createUser was passed a phone number with an "
                                   "invalid type"):
            Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                      phone_number='4149818000', home_address='2513 N Farewell Ave',
                                      user_type='Instructor',
                                      email='johnDoe@aol.com')

    def testPhoneNumberTypeInstance(self):
        self.assertIsInstance(self.instructor.getPhoneNumber(), str, msg="Invalid Phone Number Type stored in Database")

    def testPhoneNumberLength(self):
        with self.assertRaises(ValueError, msg="incorrect length for User Instructor phone number"):
            self.assertEqual(10, len(self.instructor.getPhoneNumber()))


class TestSetInstructorPhoneNumber(TestCase):
    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='instructor')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testSetPhoneNumber(self):
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_object = Instructor.objects.filter(username='John_Doe')[0]
        user_new_model = Instructor.objects.create(account_ID=user_object.account_ID)
        self.new_instructor: InstructorUser = InstructorUser(user_new_model)

        new_phone_number = self.new_instructor.setPhoneNumber("4149818001")
        self.assertEqual(new_phone_number, self.instructor.getPhoneNumber(),
                         msg="New changes were not reflected in Database")


class TestGetInstructorAddress(TestCase):
    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)
        self.instructor: InstructorUser = InstructorUser(user_model)

    def testHomeAddressExists(self):
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number='4149818000', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_object = Instructor.objects.filter(username='John_Doe')[0]
        user_model_new = Instructor.objects.create(account_ID=user_object.account_ID)
        self.new_instructor: InstructorUser = InstructorUser(user_model_new)
        self.assertNotEqual(None, self.new_instructor.getHomeAddress(),
                            msg="A password cannot exist when the field is not "
                                "declared")

    def testHomeAddress(self):
        self.assertEqual("2513 N Farewell Ave", self.instructor.getHomeAddress(),
                         "Home Address was not set correctly when creating a Instructor.")

    def testHomeAddressType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createUser was passed an address with an "
                                   "invalid type"):
            Instructor.objects.createUser(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                          phone_number='4149818000', home_address=2513, user_type='Instructor',
                                          email='johnDoe@aol.com')

    def testHomeAddressTypeInstance(self):
        with self.assertRaises(TypeError, msg="incorrect User Instructor home address Type"):
            self.assertIsInstance(self.instructor.getHomeAddress(), str, msg="Incorrect type")


class TestSetInstructorHomeAddress(TestCase):
    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)
        self.instructor: InstructorUser = InstructorUser(user_model)

    def testSetHomeAddress(self):
        Instructor.objects.create(username='John_Doe', last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_object = Instructor.objects.filter(username='John_Doe')[0]
        user_new_model = Instructor.objects.create(account_ID=user_object.account_ID)
        self.new_instructor: InstructorUser = InstructorUser(user_new_model)

        new_password = self.new_instructor.setHomeAddress("2512 N Farewell Ave")
        self.assertEqual(new_password, self.instructor.getHomeAddress(),
                         msg="New changes were not reflected in Database")


class TestGetInstructorUserType(TestCase):
    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testUserTypeInstance(self):
        self.assertEqual("Instructor", self.instructor.getUserType(),
                         msg="User type was not correctly set up when creating a Instructor")


class TestSetInstructorUserType(TestCase):
    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testSetUserType(self):
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type=None,
                                  email='johnDoe@aol.com')
        user_object = Instructor.objects.filter(username='John_Doe')[0]
        user_new_model = Instructor.objects.create(account_ID=user_object.account_ID)
        self.new_instructor: InstructorUser = InstructorUser(user_new_model)
        new_user_type = self.new_instructor.setUserType("Instructor")

        self.assertEqual(new_user_type, self.instructor.getUserType(), msg="New changes were not reflected in Database")


class TestGetInstructorUserPassword(TestCase):
    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testInstructorPassword(self):
        self.assertEqual("password", self.instructor.getPassword(),
                         msg="Password was not set correctly when creating a "
                             "Instructor.")

    def testPasswordExists(self):
        Instructor.objects.create(username='John_Doe', first_name="John", last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model_new = Instructor.objects.create(account_ID=user_obj.account_ID)
        self.new_instructor: InstructorUser = InstructorUser(user_model_new)
        self.assertNotEqual(None, self.new_instructor.getPassword(),
                            msg="A password cannot exist when the field is not "
                                "declared")

    def testInstructorPasswordType(self):
        with self.assertRaises(TypeError, msg="An exception was not raised when create was passed a user type with an "
                                              "invalid type"):
            Instructor.objects.create(username='John_Doe', password=123, first_name="John", last_name='Doe',
                                      phone_number='4149818000', home_address='2513 N Farewell Ave',
                                      user_type='Instructor',
                                      email='johnDoe@aol.com')

    def testInstructorPasswordTypeInstance(self):
        self.assertIsInstance(self.instructor.getPassword(), str, msg="Incorrect Password Type in Database")


class TestSetInstructorUserPassword(TestCase):
    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testSetPassword(self):
        Instructor.objects.create(username='John_Doe', password=12345, first_name="John",
                                  last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_object = Instructor.objects.filter(username='John_Doe')[0]
        user_new_model = Instructor.objects.create(account_ID=user_object.account_ID)
        self.new_instructor: InstructorUser = InstructorUser(user_new_model)

        new_password = self.new_instructor.setPassword("password2")
        self.assertEqual(new_password, self.instructor.getPassword(), msg="New changes were not reflected in Database")


class TestGetInstructorEmail(TestCase):
    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)
        self.instructor: InstructorUser = InstructorUser(user_model)

    def testEmailExists(self):
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number='4149818000', user_type='Instructor')
        user_object = Instructor.objects.filter(username='John_Doe')[0]
        user_model_new = Instructor.objects.create(account_ID=user_object.account_ID)
        self.new_instructor: InstructorUser = InstructorUser(user_model_new)
        self.assertNotEqual(None, self.new_instructor.getEmail(), msg="An email cannot exist when the field is not "
                                                                      "declared")

    def testEmailAddress(self):
        self.assertEqual("johnDoe@aol.com", self.instructor.getEmail(),
                         "Email Address was not set correctly when creating a Instructor.")

    def testEmailAddressType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when create was passed an email with an "
                                   "invalid type"):
            Instructor.objects.createUser(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                          phone_number='4149818000', home_address=2513, user_type='Instructor',
                                          email=12345)

    def testEmailTypeInstance(self):
        with self.assertRaises(TypeError, msg="incorrect User Instructor home address Type"):
            self.assertIsInstance(self.instructor.getEmail(), str, msg="Incorrect type")


class TestSetEmail(TestCase):
    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testSetEmail(self):
        Instructor.objects.create(username='John_Doe', password=12345, first_name="John",
                                  last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_object = Instructor.objects.filter(username='John_Doe')[0]
        user_new_model = Instructor.objects.create(account_ID=user_object.account_ID)
        self.new_instructor: InstructorUser = InstructorUser(user_new_model)

        new_email = self.new_instructor.setEmail('johnDoe1@aol.com')
        self.assertEqual(new_email, self.instructor.getEmail(), msg="New changes were not reflected in Database")


class TestGetInstructorUsername(TestCase):
    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)
        self.instructor: InstructorUser = InstructorUser(user_model)

    def testUsernameExists(self):
        Instructor.objects.create(password='password', first_name="John", last_name='Doe',
                                  phone_number='4149818000', user_type='Instructor', email='johnDoe@aol.com')
        user_object = Instructor.objects.filter(username='John_Doe')[0]
        user_model_new = Instructor.objects.create(account_ID=user_object.account_ID)
        self.new_instructor: InstructorUser = InstructorUser(user_model_new)
        self.assertNotEqual(None, self.new_instructor.getEmail(), msg="An email cannot exist when the field is not "
                                                                      "declared")

    def testUsername(self):
        self.assertEqual("John_Doe", self.instructor.getUsername(),
                         "Username was not set correctly when creating a Instructor.")

    def testUsernameType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when create was passed a username with an "
                                   "invalid type"):
            Instructor.objects.createUser(username=12345, password='password', first_name="John", last_name='Doe',
                                          phone_number='4149818000', home_address='2513 N Farewell Ave',
                                          user_type='Instructor',
                                          email='johnDoe@aol.com')

    def testHomeAddressTypeInstance(self):
        with self.assertRaises(TypeError, msg="incorrect User Instructor home address Type"):
            self.assertIsInstance(self.instructor.getEmail(), str, msg="Incorrect type")


class TestSetUsername(TestCase):
    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testSetUsername(self):
        Instructor.objects.create(username='John_Doe', password=12345, first_name="John",
                                  last_name='Doe',
                                  phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_object = Instructor.objects.filter(username='John_Doe')[0]
        user_new_model = Instructor.objects.create(account_ID=user_object.account_ID)
        self.new_instructor: InstructorUser = InstructorUser(user_new_model)

        new_username = self.new_instructor.setUsername('Steven_Adams')
        self.assertEqual(new_username, self.instructor.getUsername(), msg="New changes were not reflected in Database")

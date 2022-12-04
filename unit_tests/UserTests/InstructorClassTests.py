from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from app.models import Instructor
from classes.Users.users import InstructorUser


class TestGetInstructorName(TestCase):

    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testFirstNameExists(self):
        with self.assertRaises(ObjectDoesNotExist, msg="User Instructor first name does not exist"):
            self.instructor.getFirstName()

    def testLastNameExists(self):
        with self.assertRaises(ObjectDoesNotExist, msg="User Instructor last name does not exist"):
            self.instructor.getLastName()

    def testBadFirstName(self):
        instructor_first_name = Instructor.objects.filter(first_name="John")
        with self.assertRaises(ValueError, msg="Bad First Name"):
            self.assertEqual(instructor_first_name, self.instructor.getFirstName(),
                             msg='User Instructor First name was not correctly '
                                 'set up '
                                 'in '
                                 'database')
            # self.assertEqual(ta_first_name, self.ta.getFirstName())

    def testBadLastName(self):
        instructor_first_name = Instructor.objects.filter(last_name="Doe")
        with self.assertRaises(ValueError, msg="Bad First Name"):
            self.assertEqual(instructor_first_name, self.instructor.getLastName(), msg='User Instructor Last name was '
                                                                                       'not correctly '
                                                                                       'set up in '
                                                                                       'database')

    def testBadFirstNameType(self):
        with self.assertRaises(TypeError, msg="incorrect user type"):
            self.assertIsInstance(self.instructor.getFirstName(), str, msg="Incorrect User Instructor first name type")

    def testBadLastNameType(self):
        with self.assertRaises(TypeError, msg="incorrect user type"):
            self.assertIsInstance(self.instructor.getLastName(), str, msg="Incorrect User Instructor last name type")


class TestSetInstructorName(TestCase):

    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testNoArgsFirstName(self):
        with self.assertRaises(TypeError, msg="No Arguments provided for function requiring params"):
            self.instructor.setFirstName()

    def testNoArgsLastName(self):
        with self.assertRaises(TypeError, msg="No Arguments provided for function requiring params"):
            self.instructor.setLastName()

    def testSetFirstNameCorrectType(self):
        first_name = Instructor.objects.filter(first_name="John")

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
        last_name = Instructor.objects.filter(last_name="Doe")

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
        first_name = Instructor.objects.filter(first_name="John")
        first_new_name = self.instructor.setFirstName("Steven")
        with self.assertRaises(ValueError, msg="Bad First Name"):
            self.assertEqual(1, self.instructor.setFirstName(first_new_name),
                             msg='First name was not correctly set up in '
                                 'database')
            self.assertEqual(first_name, self.instructor.getFirstName(), msg='Incorrect First Name')

    def testSetBadLastName(self):
        last_name = Instructor.objects.filter(last_name="Doe")
        first_new_name = self.instructor.setLastName("Adams")
        with self.assertRaises(ValueError, msg="Bad Last Name"):
            self.assertEqual(1, self.instructor.setFirstName(first_new_name),
                             msg='Last name was not correctly set up in '
                                 'database')
            self.assertEqual(last_name, self.instructor.getFirstName(), msg='Incorrect Last Name')


class TestGetInstructorPhoneNumber(TestCase):
    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testPhoneNumberExists(self):
        with self.assertRaises(ObjectDoesNotExist, msg="User instructor phone number does not exist"):
            self.instructor.getPhoneNumber()

    def testPhoneNumberCorrectType(self):
        with self.assertRaises(TypeError, msg="incorrect User instructor phone number type"):
            self.assertIsInstance(self.instructor.getPhoneNumber(), int, msg="Incorrect type")

    def testBadPhoneNumberLength(self):
        with self.assertRaises(ValueError, msg="incorrect length for User instructor phone number"):
            self.assertEqual(10, len(self.instructor.getPhoneNumber()))

    def testBadPhoneNumber(self):
        phone_number = Instructor.objects.filter(phone_number=4149818000)
        with self.assertRaises(ValueError, msg="incorrect number"):
            self.assertEqual(phone_number, self.instructor.getPhoneNumber())


class TestSetInstructorPhoneNumber(TestCase):
    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testNoArgs(self):
        with self.assertRaises(TypeError, msg="No Arguments provided for function requiring params"):
            self.instructor.setPhoneNumber()

    def testSetPhoneNumberCorrectType(self):
        phone_number = Instructor.objects.filter(phone_number=4149818000)
        with self.assertRaises(TypeError, msg="Bad Phone Type"):
            self.assertIsInstance(self.instructor.setPhoneNumber(phone_number), int, msg='Only integers allowed')

    def testSetBadPhoneNumber(self):
        phone_number = Instructor.objects.filter(phone_number=4149818000)
        first_new_name = self.instructor.setPhoneNumber(4149818222)
        with self.assertRaises(ValueError, msg="Bad Phone Number"):
            self.assertEqual(1, self.instructor.setFirstName(first_new_name),
                             msg='Phone number was not correctly set up in '
                                 'database')
            self.assertEqual(phone_number, self.instructor.getPhoneNumber(), msg='Incorrect Phone number')


class TestGetInstructorHomeAddressTests(TestCase):
    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testHomeAddressExists(self):
        with self.assertRaises(ObjectDoesNotExist, msg="User instructor home address does not exist"):
            self.instructor.getHomeAddress()

    def testHomeAddressType(self):
        with self.assertRaises(TypeError, msg="incorrect User instructor home address Type"):
            self.assertIsInstance(self.instructor.getHomeAddress(), str, msg="Incorrect type")

    def testBadHomeAddress(self):
        home_address = Instructor.objects.filter(home_address="2513 N Farewell Ave")
        with self.assertRaises(ValueError, msg="incorrect user instructor home address"):
            self.assertEqual(home_address, self.instructor.getHomeAddress())


class TestSetInstructorHomeAddressTests(TestCase):
    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testNoArgs(self):
        with self.assertRaises(TypeError, msg="No Arguments provided for function requiring params"):
            self.instructor.setPhoneNumber()

    def testSetHomeAddressType(self):
        home_address = Instructor.objects.filter(home_address='2513 N Farewell Ave')
        with self.assertRaises(TypeError, msg="Bad Home Address Type"):
            self.assertIsInstance(self.instructor.setHomeAddress(home_address), int, msg='Only integers allowed')

    def testSetBadHomeNumber(self):
        home_address = Instructor.objects.filter(home_address='12513 N Farewell Ave')
        new_home_address = self.instructor.setHomeAddress('2513 N Farewell Ave')
        with self.assertRaises(ValueError, msg="Bad Phone Number"):
            self.assertEqual(1, self.instructor.setHomeAddress(new_home_address),
                             msg='Phone Number was not correctly set up '
                                 'in '
                                 'database')
            self.assertEqual(home_address, self.instructor.getHomeAddress(),
                             msg='Incorrect User instructor Phone Number')


class TestGetInstructorUserType(TestCase):
    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testUserTypeExists(self):
        with self.assertRaises(ObjectDoesNotExist, msg="User Type does not exist"):
            self.instructor.getUserType()

    def testUserType(self):
        with self.assertRaises(TypeError, msg="incorrect user type"):
            self.assertIsInstance(self.instructor.getUserType(), str, msg="Incorrect type")


class TestSetInstructorUserType(TestCase):
    def setUp(self) -> None:
        Instructor.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                                  phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='Instructor',
                                  email='johnDoe@aol.com')
        user_obj = Instructor.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj.account_ID)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testNoArgs(self):
        with self.assertRaises(TypeError, msg="No Arguments provided for function requiring params"):
            self.instructor.setPhoneNumber()

    def testSetUserCorrectType(self):
        user_type = Instructor.objects.filter(user_type='instructor')
        with self.assertRaises(TypeError, msg="Bad User Type"):
            self.assertIsInstance(self.instructor.setUserType(user_type), str, msg='This is a Instructor object')

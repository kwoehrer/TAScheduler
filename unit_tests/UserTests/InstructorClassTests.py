from django.test import TestCase
from app.models import Instructor, User
from classes.Users.users import InstructorUser


# New Branch
class TestGetIDInstructor(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password="password", first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj)
        self.instructor: InstructorUser = InstructorUser(user_model)

    def testID(self):
        account_id = self.instructor.getID()
        self.assertEqual(self.instructor.getID(), account_id,
                         msg="Instructor User ID was not correctly "
                             "set up when creating a Instructor")

    def testIDInstance(self):
        self.assertIsInstance(self.instructor.getID(), int, msg="Correct Type was not stored in Database")


class TestGetInstructorFirstName(TestCase):

    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testFirstNameExists(self):
        name = self.instructor.getFirstName()
        self.assertNotEqual(name, None, msg="A first name exists")

    def testFirstName(self):
        first_name = self.instructor.getFirstName()
        self.assertEqual(first_name, 'John',
                         msg="Incorrect First Name when setting up a instructor")

    def testFirstNameTypeInstance(self):
        self.assertIsInstance(self.instructor.getLastName(), str, msg="Correct Type was not stored in Database")


class TestSetInstructorFirstName(TestCase):

    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testSetFirstName(self):
        new_first_name = "Steven"

        self.instructor.setFirstName(new_first_name)

        # Retrieve the updated data from the database
        updated_instructor = User.objects.get(account_ID=self.instructor.getID())

        # Verify that the changes were stored in the database
        self.assertEqual(updated_instructor.first_name, new_first_name, msg="Change was not reflected in Database")


class TestGetInstructorLastName(TestCase):

    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password="password", first_name="John", last_name="Doe",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testLastName(self):
        name = self.instructor.getLastName()
        self.assertEqual(name, 'Doe', msg="Incorrect Last Name when setting up a instructor")

    def testLastNameExists(self):
        last_name = self.instructor.getLastName()
        self.assertNotEqual(last_name, None, msg="A last name exists")

    def testLastNameTypeInstance(self):
        self.assertIsInstance(self.instructor.getLastName(), str, msg="Correct Type was not stored in Database")


class TestSetInstructorLastName(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password="password", first_name="John", last_name="Doe",
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testNoArg(self):
        with self.assertRaises(TypeError, msg="Add ta - more than one arg is required"):
            self.instructor.setLastName()

    def testSetLastName(self):
        new_last_name = "Adams"

        self.instructor.setLastName(new_last_name)

        # Retrieve the updated data from the database
        updated_instructor = User.objects.get(account_ID=self.instructor.getID())

        # Verify that the changes were stored in the database
        self.assertEqual(updated_instructor.last_name, new_last_name, msg="Change was not reflected in Database")


class TestGetInstructorPhoneNumber(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testPhoneNumberExists(self):
        phone_number = self.instructor.getPhoneNumber()
        self.assertNotEqual(phone_number, None, msg="A phone number exists")

    def testPhoneNumber(self):
        phone_number = self.instructor.getPhoneNumber()
        self.assertEqual(phone_number, '4149818000',
                         "Phone was not set correctly when creating a Instructor.")

    def testPhoneNumberTypeInstance(self):
        self.assertIsInstance(self.instructor.getPhoneNumber(), str, msg="Invalid Phone Number Type stored in Database")

    def testPhoneNumberLength(self):
        phone_number_length = len(self.instructor.getPhoneNumber())
        self.assertEqual(phone_number_length, 10, msg="Invalid Phone Number Length")


class TestSetInstructorPhoneNumber(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testNoArg(self):
        with self.assertRaises(TypeError, msg="more than one arg is required"):
            self.instructor.setPhoneNumber()

    def testSetPhoneNumber(self):
        # Set up the test data
        new_phone_number = "4149828002"

        # Exercise the system
        self.instructor.setPhoneNumber(new_phone_number)

        # Retrieve the updated data from the database
        updated_instructor = User.objects.get(account_ID=self.instructor.getID())

        # Verify that the changes were stored in the database
        self.assertEqual(updated_instructor.phone_number, new_phone_number, msg="Change was not reflected in Database")


class TestGetInstructorAddress(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj)
        self.instructor: InstructorUser = InstructorUser(user_model)

    def testHomeAddressExists(self):
        home_address = self.instructor.getHomeAddress()
        self.assertNotEqual(home_address, None, msg="A home address exists")

    def testHomeAddress(self):
        home_address = self.instructor.getHomeAddress()
        self.assertEqual(home_address, "2513 N Farewell Ave",
                         msg="Home Address was not set correctly when creating a Admin.")

    def testHomeAddressTypeInstance(self):
        self.assertIsInstance(self.instructor.getHomeAddress(), str, msg="Incorrect type")


class TestSetInstructorHomeAddress(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj)
        self.instructor: InstructorUser = InstructorUser(user_model)

    def testNoArg(self):
        with self.assertRaises(TypeError, msg="more than one arg is required"):
            self.instructor.setHomeAddress()

    def testSetHomeAddress(self):
        new_home_address = "2514 N Brady Ave"
        self.instructor.setHomeAddress(new_home_address)
        # Retrieve the updated data from the database
        updated_instructor = User.objects.get(account_ID=self.instructor.getID())

        # Verify that the changes were stored in the database
        self.assertEqual(updated_instructor.home_address, new_home_address, msg="Change was not reflected in Database")


class TestGetInstructorUserType(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testUserType(self):
        user_type_admin = self.instructor.getUserType()
        self.assertEqual(user_type_admin, "Instructor",
                         msg="User type was not correctly set up when creating an Instructor")


class TestSetInstructorUserType(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testNoArg(self):
        with self.assertRaises(TypeError, msg="more than one arg is required"):
            self.instructor.setUserType()

    def testSetUserType(self):
        new_type = "Instructor"
        self.instructor.setUserType(new_type)
        # Retrieve the updated data from the database
        updated_instructor = User.objects.get(account_ID=self.instructor.getID())

        # Verify that the changes were stored in the database
        self.assertEqual(updated_instructor.user_type, new_type, msg="Change was not reflected in Database")


class TestGetInstructorUserPassword(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testInstructorPasswordExists(self):
        password = self.instructor.getPassword()
        self.assertNotEqual(password, None, msg="A password cannot exist when the field is not "
                                                "declared")

    def testInstructorPassword(self):
        password = self.instructor.getPassword()
        self.assertEqual(password, "password", msg="Password was not set correctly when creating a "
                                                   "Instructor.")

    def testInstructorPasswordTypeInstance(self):
        password = self.instructor.getPassword()
        self.assertIsInstance(password, str, msg="Incorrect Password Type in Database")


class TestSetInstructorUserPassword(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave', user_type='Instructor',
                            email='johnDoe@aol.com')
        user_obj = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_obj)

        self.instructor: InstructorUser = InstructorUser(user_model)

    def testNoArg(self):
        with self.assertRaises(TypeError, msg="more than one arg is required"):
            self.instructor.setPassword()

    def testSetUserPassword(self):
        new_password = 'new_password'
        self.instructor.setPassword(new_password)
        # Retrieve the updated data from the database
        updated_instructor = User.objects.get(account_ID=self.instructor.getID())

        # Verify that the changes were stored in the database
        self.assertEqual(updated_instructor.password, new_password, msg="Change was not reflected in Database")

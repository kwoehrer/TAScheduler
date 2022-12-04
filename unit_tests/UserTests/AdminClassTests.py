from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from app.models import Admin
from classes.Users.users import AdminUser


class GetNameTestAdmin(TestCase):

    def setUp(self) -> None:
        Admin.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                             phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='Admin',
                             email='johnDoe@aol.com')
        user_obj = Admin.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj.account_ID)

        self.admin: AdminUser = AdminUser(user_model)

    def testFirstNameExists(self):
        with self.assertRaises(ObjectDoesNotExist, msg="User Admin first name does not exist"):
            self.admin.getFirstName()

    def testLastNameExists(self):
        with self.assertRaises(ObjectDoesNotExist, msg="User Admin last name does not exist"):
            self.admin.getLastName()

    def testBadFirstName(self):
        admin_first_name = Admin.objects.filter(first_name="John")
        with self.assertRaises(ValueError, msg="Bad First Name"):
            self.assertEqual(admin_first_name, self.admin.getFirstName(),
                             msg='User Admin First name was not correctly set up '
                                 'in '
                                 'database')
            # self.assertEqual(admin_first_name, self.admin.getFirstName())

    def testBadLastName(self):
        admin_first_name = Admin.objects.filter(last_name="Doe")
        with self.assertRaises(ValueError, msg="Bad First Name"):
            self.assertEqual(admin_first_name, self.admin.getLastName(),
                             msg='User Admin Last name was not correctly set up in '
                                 'database')

    def testBadFirstNameType(self):
        with self.assertRaises(TypeError, msg="incorrect user type"):
            self.assertIsInstance(self.admin.getFirstName(), str, msg="Incorrect User Admin first name type")

    def testBadLastNameType(self):
        with self.assertRaises(TypeError, msg="incorrect user type"):
            self.assertIsInstance(self.admin.getLastName(), str, msg="Incorrect User Admin last name type")


class SetNameTestAdmin(TestCase):

    def setUp(self) -> None:
        Admin.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                             phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='Admin',
                             email='johnDoe@aol.com')
        user_obj = Admin.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj.account_ID)

        self.admin: AdminUser = AdminUser(user_model)

    def testNoArgsFirstName(self):
        with self.assertRaises(TypeError, msg="No Arguments provided for function requiring params"):
            self.admin.setFirstName()

    def testNoArgsLastName(self):
        with self.assertRaises(TypeError, msg="No Arguments provided for function requiring params"):
            self.admin.setLastName()

    def testSetFirstNameCorrectType(self):
        first_name = Admin.objects.filter(first_name="John")

        # with self.assertRaises(ValueError, msg="Bad First Name"):
        #    self.assertEqual(1, self.admin.setFirstName(first_name), msg='First name was not correctly set up in '
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
        last_name = Admin.objects.filter(last_name="Doe")

        # with self.assertRaises(ValueError, msg="Bad Last Name"):
        #    self.assertEqual(1, self.admin.setFirstName(last_name), msg='Last name was not correctly set up in '
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
        first_name = Admin.objects.filter(first_name="John")
        first_new_name = self.admin.setFirstName("Steven")
        with self.assertRaises(ValueError, msg="Bad First Name"):
            self.assertEqual(1, self.admin.setFirstName(first_new_name), msg='First name was not correctly set up in '
                                                                             'database')
            self.assertEqual(first_name, self.admin.getFirstName(), msg='Incorrect First Name')

    def testSetBadLastName(self):
        last_name = Admin.objects.filter(last_name="Doe")
        first_new_name = self.admin.setLastName("Adams")
        with self.assertRaises(ValueError, msg="Bad Last Name"):
            self.assertEqual(1, self.admin.setFirstName(first_new_name), msg='Last name was not correctly set up in '
                                                                             'daJohn_Doebase')
            self.assertEqual(last_name, self.admin.getFirstName(), msg='Incorrect Last Name')


class GetPhoneNumberTests(TestCase):
    def setUp(self) -> None:
        Admin.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                             phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='Admin',
                             email='johnDoe@aol.com')
        user_obj = Admin.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj.account_ID)

        self.admin: AdminUser = AdminUser(user_model)

    def testPhoneNumberExists(self):
        with self.assertRaises(ObjectDoesNotExist, msg="User Admin phone number does not exist"):
            self.admin.getPhoneNumber()

    def testPhoneNumberCorrectType(self):
        with self.assertRaises(TypeError, msg="incorrect User Admin phone number type"):
            self.assertIsInstance(self.admin.getPhoneNumber(), int, msg="Incorrect type")

    def testBadPhoneNumberLength(self):
        with self.assertRaises(ValueError, msg="incorrect length for User Admin phone number"):
            self.assertEqual(10, len(self.admin.getPhoneNumber()))

    def testBadPhoneNumber(self):
        phone_number = Admin.objects.filter(phone_number=4149818000)
        with self.assertRaises(ValueError, msg="incorrect number"):
            self.assertEqual(phone_number, self.admin.getPhoneNumber())


class SetPhoneNumberTests(TestCase):
    def setUp(self) -> None:
        Admin.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                             phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='Admin',
                             email='johnDoe@aol.com')
        user_obj = Admin.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj.account_ID)

        self.admin: AdminUser = AdminUser(user_model)

    def testNoArgs(self):
        with self.assertRaises(TypeError, msg="No Arguments provided for function requiring params"):
            self.admin.setPhoneNumber()

    def testSetPhoneNumberCorrectType(self):
        phone_number = Admin.objects.filter(phone_number=4149818000)
        with self.assertRaises(TypeError, msg="Bad Phone Type"):
            self.assertIsInstance(self.admin.setPhoneNumber(phone_number), int, msg='Only integers allowed')

    def testSetBadPhoneNumber(self):
        phone_number = Admin.objects.filter(phone_number=4149818000)
        first_new_name = self.admin.setPhoneNumber(4149818222)
        with self.assertRaises(ValueError, msg="Bad Phone Number"):
            self.assertEqual(1, self.admin.setFirstName(first_new_name), msg='Phone number was not correctly set up in '
                                                                             'database')
            self.assertEqual(phone_number, self.admin.getPhoneNumber(), msg='Incorrect Phone number')


class GetAddressTests(TestCase):
    def setUp(self) -> None:
        Admin.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                             phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='Admin',
                             email='johnDoe@aol.com')
        user_obj = Admin.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj.account_ID)

        self.admin: AdminUser = AdminUser(user_model)

    def testHomeAddressExists(self):
        with self.assertRaises(ObjectDoesNotExist, msg="User Admin home address does not exist"):
            self.admin.getHomeAddress()

    def testHomeAddressType(self):
        with self.assertRaises(TypeError, msg="incorrect User Admin home address Type"):
            self.assertIsInstance(self.admin.getHomeAddress(), str, msg="Incorrect type")

    def testBadHomeAddress(self):
        home_address = Admin.objects.filter(home_address="2513 N Farewell Ave")
        with self.assertRaises(ValueError, msg="incorrect user Admin home address"):
            self.assertEqual(home_address, self.admin.getHomeAddress())


class SetHomeAddressTests(TestCase):
    def setUp(self) -> None:
        Admin.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                             phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='Admin',
                             email='johnDoe@aol.com')
        user_obj = Admin.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj.account_ID)

        self.admin: AdminUser = AdminUser(user_model)

    def testNoArgs(self):
        with self.assertRaises(TypeError, msg="No Arguments provided for function requiring params"):
            self.admin.setPhoneNumber()

    def testSetHomeAddressType(self):
        home_address = Admin.objects.filter(home_address='2513 N Farewell Ave')
        with self.assertRaises(TypeError, msg="Bad Home Address Type"):
            self.assertIsInstance(self.admin.setHomeAddress(home_address), int, msg='Only integers allowed')

    def testSetBadHomeNumber(self):
        home_address = Admin.objects.filter(home_address='12513 N Farewell Ave')
        new_home_address = self.admin.setHomeAddress('2513 N Farewell Ave')
        with self.assertRaises(ValueError, msg="Bad Phone Number"):
            self.assertEqual(1, self.admin.setHomeAddress(new_home_address),
                             msg='Phone Number was not correctly set up '
                                 'in '
                                 'database')
            self.assertEqual(home_address, self.admin.getHomeAddress(), msg='Incorrect User Admin Phone Number')


class GetUserType(TestCase):
    def setUp(self) -> None:
        Admin.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                             phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='Admin',
                             email='johnDoe@aol.com')
        user_obj = Admin.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj.account_ID)

        self.admin: AdminUser = AdminUser(user_model)

    def testUserTypeExists(self):
        with self.assertRaises(ObjectDoesNotExist, msg="User Type does not exist"):
            self.admin.getUserType()

    def testUserType(self):
        with self.assertRaises(TypeError, msg="incorrect user type"):
            self.assertIsInstance(self.admin.getUserType(), str, msg="Incorrect type")


class SetUserType(TestCase):
    def setUp(self) -> None:
        Admin.objects.create(username='John_Doe', password='password', first_name="John", last_name='Doe',
                             phone_number=4149818000, home_address='2513 N Farewell Ave', user_type='Admin',
                             email='johnDoe@aol.com')
        user_obj = Admin.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_obj.account_ID)

        self.admin: AdminUser = AdminUser(user_model)

    def testNoArgs(self):
        with self.assertRaises(TypeError, msg="No Arguments provided for function requiring params"):
            self.admin.setPhoneNumber()

    def testSetUserCorrectType(self):
        user_type = Admin.objects.filter(user_type='Admin')
        with self.assertRaises(TypeError, msg="Bad User Type"):
            self.assertIsInstance(self.admin.setUserType(user_type), str, msg='This is a Admin object')

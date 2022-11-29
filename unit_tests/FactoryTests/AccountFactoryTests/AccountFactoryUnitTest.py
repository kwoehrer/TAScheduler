import unittest


class TestCreateCourse(unittest.TestCase):

    def setUp(self) -> None:
        acc_fact :AbstractAccountFactory = AccountFactory()
    def test_no_arg(self):
        with self.assertRaises(TypeError, msg="Three Argument failed to throw value error"):
            a = self.acc_fact

    def test_only_course_attributes(self):
        with self.assertRaises(TypeError, msg="Three Argument failed to throw value error"):
            a = AccountFactory()

    def test_only_admin_user(self):
        self.assertEqual(True, False)  # add assertion here

    def test_good_attribute_TA_user(self):
        self.assertEqual(True, False)  # add assertion here

    def test_good_attribute_Instructor_user(self):
        self.assertEqual(True, False)  # add assertion her

    def test_good_attribute_admin_user(self):
        self.assertEqual(True, False)  # add assertion her

    def test_existing_username(self):
        self.assertEqual(True, False)  # add assertion her
    def test_existing_email(self):
        self.assertEqual(True, False)  # add assertion her

class TestDeleteCourse(unittest.TestCase):
    pass


class TestEditCourse(unittest.TestCase):
    pass


class TestDeleteCourse(unittest.TestCase):
    pass


class TestGetAllCourses(unittest.TestCase):
    pass


class TestFilterCourses(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()

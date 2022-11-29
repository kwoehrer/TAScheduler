from django.test import TestCase
from app.models import Course, User, Section
from classes.Courses.CoursesClass import ConcreteCourse, AbstractCourse
from classes.Sections.SectionClass import AbstractSection, ConcreteSection


class TestCourseCredits(TestCase):

    def setUp(self) -> None:

        Course.objects.create(name="course1", semester="Spring", year="2022",
                              description="first course", credits="0")
        f_course_model = Course.objects.filter(name='course1')[0]
        self.first_course_model = Course.objects.create(course_ID=f_course_model.course_ID)

        Course.objects.create(name="course2", semester="Spring", year="2022",
                              description="second course", credits="1")
        s_course_model = Course.objects.filter(name='course2')[0]
        self.second_course_model = Course.objects.create(course_ID=s_course_model.course_ID)

        Course.objects.create(name="course3", semester="Spring", year="2022",
                              description="second course", credits="4")
        t_course_model = Course.objects.filter(name='course3')[0]
        self.third_course_model = Course.objects.create(course_ID=t_course_model.course_ID)


        self.course: AbstractCourse = ConcreteCourse()

    def course_credits_less(self):
        with self.assertRaises(ValueError, msg="Course credits should be bigger than 0"):
            self.course.get_credits()




class TestAddInstructor(TestCase):

    def setUp(self) -> None:
        self.course: AbstractCourse = ConcreteCourse()

        Course.objects.create(name="course1", semester="Spring", year="2022",
                              description="first course", credits="3")
        f_course_model = Course.objects.filter(name='course1')[0]
        self.first_course_model = Course.objects.create(course_ID=f_course_model.course_ID)

        Course.objects.create(name="course2", semester="Spring", year="2022",
                              description="second course", credits="3")
        s_course_model = Course.objects.filter(name='course2')[0]
        self.second_course_model = Course.objects.create(course_ID=s_course_model.course_ID)

        User.objects.create(email="Inst1@gmail.com", username="Inst1", password="inst1",
                            first_name="first", last_name="instructor", phone_number="123", home_address="address",
                            user_type="Instructor")
        instr_user_model = User.objects.filter(username='Inst1')[0]
        self.instr_model = User.objects.create(account_ID=instr_user_model.account_ID)

        User.objects.create(email="Ta1@gmail.com", username="Ta1", password="ta1",
                            first_name="first", last_name="ta", phone_number="123", home_address="address",
                            user_type="TA")
        ta_user_model = User.objects.filter(username='Ta1')[0]
        self.ta_model = User.objects.create(account_ID=ta_user_model.account_ID)

        User.objects.create(email="Ta2@gmail.com", username="Ta2", password="ta2",
                            first_name="first", last_name="ta", phone_number="123", home_address="address",
                            user_type="TA")
        s_ta_user_model = User.objects.filter(username='Ta2')[0]
        self.second_ta_model = User.objects.create(account_ID=s_ta_user_model.account_ID)

    def add_Instr_no_Arg(self):
        with self.assertRaises(TypeError, msg="More than zero argument is required"):
            self.course.add_instructor()

    def add_Instr_more_arg(self):
        with self.assertRaises(TypeError, msg="add instr - Too much arg was added"):
            self.course.add_instructor(self.instr_model, self.ta_model)

    def add_Instr_wrong_User(self):
        with self.assertRaises(TypeError, msg="This user is not a instructor"):
            self.course.add_instructor(self.ta_model)

class TestAddTa(TestCase):

    def setUp(self) -> None:
        self.course: AbstractCourse = ConcreteCourse()

        Course.objects.create(name="course1", semester="Spring", year="2022",
                              description="first course", credits="3")
        f_course_model = Course.objects.filter(name='course1')[0]
        self.first_course_model = Course.objects.create(course_ID=f_course_model.course_ID)

        Course.objects.create(name="course2", semester="Spring", year="2022",
                              description="second course", credits="3")
        s_course_model = Course.objects.filter(name='course2')[0]
        self.second_course_model = Course.objects.create(course_ID=s_course_model.course_ID)

        User.objects.create(email="Inst1@gmail.com", username="Inst1", password="inst1",
                            first_name="first", last_name="instructor", phone_number="123", home_address="address",
                            user_type="Instructor")
        instr_user_model = User.objects.filter(username='Inst1')[0]
        self.instr_model = User.objects.create(account_ID=instr_user_model.account_ID)

        User.objects.create(email="Ta1@gmail.com", username="Ta1", password="ta1",
                            first_name="first", last_name="ta", phone_number="123", home_address="address",
                            user_type="TA")
        ta_user_model = User.objects.filter(username='Ta1')[0]
        self.ta_model = User.objects.create(account_ID=ta_user_model.account_ID)

        User.objects.create(email="Ta2@gmail.com", username="Ta2", password="ta2",
                            first_name="first", last_name="ta", phone_number="123", home_address="address",
                            user_type="TA")
        s_ta_user_model = User.objects.filter(username='Ta2')[0]
        self.second_ta_model = User.objects.create(account_ID=s_ta_user_model.account_ID)

    def add_ta_no_arg(self):
        with self.assertRaises(TypeError, msg="Add ta - more than one arg is required"):
            self.course.add_ta()

    def add_ta_more_arg(self):
        with self.assertRaises(TypeError, msg="Add ta - Too much arg was added"):
            self.course.add_ta(self.ta_model, self.second_ta_model)

    def add_ta_wrong_user(self):
        with self.assertRaises(TypeError, msg="Add ta - this user is not a TA"):
            self.course.add_ta(self.instr_model)

class TestremoveTA(TestCase):

    def setUp(self) -> None:
        self.course: AbstractCourse = ConcreteCourse()

        Course.objects.create(name="course1", semester="Spring", year="2022",
                              description="first course", credits="3")
        f_course_model = Course.objects.filter(name='course1')[0]
        self.first_course_model = Course.objects.create(course_ID=f_course_model.course_ID)

        User.objects.create(email="Ta1@gmail.com", username="Ta1", password="ta1",
                            first_name="first", last_name="ta", phone_number="123", home_address="address",
                            user_type="TA")
        ta_user_model = User.objects.filter(username='Ta1')[0]
        self.ta_model = User.objects.create(account_ID=ta_user_model.account_ID)

        User.objects.create(email="Ta2@gmail.com", username="Ta2", password="ta2",
                            first_name="first", last_name="ta", phone_number="123", home_address="address",
                            user_type="TA")
        s_ta_user_model = User.objects.filter(username='Ta2')[0]
        self.second_ta_model = User.objects.create(account_ID=s_ta_user_model.account_ID)

    def remove_ta_no_arg(self):
        with self.assertRaises(TypeError, msg="Remove ta - No arg was added"):
            self.course.remove_ta()

    def remove_ta_more_arg(self):
        with self.assertRaises(TypeError, msg="Remove ta - Too much arg was added"):
            self.course.remove_ta(self.ta_model, self.second_ta_model)

    def remove_ta_no_user(self):
        self.course.add_ta(self.ta_model)
        with self.assertRaises(TypeError, msg="Remove ta - no such TA was found"):
            self.course.remove_ta(self.second_ta_model)


class TestaddSection(TestCase):

    def setUp(self) -> None:
        self.section: AbstractSection = ConcreteSection()
        Section.objects.create()










from django.contrib.auth.models import AbstractUser
from django.test import TestCase
from app.models import Course, User, Section
from classes.Courses.CoursesClass import ConcreteCourse, AbstractCourse
from classes.Sections.SectionClass import AbstractSection, ConcreteSection


class TestAddInstructor(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022",
                                             description="first course", credits="3")
        self.course: AbstractCourse = ConcreteCourse(course_model)

        s_course_model = Course.objects.create(name="course2", semester="Spring", year="2022",
                                               description="second course", credits="3")
        self.course2: AbstractCourse = ConcreteCourse(s_course_model)

        inst_model = User.objects.create(email="Inst1@gmail.com", username="Inst1", password="inst1",
                                         first_name="first", last_name="instructor", phone_number="123",
                                         home_address="address",
                                         user_type="Instructor")
        self.inst: AbstractUser = ConcreteUser(inst_model)

        ta_model = User.objects.create(email="Ta1@gmail.com", username="Ta1", password="ta1",
                                       first_name="first", last_name="ta", phone_number="123", home_address="address",
                                       user_type="TA")
        self.ta: AbstractUser = ConcreteUser(ta_model)

        ta2_model = User.objects.create(email="Ta2@gmail.com", username="Ta2", password="ta2",
                                        first_name="first", last_name="ta", phone_number="123", home_address="address",
                                        user_type="TA")
        self.ta2: AbstractUser = ConcreteUser(ta2_model)

    def add_Instr_no_Arg(self):
        with self.assertRaises(TypeError, msg="More than zero argument is required"):
            self.course.add_instructor()

    def add_Instr_more_arg(self):
        with self.assertRaises(TypeError, msg="add instr - Too much arg was added"):
            self.course.add_instructor(self.inst, self.ta)

    def add_Instr_wrong_User(self):
        with self.assertRaises(TypeError, msg="This user is not a instructor"):
            self.course.add_instructor(self.ta)


class TestAddTa(TestCase):

    def setUp(self) -> None:
        f_course_model = Course.objects.create(name="course1", semester="Spring", year="2022",
                                               description="first course", credits="3")
        self.course: AbstractCourse = ConcreteCourse(f_course_model)

        s_course_model = Course.objects.create(name="course2", semester="Spring", year="2022",
                                               description="second course", credits="3")
        self.course: AbstractCourse = ConcreteCourse(s_course_model)

        inst_model = User.objects.create(email="Inst1@gmail.com", username="Inst1", password="inst1",
                                         first_name="first", last_name="instructor", phone_number="123",
                                         home_address="address",
                                         user_type="Instructor")
        self.inst: AbstractUser = ConcreteUser(inst_model)

        ta_model = User.objects.create(email="Ta1@gmail.com", username="Ta1", password="ta1",
                                       first_name="first", last_name="ta", phone_number="123", home_address="address",
                                       user_type="TA")
        self.ta: AbstractUser = ConcreteUser(ta_model)

        ta2_model = User.objects.create(email="Ta2@gmail.com", username="Ta2", password="ta2",
                                        first_name="first", last_name="ta", phone_number="123", home_address="address",
                                        user_type="TA")
        self.ta2: AbstractUser = ConcreteUser(ta2_model)

    def add_ta_no_arg(self):
        with self.assertRaises(TypeError, msg="Add ta - more than one arg is required"):
            self.course.add_ta()

    def add_ta_more_arg(self):
        with self.assertRaises(TypeError, msg="Add ta - Too much arg was added"):
            self.course.add_ta(self.ta, self.ta2)

    def add_ta_wrong_user(self):
        with self.assertRaises(TypeError, msg="Add ta - this user is not a TA"):
            self.course.add_ta(self.inst)


class TestremoveTA(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022",
                                             description="first course", credits="3")
        self.course: AbstractCourse = ConcreteCourse(course_model)

        ta_model = User.objects.create(email="Ta1@gmail.com", username="Ta1", password="ta1",
                                       first_name="first", last_name="ta", phone_number="123", home_address="address",
                                       user_type="TA")
        self.ta: AbstractUser = ConcreteUser(ta_model)

        s_ta_model = User.objects.create(email="Ta2@gmail.com", username="Ta2", password="ta2",
                                         first_name="first", last_name="ta", phone_number="123", home_address="address",
                                         user_type="TA")
        self.ta2: AbstractUser = ConcreteUser(s_ta_model)

    def remove_ta_no_arg(self):
        with self.assertRaises(TypeError, msg="Remove ta - No arg was added"):
            self.course.remove_ta()

    def remove_ta_more_arg(self):
        with self.assertRaises(TypeError, msg="Remove ta - Too much arg was added"):
            self.course.remove_ta(self.ta, self.ta2)

    def remove_ta_no_user(self):
        self.course.add_ta(self.ta)
        with self.assertRaises(TypeError, msg="Remove ta - no such TA was found"):
            self.course.remove_ta(self.ta2)


class TestaddSection(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022", description="test",
                                             credits="3")
        self.course: AbstractCourse = ConcreteCourse(course_model)

        section_model = Section.objects.create(course_model.course_ID, section_num=100, MeetingTime="9:00")
        self.section: AbstractSection = ConcreteSection(section_model)

    def add_section_no_arg(self):
        with self.assertRaises(TypeError, msg="add_section - More than zero arg is required"):
            self.course.add_section()

    def add_secion_one_arg(self):
        with self.assertRaises(TypeError, msg="add_section - More than one arg is required"):
            self.course.add_section(self.section.getTA())

    def add_secion_two_arg(self):
        with self.assertRaises(TypeError, msg="add_section - More than two arg is required"):
            self.course.add_section(self.section.getTA(), self.section.getSectionNumber())

    def add_section_more_arg(self):
        with self.assertRaises(TypeError, msg="add_section - Too many arg was added"):
            self.course.add_section(self.section.getTA(), self.section.getSectionNumber(), self.section.getMeetTime(),
                                    self.course.get_course_id)

    def add_section_not_saved(self):
        self.course.add_section(self.section.getTA(), self.section.getSectionNumber(), self.section.getSectionNumber())
        length = len(Section.objects.filter(section_num=100))
        self.assertNotEqual(0, length, msg="Section was not added")


class TestremoveSection(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022", description="test",
                                             credits="3")

        section_model = Section.objects.create(course_model.course_ID, section_num=100, MeetingTime="9:00")

        self.course: AbstractCourse = ConcreteCourse(course_model)
        self.section: AbstractSection = ConcreteSection(section_model)

    def remove_section_no_arg(self):
        with self.assertRaises(TypeError, msg="remove_section - More than zero arg is required"):
            self.course.remove_section()

    def add_section_more_arg(self):
        with self.assertRaises(TypeError, msg="add_section - Too many arg was added"):
            self.course.add_section(self.section, self.course)

    def remove_section_not_deleted(self):
        self.course.remove_section(self.section)
        length = len(Section.objects.filter(section_num=100))
        self.assertEqual(0, length, msg="Section was not deleted, it still exists")

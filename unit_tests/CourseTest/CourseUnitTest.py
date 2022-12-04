from django.test import TestCase
from django.contrib.auth.models import AbstractUser
from app.models import Course, User, Section
from classes.Courses.CoursesClass import ConcreteCourse, AbstractCourse
from classes.Sections.SectionClass import AbstractSection, ConcreteSection


class TestGetCourseId(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022",
                                             description="first course", credits="3")
        self.course = ConcreteCourse(course_model)

    def test_get_id(self):
        id = self.course.get_course_id
        self.assertEqual(self.course.get_course_id, id, msg="Course id is incorrect")


class TestGetCourseName(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name='course1', semester="Spring", year="2022",
                                             description="first course", credits="3")
        self.course = ConcreteCourse(course_model)

        course2_model = Course.objects.create(name=1234, semester="Spring", year="2022",
                                              description="first course", credits="3")
        self.course2: AbstractCourse = ConcreteCourse(course2_model)

    def test_get_correct_name(self):
        name = self.course.get_course_name()
        self.assertEqual(name, 'course1', msg="Course name is incorrect")

    def test_get_int_name(self):
        self.assertRaises(TypeError, self.course2.get_course_name, msg="Course name is integers")


class TestSetCourseName(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022",
                                             description="first course", credits="3")
        self.course = ConcreteCourse(course_model)

    def test_set_correct_name(self):
        self.course.set_course_name('First Course')
        name = self.course.get_course_name()
        self.assertEqual(name, "First Course", msg="Course name was not set correctly")

    def test_set_int_name(self):
        with self.assertRaises(TypeError, msg="The name is not string"):
            self.course.set_course_name(1234)

    def test_set_max_name(self):
        with self.assertRaises(ValueError, msg="The name is too long"):
            self.course.set_course_name("123456789012345678901234567890123")

class TestGetSemester(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Fall", year="2022",
                                             description="first course", credits="3")
        self.course: AbstractCourse = ConcreteCourse(course_model)

        course2_model = Course.objects.create(name="course2", semester=1234, year="2022",
                                              description="first course", credits="3")
        self.course2: AbstractCourse = ConcreteCourse(course2_model)


    def test_get_correct_semester(self):
        self.assertEqual(self.course.get_semester(), "Fall", msg="Semester is incorrect")

    def test_get_int_name(self):
        self.assertRaises(TypeError, self.course2.get_course_name(), msg="Semester is integer")

class TestSetSemester(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022",
                                             description="first course", credits="3")
        self.course: AbstractCourse = ConcreteCourse(course_model)

    def test_set_correct_semester(self):
        self.course.set_semester("Fall")
        self.assertEqual(self.course.get_semester(), "Fall", msg="Semester was not set correctly")

    def test_set_None_name(self):
        with self.assertRaises(ValueError, msg="Course name cannot be none"):
            self.course.set_semester(None)

    def test_set_int_name(self):
        with self.assertRaises(ValueError, msg="Course name cannot be integers"):
            self.course.set_semester(1234)


class TestGetYear(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Fall", year=2022,
                                             description="first course", credits="3")
        self.course: AbstractCourse = ConcreteCourse(course_model)

        course2_model = Course.objects.create(name="course2", semester="Fall", year="2022",
                                              description="first course", credits="3")
        self.course2: AbstractCourse = ConcreteCourse(course2_model)

        course3_model = Course.objects.create(name="course3", semester="Fall", year=2035,
                                             description="first course", credits="3")
        self.course3: AbstractCourse = ConcreteCourse(course3_model)


    def test_get_correct_year(self):
        self.assertEqual(self.course.get_year, 2022, msg="Year is incorrect")

    def test_get_None_name(self):
        self.assertRaises(ValueError, self.course2.get_year, msg="Year is none")

    def test_get_int_name(self):
        self.assertRaises(TypeError, self.course3.get_year, msg="Year is integer")

    def test_get_more_than_10_year(self):
        self.assertRaises(ValueError, self.course4.get_year, msg="Year is more than 10 years after this year")

class TestSetYear(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year=2022,
                                             description="first course", credits="3")
        self.course: AbstractCourse = ConcreteCourse(course_model)

    def set_correct_year(self):
        self.course.set_year(2025)
        self.assertEqual(self.course.get_year, 2025, msg="Course name was not set correctly")

    def set_None_name(self):
        self.course.set_course_name(None)
        self.assertEqual(self.course.get_course_name, 2022, msg="Course name cannot be none")

    def set_int_name(self):
        with self.assertRaises(TypeError, msg="Year is string"):
            self.course.set_course_name("2022")

    def set_max_name(self):
        with self.assertRaises(ValueError, msg="The year is too far in the future"):
            self.course.set_course_name(2200)

class TestGetInstructor(TestCase):

    def setUp(self) -> None:

        course_model = Course.objects.create(name="course1", semester="Spring", year="2022",
                                             description="first course", credits="3")
        self.course: AbstractCourse = ConcreteCourse(course_model)

        inst_model = User.objects.create(email="Inst1@gmail.com", username="Inst1", password="inst1",
                                         first_name="first", last_name="instructor", phone_number="123",
                                         home_address="address",
                                         user_type="Instructor")
        self.inst: AbstractUser = ConcreteUser(inst_model)

    def get_instructor(self):
        self.assertNotEqual(self.course.get_instructor,[], msg="Instructor was not found")


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

class TestGetTa(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022",
                                               description="first course", credits="3")
        self.course: AbstractCourse = ConcreteCourse(course_model)

        ta_model = User.objects.create(email="Ta1@gmail.com", username="Ta1", password="ta1",
                                       first_name="first", last_name="ta", phone_number="123", home_address="address",
                                       user_type="TA")
        self.ta: AbstractUser = ConcreteUser(ta_model)

        section_model = Section.objects.create(course_ID = self.course, section_num = 101, MettingTimes="9:00", ta_account_id=self.ta)
        self.section: AbstractSection = ConcreteSection(section_model)

    def get_correct_ta(self):
        self.assertEqual(self.ta.account_ID, self.section.getTA())



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

class TestGetSection(TestCase):
    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022", description="test",
                                             credits="3")
        self.course: AbstractCourse = ConcreteCourse(course_model)

        section_model = Section.objects.create(course_ID = self.course, section_num=101, MeetingTime="9:00")
        self.section: AbstractSection = ConcreteSection(section_model)

    def get_correct_section(self):
        self.assertEqual(101,self.section.getSectionNumber())



class TestaddSection(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022", description="test",
                                             credits="3")
        self.course: AbstractCourse = ConcreteCourse(course_model)

        section_model = Section.objects.create(course_ID = self.course, section_num=1, MeetingTime="9:00")
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

        section_model = Section.objects.create(course_ID = self.course, section_num=101, MeetingTime="9:00")

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

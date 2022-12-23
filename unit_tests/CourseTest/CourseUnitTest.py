from django.test import TestCase
from django.contrib.auth.models import AbstractUser
from app.models import Course, User, Section, Instructor, TA
from classes.Courses.CoursesClass import ConcreteCourse, AbstractCourse
from classes.Sections.SectionClass import AbstractSection, ConcreteSection
from classes.Users.users import InstructorUser, TAUser


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
        new_course_name = 'First Course'

        self.course.set_course_name(new_course_name)

        # Retrieve the updated data from the database
        updated_course = Course.objects.get(course_ID=self.course.get_course_id())

        # Verify that the changes were stored in the database
        self.assertEqual(updated_course.name, new_course_name, msg="Changes were not correctly added to database")

    def test_set_int_name(self):
        with self.assertRaises(TypeError, msg="The name is not string"):
            self.course.set_course_name(1234)

    def test_set_max_name(self):
        with self.assertRaises(ValueError, msg="The name is too long"):
            self.course.set_course_name("123456789012345678901234567890123")


class TestGetCourseDescription(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022",
                                             description="first", credits="3")
        self.course = ConcreteCourse(course_model)

    def test_get_correct_description(self):
        self.assertEqual(self.course.get_description(), "first", msg="Course description is not correct")


class TestGetCourseDescription(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022",
                                             description="first", credits="3")
        self.course = ConcreteCourse(course_model)

    def test_set_correct_description(self):
        new_description = 'FIRST'

        self.course.set_description(new_description)

        # Retrieve the updated data from the database
        updated_course = Course.objects.get(course_ID=self.course.get_course_id())

        # Verify that the changes were stored in the database
        self.assertEqual(updated_course.description, new_description)


class TestGetCourseCredits(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022",
                                             description="first", credits=3)
        self.course = ConcreteCourse(course_model)

    def test_get_correct_Credits(self):
        self.assertEqual(self.course.get_credits(), 3, msg="Course description is not correct")


class TestSetCourseCredits(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022",
                                             description="first", credits=3)
        self.course = ConcreteCourse(course_model)

    def test_set_correct_Credits(self):
        new_credits = 5

        self.course.set_credits(5)

        # Retrieve the updated data from the database
        updated_course = Course.objects.get(course_ID=self.course.get_course_id())

        # Verify that the changes were stored in the database
        self.assertEqual(updated_course.credits, new_credits)

    def test_set_min_Credits(self):
        with self.assertRaises(ValueError, msg="Credits is too small"):
            self.course.set_credits(0)

    def test_set_max_Credits(self):
        with self.assertRaises(ValueError, msg="Credits is too small"):
            self.course.set_credits(10)


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

    def test_get_int_semester(self):
        self.assertRaises(TypeError, self.course2.get_course_name(), msg="Semester is integer")


class TestSetSemester(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022",
                                             description="first course", credits="3")
        self.course: AbstractCourse = ConcreteCourse(course_model)

    def test_set_correct_semester(self):
        new_semester = 'Fall'

        self.course.set_semester(new_semester)

        # Retrieve the updated data from the database
        updated_course = Course.objects.get(course_ID=self.course.get_course_id())

        # Verify that the changes were stored in the database
        self.assertEqual(updated_course.semester, new_semester)

    def test_set_int_semester(self):
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

    def test_get_correct_year(self):
        self.assertEqual(self.course.get_year(), 2022, msg="Year is incorrect")

    def test_get_str_year(self):
        self.assertRaises(TypeError, self.course2.get_year(), msg="Year is integer")


class TestSetYear(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year=2022,
                                             description="first course", credits="3")
        self.course: AbstractCourse = ConcreteCourse(course_model)

    def test_set_correct_year(self):
        new_year = 2025

        self.course.set_year(new_year)

        # Retrieve the updated data from the database
        updated_course = Course.objects.get(course_ID=self.course.get_course_id())

        # Verify that the changes were stored in the database
        self.assertEqual(updated_course.year, new_year)

    def test_set_str_year(self):
        with self.assertRaises(TypeError, msg="Year is string"):
            self.course.set_year("2022")

    def test_set_max_year(self):
        with self.assertRaises(ValueError, msg="The year is too far in the future"):
            self.course.set_year(2200)

    def test_set_min_year(self):
        with self.assertRaises(ValueError, msg="The year is too far in the past"):
            self.course.set_year(1888)


class TestGetInstructor(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022",
                                             description="first course", credits="3")
        self.course: AbstractCourse = ConcreteCourse(course_model)

        inst_model = User.objects.create(email="Inst1@gmail.com", username="Inst1", password="inst1",
                                         first_name="first", last_name="instructor", phone_number="123",
                                         home_address="address",
                                         user_type="Instructor")
        inst_user_model = Instructor.objects.create(account_ID=inst_model)
        self.instr: AbstractUser = InstructorUser(inst_user_model)

    def test_get_instructor(self):
        self.course.add_instructor(self.instr)
        self.assertNotEqual(self.course.get_instructors(), [], msg="Instructor was not found")


class TestAddInstructor(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022",
                                             description="first course", credits="3")
        self.course: AbstractCourse = ConcreteCourse(course_model)

        inst_model = User.objects.create(email="Inst1@gmail.com", username="Inst1", password="inst1",
                                         first_name="first", last_name="instructor", phone_number="123",
                                         home_address="address",
                                         user_type="Instructor")
        inst_user_model = Instructor.objects.create(account_ID=inst_model)
        self.instr: AbstractUser = InstructorUser(inst_user_model)

        ta_model = User.objects.create(email="Ta1@gmail.com", username="Ta1", password="ta1",
                                       first_name="first", last_name="ta", phone_number="1234", home_address="address",
                                       user_type="TA")
        self.ta: AbstractUser = TAUser(ta_model)

    def test_add_Instr_no_Arg(self):
        with self.assertRaises(TypeError, msg="More than zero argument is required"):
            self.course.add_instructor()

    def test_add_Instr_more_arg(self):
        with self.assertRaises(TypeError, msg="add instr - Too much arg was added"):
            self.course.add_instructor(self.instr, self.ta)

    def test_add_Instr_wrong_User(self):
        with self.assertRaises(TypeError, msg="This user is not a instructor"):
            self.course.add_instructor(self.ta)

    def test_add_Instr_success(self):
        self.course.add_instructor(self.instr)
        self.assertNotEqual(self.course.get_instructors(), [], msg="Instructor was not found")


class TestremoveInstructor(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022",
                                             description="first course", credits="3")
        self.course: AbstractCourse = ConcreteCourse(course_model)

        inst_model = User.objects.create(email="Inst1@gmail.com", username="Inst1", password="inst1",
                                         first_name="first", last_name="instructor", phone_number="123",
                                         home_address="address",
                                         user_type="Instructor")
        inst_user_model = Instructor.objects.create(account_ID=inst_model)
        self.instr: AbstractUser = InstructorUser(inst_user_model)

        User.objects.create(username='ta', password='password1', first_name="ta", last_name='ta',
                            phone_number=2345678901, home_address='123 Hell Lane', user_type='TA',
                            email='taemail@aol.com')
        ta_user_model = User.objects.filter(username='ta')[0]
        self.ta = TA.objects.create(account_ID=ta_user_model)

    def test_remove_instructor_no_arg(self):
        with self.assertRaises(TypeError, msg="Remove instructor - No arg was added"):
            self.course.remove_instructor()

    def test_remove_instructor_more_arg(self):
        with self.assertRaises(TypeError, msg="Remove instructor - Too much arg was added"):
            self.course.remove_instructor(self.ta, self.instr)

    def test_remove_ta_no_user(self):
        with self.assertRaises(TypeError, msg="Remove instructor - no such instructor was found"):
            self.course.remove_instructor(self.ta)

    def test_remove_instr_success(self):
        self.course.add_instructor(self.instr)
        self.course.remove_instructor(self.instr)
        self.assertEqual(self.course.get_instructors(), [], msg="Instructor was not deleted")


class TestGetTa(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022",
                                             description="first course", credits="3")
        self.course: AbstractCourse = ConcreteCourse(course_model)

        inst_model = User.objects.create(email="Inst1@gmail.com", username="Inst1", password="inst1",
                                         first_name="first", last_name="instructor", phone_number="123",
                                         home_address="address",
                                         user_type="Instructor")
        inst_user_model = Instructor.objects.create(account_ID=inst_model)
        self.instr: AbstractUser = InstructorUser(inst_user_model)

        ta_model = User.objects.create(email="Ta1@gmail.com", username="Ta1", password="ta1",
                                       first_name="first", last_name="ta", phone_number="1234", home_address="address",
                                       user_type="TA")
        ta_user_model = TA.objects.create(account_ID=ta_model)
        self.ta = TAUser(ta_user_model)

    def test_get_correct_ta(self):
        self.assertEqual(self.course.get_tas(), [], msg="Instructor was not found")


class TestAddTa(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022",
                                             description="first course", credits="3")
        self.course: AbstractCourse = ConcreteCourse(course_model)

        inst_model = User.objects.create(email="Inst1@gmail.com", username="Inst1", password="inst1",
                                         first_name="first", last_name="instructor", phone_number="123",
                                         home_address="address",
                                         user_type="Instructor")
        self.inst: AbstractUser = InstructorUser(inst_model)

        ta_model = User.objects.create(email='taemail@aol.com', username='ta', password='password1', first_name="ta",
                                       last_name='ta', phone_number=2345678901, home_address='123 Hell Lane',
                                       user_type='TA'
                                       )
        ta_user_model = TA.objects.filter(account_ID=ta_model)
        self.ta: AbstractUser = TAUser(ta_user_model)

    def test_add_ta_no_arg(self):
        with self.assertRaises(TypeError, msg="Add ta - more than one arg is required"):
            self.course.add_ta()

    def test_add_ta_more_arg(self):
        with self.assertRaises(TypeError, msg="Add ta - Too much arg was added"):
            self.course.add_ta(self.ta, self.inst)

    def test_add_ta_wrong_user(self):
        with self.assertRaises(TypeError, msg="Add ta - this user is not a TA"):
            self.course.add_ta(self.inst)


class TestremoveTA(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022",
                                             description="first course", credits="3")
        self.course: AbstractCourse = ConcreteCourse(course_model)

        inst_model = User.objects.create(email="Inst1@gmail.com", username="Inst1", password="inst1",
                                         first_name="first", last_name="instructor", phone_number="123",
                                         home_address="address",
                                         user_type="Instructor")
        self.inst: AbstractUser = InstructorUser(inst_model)

        User.objects.create(username='ta', password='password1', first_name="ta", last_name='ta',
                            phone_number=2345678901, home_address='123 Hell Lane', user_type='TA',
                            email='taemail@aol.com')
        ta_user_model = User.objects.filter(username='ta')[0]
        self.ta = TA.objects.create(account_ID=ta_user_model)

    def test_remove_ta_no_arg(self):
        with self.assertRaises(TypeError, msg="Remove ta - No arg was added"):
            self.course.remove_ta()

    def test_remove_ta_more_arg(self):
        with self.assertRaises(TypeError, msg="Remove ta - Too much arg was added"):
            self.course.remove_ta(self.ta, self.inst)

    def test_remove_ta_no_user(self):
        with self.assertRaises(TypeError, msg="Remove ta - no such TA was found"):
            self.course.remove_ta(self.inst)


class TestGetSection(TestCase):
    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022", description="test",
                                             credits="3")
        self.course: AbstractCourse = ConcreteCourse(course_model)

        section_model = Section.objects.create(course_ID=course_model, section_num=101, MeetingTimes="9:00")
        self.section: AbstractSection = ConcreteSection(section_model)

    def test_get_correct_section(self):
        self.assertNotEqual(self.course.get_sections()[0], [], msg="No sections are found")


class TestaddSection(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022", description="test",
                                             credits="3")
        self.course: AbstractCourse = ConcreteCourse(course_model)

        section_model = Section.objects.create(course_ID=course_model, section_num=101, MeetingTimes="9:00")
        self.section: AbstractSection = ConcreteSection(section_model)
        self.section.section_num = 101
        self.section.MeetingTimes = "9.00"

        User.objects.create(username='ta', password='password1', first_name="ta", last_name='ta',
                            phone_number=2345678901, home_address='123 Hell Lane', user_type='TA',
                            email='taemail@aol.com')
        ta_user_model = User.objects.filter(username='ta')[0]
        self.ta = TA.objects.create(account_ID=ta_user_model)

    def test_add_section_no_arg(self):
        with self.assertRaises(TypeError, msg="add_section - More than zero arg is required"):
            self.course.add_section()

    def test_add_secion_one_arg(self):
        with self.assertRaises(TypeError, msg="add_section - More than one arg is required"):
            self.course.add_section(self.ta.account_ID)

    def test_add_secion_two_arg(self):
        with self.assertRaises(TypeError, msg="add_section - More than two arg is required"):
            self.course.add_section(self.ta.account_ID, self.section.section_num)

    def test_add_section_more_arg(self):
        with self.assertRaises(TypeError, msg="add_section - Too many arg was added"):
            self.course.add_section(self.ta.account_ID, self.section.section_num, self.section.MeetingTimes,
                                    self.course.get_course_id)

    def test_add_section_not_saved(self):
        self.course.add_section(self.ta.account_ID, 102, self.section.MeetingTimes)
        length = len(Section.objects.filter(section_num=102))
        self.assertNotEqual(0, length, msg="Section was not added")


class TestremoveSection(TestCase):

    def setUp(self) -> None:
        course_model = Course.objects.create(name="course1", semester="Spring", year="2022", description="test",
                                             credits="3")

        section_model = Section.objects.create(course_ID=course_model, section_num=101, MeetingTimes="9:00")

        self.course: AbstractCourse = ConcreteCourse(course_model)
        self.section: AbstractSection = ConcreteSection(section_model)

    def test_remove_section_no_arg(self):
        with self.assertRaises(TypeError, msg="remove_section - More than zero arg is required"):
            self.course.remove_section()

    def test_add_section_more_arg(self):
        with self.assertRaises(TypeError, msg="add_section - Too many arg was added"):
            self.course.add_section(self.section, 111)

    def test_remove_section_not_deleted(self):
        self.course.remove_section(self.section)
        length = len(Section.objects.filter(section_num=100))
        self.assertEqual(0, length, msg="Section was not deleted, it still exists")

from django.test import TestCase
from app.models import Section, Course, User
from classes.Sections.SectionClass import AbstractSection, ConcreteSection
from classes.Courses.CoursesClass import AbstractCourse, ConcreteCourse
from classes.Users.users import AbstractUser, TAUser
from django.core.exceptions import ObjectDoesNotExist


class SectionTest(TestCase):
    pass


class TestGetParent(TestCase):
    def setUp(self) -> None:
        self.course_model = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                                  description="", credits=4)
        self.course_model2 = Course.objects.create(name='Advanced Nonsense', semester='Spring', year=2022,
                                                   description="", credits=4)
        section = Section.objects.create(course_ID=self.course_model, section_num=100, MeetingTimes='12:00')
        section2 = Section.objects.create(course_ID=self.course_model2, section_num=200, MeetingTimes='1:00')
        self.course: AbstractCourse = ConcreteCourse(self.course_model)
        self.wrapper: AbstractSection = ConcreteSection(section)
        self.wrapper2: AbstractSection = ConcreteSection(section2)

    def test_success(self):
        self.assertEqual(self.course.getCourseID(), self.wrapper.getParentCourse())
        # TODO check getCourseID after merge

    def test_delete_course(self):
        self.course_model.delete()
        with self.assertRaises(ObjectDoesNotExist, msg="Section parent does not exist"):
            self.wrapper.getParentCourse()

    def test_delete_section(self):  # TODO check if this should be left out
        self.wrapper2.delete()
        with self.assertRaises(ObjectDoesNotExist, msg="Section does not exist"):
            self.wrapper2.getParentCourse()

    # TODO add test for invalid course if needed
    # TODO add more tests if needed


class TestGetSectionNum(TestCase):
    def setUp(self) -> None:
        self.course = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                            description="idk lol", credits=4)
        section = Section.objects.create(course_ID=self.course, section_num=100, MeetingTimes='12:00')
        section2 = Section.objects.create(course_ID=self.course, section_num=None, MeetingTimes='1:00')
        section3 = Section.objects.create(course_ID=self.course, section_num=11111111111111111,
                                          MeetingTimes='2:00')
        self.course: AbstractCourse = ConcreteCourse(self.course)
        self.wrapper: AbstractSection = ConcreteSection(section)
        self.wrapper2: AbstractSection = ConcreteSection(section2)
        self.wrapper3: AbstractSection = ConcreteSection(section3)

    def test_success(self):
        self.assertEqual(100, self.wrapper.getSectionNumber())

    def test_no_number(self):
        self.assertRaises(TypeError, self.wrapper2.getSectionNumber())
        # TODO check if correct error type

    def test_invalid_number(self):
        self.assertRaises(ValueError, self.wrapper3.getSectionNumber())
        # TODO check if correct error type

    # TODO add more tests if needed


class TestSetSectionNum(TestCase):
    def setUp(self) -> None:
        self.course = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                            description="idk lol", credits=4)
        section = Section.objects.create(course_ID=self.course, section_num=100, MeetingTimes='12:00')
        self.course: AbstractCourse = ConcreteCourse(self.course)
        self.wrapper: AbstractSection = ConcreteSection(section)

    def test_success(self):
        new = self.wrapper.setSectionNumber(400)
        self.assertEquals(1, new)
        # TODO fix these

    def test_set_long(self):
        new = self.wrapper.setSectionNumber(11111111111111111111)
        self.assertEqual(0, new)
        # TODO make sure section num is not changed when given long value

    def test_set_none(self):
        new = self.wrapper.setSectionNumber(None)
        self.assertEqual(0, new)
        # TODO make sure section num is not changed when given no value

    def test_invalid(self):
        new = self.wrapper.setSectionNumber('WRONG')
        self.assertEqual(0, new)
        # TODO make sure section num is not changed when given invalid value

    # TODO add more tests if needed


class TestGetTA(TestCase):
    def setUp(self) -> None:
        self.course = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                            description="idk lol", credits=4)
        self.ta = User.objects.create(user_type="TA", first_name='Luke', last_name='Hodory', password="password",
                                      email="profhod@gmail.com", username='lhodory')
        section = Section.objects.create(course_ID=self.course, section_num=100, MeetingTimes='12:00',
                                         ta_account_id=self.ta)
        section2 = Section.objects.create(course_ID=self.course, section_num=200, MeetingTimes='12:00',
                                          ta_account_id=123)
        section3 = Section.objects.create(course_ID=self.course, section_num=300, MeetingTimes='12:00',
                                          ta_account_id='WRONG')
        section4 = Section.objects.create(course_ID=self.course, section_num=400, MeetingTimes='12:00',
                                          ta_account_id=None)
        self.course: AbstractCourse = ConcreteCourse(self.course)
        self.ta: AbstractUser = TAUser(self.ta)
        self.wrapper: AbstractSection = ConcreteSection(section)
        self.wrapper2: AbstractSection = ConcreteSection(section2)
        self.wrapper3: AbstractSection = ConcreteSection(section3)
        self.wrapper4: AbstractSection = ConcreteSection(section4)

    def test_success(self):
        self.assertEqual(self.ta.account_ID, self.wrapper.getTA())

    def test_invalid(self):
        self.assertRaises(ValueError, self.wrapper2.getTA())

    def test_string(self):
        self.assertRaises(ValueError, self.wrapper3.getTA())

    def test_none(self):
        self.assertRaises(ValueError, self.wrapper4.getTA())


class TestSetTA(TestCase):
    def setUp(self) -> None:
        self.course = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                            description="idk lol", credits=4)
        self.ta = User.objects.create(user_type="TA", first_name='Luke', last_name='Hodory', password="password",
                                      email="proflhod@gmail.com", username='lhodory')
        self.ta2 = User.objects.create(user_type="TA", first_name='Jake', last_name='Hodory', password="password",
                                      email="profjhod@gmail.com", username='jhodory')
        self.inst = User.objects.create(user_type="Instructor", first_name='Max', last_name='Hodory', password="password",
                                       email="profmhod@gmail.com", username='mhodory')
        section = Section.objects.create(course_ID=self.course, section_num=100, MeetingTimes='12:00',
                                         ta_account_id=self.ta)
        self.course: AbstractCourse = ConcreteCourse(self.course)
        self.ta: AbstractUser = TAUser(self.ta)
        self.ta2: AbstractUser = TAUser(self.ta2)
        self.inst: AbstractUser = TAUser(self.inst)
        self.wrapper: AbstractSection = ConcreteSection(section)

    def test_success(self):
        new = self.wrapper.setTA(self.ta2)
        self.assertEqual(1, new)

    def test_invalid_user(self):
        new = self.wrapper.setTA(self.ta2)
        self.assertEqual(0, new)

    def test_not_ta(self):
        new = self.wrapper.setTA(self.inst)
        self.assertEqual(0, new)

    def test_assigned_ta(self):
        new = self.wrapper.setTA(self.ta)
        self.assertEqual(0, new)


class TestGetMeetTime(TestCase):
    def setUp(self) -> None:
        self.course = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                            description="idk lol", credits=4)
        section = Section.objects.create(course_ID=self.course, section_num=100, MeetingTimes='12:00')
        section2 = Section.objects.create(course_ID=self.course, section_num=100, MeetingTimes='')
        section3 = Section.objects.create(course_ID=self.course, section_num=100, MeetingTimes=123)
        section4 = Section.objects.create(course_ID=self.course, section_num=100, MeetingTimes=None)
        self.course: AbstractCourse = ConcreteCourse(self.course)
        self.wrapper: AbstractSection = ConcreteSection(section)
        self.wrapper2: AbstractSection = ConcreteSection(section2)
        self.wrapper3: AbstractSection = ConcreteSection(section3)
        self.wrapper4: AbstractSection = ConcreteSection(section4)

    def test_success(self):
        self.assertEqual('12:00', self.wrapper.getMeetTime())

    def test_empty(self):
        self.assertRaises(ValueError, self.wrapper2.getMeetTime())

    def test_invalid(self):
        self.assertRaises(TypeError, self.wrapper3.getMeetTime())

    def test_none(self):
        self.assertRaises(TypeError, self.wrapper4.getMeetTime())

    # TODO add more tests if needed


class TestSetMeetTime(TestCase):
    def setUp(self) -> None:
        self.course = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                            description="idk lol", credits=4)
        section = Section.objects.create(course_ID=self.course, section_num=100, MeetingTimes='12:00')
        section2 = Section.objects.create(course_ID=self.course, section_num=200, MeetingTimes='12:00')
        self.course: AbstractCourse = ConcreteCourse(self.course)
        self.wrapper: AbstractSection = ConcreteSection(section)
        self.wrapper2: AbstractSection = ConcreteSection(section2)

    def test_success(self):
        new = self.wrapper.setMeetTime('1:00')
        self.assertEqual(1, new)

    def test_invalid(self):
        new = self.wrapper.setMeetTime(132)
        self.assertEqual(0, new)
        # TODO make sure meet time is supposed t stay the same when given wrong value

    def test_empty(self):
        new = self.wrapper.setMeetTime('')
        self.assertEqual(0, new)

    def test_none(self):
        new = self.wrapper.setMeetTime(None)
        self.assertEqual(0, new)

    # TODO add more tests if needed

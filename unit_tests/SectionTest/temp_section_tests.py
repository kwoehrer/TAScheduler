from django.test import TestCase
from app.models import Section, Course, User, TA

# from classes.Sections.temp_course_class import AbstractCourse, ConcreteCourse
# from classes.Sections.temp_section_class import AbstractSection, ConcreteSection
from classes.Users.users import AbstractUser, InstructorUser, TAUser

from django.core.exceptions import ObjectDoesNotExist

import classes.Sections.temp_section_class as SectionClass
import classes.Sections.temp_course_class as CourseClass
import classes.Users.users as UserClass


# import classes.Users.users as UserClass

class TestGetParent(TestCase):
    def setUp(self) -> None:
        self.course_model = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                                  description='something', credits=4)
        section = Section.objects.create(course_ID=self.course_model, section_num=100, MeetingTimes='1:00')
        self.course = CourseClass.ConcreteCourse(self.course_model)
        self.wrapper = SectionClass.ConcreteSection(section)

    def test_success(self):
        self.assertEqual(self.course_model.course_ID, self.wrapper.getParentCourse().get_course_id())


class TestGetSectionNum(TestCase):
    def setUp(self) -> None:
        self.course_model = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                                  description='something', credits=4)
        section = Section.objects.create(course_ID=self.course_model, section_num=100, MeetingTimes='1:00')
        section2 = Section.objects.create(course_ID=self.course_model, section_num=0, MeetingTimes='2:00')
        section3 = Section.objects.create(course_ID=self.course_model, section_num=-1, MeetingTimes='3:00')
        self.course = CourseClass.ConcreteCourse(self.course_model)
        self.wrapper = SectionClass.ConcreteSection(section)
        self.wrapper2 = SectionClass.ConcreteSection(section2)
        self.wrapper3 = SectionClass.ConcreteSection(section3)

    def test_success(self):
        self.assertEqual(100, self.wrapper.getSectionNumber())

    def test_zero(self):
        self.assertEqual(0, self.wrapper2.getSectionNumber())

    def test_neg(self):
        self.assertEqual(-1, self.wrapper3.getSectionNumber())



class TestSetSectionNum(TestCase):
    def setUp(self) -> None:
        self.course_model = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                                  description='something', credits=4)
        section = Section.objects.create(course_ID=self.course_model, section_num=100, MeetingTimes='1:00')
        self.course = CourseClass.ConcreteCourse(self.course_model)
        self.wrapper = SectionClass.ConcreteSection(section)

    def test_success(self):
        self.wrapper.setSectionNumber(400)
        self.assertEqual(400, self.wrapper.getSectionNumber())

    def test_none(self):
        with self.assertRaises(TypeError, msg="new section cannot be None"):
            self.wrapper.setSectionNumber(None)

    def test_string(self):
        with self.assertRaises(TypeError, msg="new section cannot be a string"):
            self.wrapper.setSectionNumber('WRONG')

    def test_short(self):
        with self.assertRaises(ValueError, msg="new section number too short"):
            self.wrapper.setSectionNumber(1)

    def test_long(self):
        with self.assertRaises(ValueError, msg="new section number too long"):
            self.wrapper.setSectionNumber(111111111)



class TestGetTA(TestCase):
    def setUp(self) -> None:
        self.course_model = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                                  description='something', credits=4)
        User.objects.create(email="lhod@gmail", username='lhod', password='password', first_name='Luke',
                            last_name='Hodory', user_type='TA')
        self.user_model = User.objects.filter(username='lhod')[0]
        self.ta_model = TA.objects.create(account_ID=self.user_model)
        section = Section.objects.create(course_ID=self.course_model, section_num=100, MeetingTimes='1:00',
                                         ta_account_id=self.ta_model.account_ID)

        self.course = CourseClass.ConcreteCourse(self.course_model)
        self.ta = UserClass.TAUser(self.ta_model)
        self.wrapper = SectionClass.ConcreteSection(section)

    def test_success(self):
        self.assertEqual(self.ta_model.account_ID, self.wrapper.getTA().getID())


class TestSetTA(TestCase):
    pass


class TestGetMeetTime(TestCase):
    def setUp(self) -> None:
        self.course_model = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                                  description='something', credits=4)
        section = Section.objects.create(course_ID=self.course_model, section_num=100, MeetingTimes='1:00')

        self.course = CourseClass.ConcreteCourse(self.course_model)
        self.wrapper = SectionClass.ConcreteSection(section)

    def test_success(self):
        self.assertEqual('1:00', self.wrapper.getMeetTime())


class TestSetMeetTime(TestCase):
    def setUp(self) -> None:
        self.course_model = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                                  description='something', credits=4)
        section = Section.objects.create(course_ID=self.course_model, section_num=100, MeetingTimes='1:00')

        self.course = CourseClass.ConcreteCourse(self.course_model)
        self.wrapper = SectionClass.ConcreteSection(section)

    def test_success(self):
        self.wrapper.setMeetTime('1:00')
        self.assertEqual('1:00', self.wrapper.getMeetTime())

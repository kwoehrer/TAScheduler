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
        section = Section.objects.create(course_ID=self.course_model, section_num=100, MeetingTimes='12:00')
        self.course = CourseClass.ConcreteCourse(self.course_model)
        self.wrapper = SectionClass.ConcreteSection(section)

    def test_success(self):
        self.assertEqual(self.course_model.course_ID, self.wrapper.getParentCourse().get_course_id())


class TestGetSectionNum(TestCase):
    def setUp(self) -> None:
        self.course_model = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                                  description='something', credits=4)
        section = Section.objects.create(course_ID=self.course_model, section_num=100, MeetingTimes='12:00')
        # section2 = Section.objects.create(course_ID=self.course_model, section_num=None, MeetingTimes='1:00')
        # section3 = Section.objects.create(course_ID=self.course_model, section_num=11111111111111111,
        # MeetingTimes='2:00')

        self.course = CourseClass.ConcreteCourse(self.course_model)
        self.wrapper = SectionClass.ConcreteSection(section)
        # self.wrapper2: SectionClass.ConcreteSection = SectionClass.ConcreteSection(section2)
        # self.wrapper3: SectionClass.ConcreteSection = SectionClass.ConcreteSection(section3)

    def test_success(self):
        self.assertEqual(100, self.wrapper.getSectionNumber())


class TestSetSectionNum(TestCase):
    def setUp(self) -> None:
        self.course_model = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                                  description='something', credits=4)
        section = Section.objects.create(course_ID=self.course_model, section_num=100, MeetingTimes='12:00')
        # section2 = Section.objects.create(self.course.course_ID, section_num=200, MeetingTimes='1:00')
        # section3 = Section.objects.create(self.course.course_ID, section_num=300, MeetingTimes='2:00')

        self.course = CourseClass.ConcreteCourse(self.course_model)
        self.wrapper = SectionClass.ConcreteSection(section)
        # self.wrapper2: SectionClass.ConcreteSection = SectionClass.ConcreteSection(section2)
        # self.wrapper3: SectionClass.ConcreteSection = SectionClass.ConcreteSection(section2)

    def test_success(self):
        self.wrapper.setSectionNumber(400)
        self.assertEqual(400, self.wrapper.getSectionNumber())


class TestGetTA(TestCase):
    def setUp(self) -> None:
        self.course_model = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                                  description='something', credits=4)
        self.user_model = User.objects.create(email="lhod@gmail", username='lhod', password='password',
                                            first_name='Luke', last_name='Hodory', user_type='TA')
        self.ta_model = TA.objects.create(account_ID=self.user_model.account_ID)
        section = Section.objects.create(course_ID=self.course_model, section_num=100, MeetingTimes='12:00')

        self.course = CourseClass.ConcreteCourse(self.course_model)
        self.ta = UserClass.TAUser(self.ta_model)
        self.wrapper = SectionClass.ConcreteSection(section)

    def test_success(self):
        self.assertEqual(self.ta_model.account_ID, self.wrapper.getTA().getID())


class TestGetMeetTime(TestCase):
    def setUp(self) -> None:
        self.course_model = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                                  description='something', credits=4)
        section = Section.objects.create(course_ID=self.course_model, section_num=100, MeetingTimes='12:00')

        self.course = CourseClass.ConcreteCourse(self.course_model)
        self.wrapper = SectionClass.ConcreteSection(section)

    def test_success(self):
        self.assertEqual('12:00', self.wrapper.getMeetTime())

class TestSetMeetTime(TestCase):
    def setUp(self) -> None:
        self.course_model = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                                  description='something', credits=4)
        section = Section.objects.create(course_ID=self.course_model, section_num=100, MeetingTimes='12:00')

        self.course = CourseClass.ConcreteCourse(self.course_model)
        self.wrapper = SectionClass.ConcreteSection(section)

    def test_success(self):
        self.wrapper.setMeetTime('1:00')
        self.assertEqual('1:00', self.wrapper.getMeetTime())

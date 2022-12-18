from django.test import TestCase
from app.models import Section, Course, User, TA

# from classes.Sections.temp_course_class import AbstractCourse, ConcreteCourse
# from classes.Sections.temp_section_class import AbstractSection, ConcreteSection
from classes.Users.users import AbstractUser, InstructorUser, TAUser

from django.core.exceptions import ObjectDoesNotExist

import classes.Sections.temp_section_class as SectionClass
import classes.Sections.temp_course_class as CourseClass
import classes.Users.users as UserClass

from django.core.exceptions import ObjectDoesNotExist


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

    def test_delete(self):
        self.course_model.delete()
        self.wrapper.getParentCourse()


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

        User.objects.create(username='lhod', password='password', first_name="luke", last_name='hodory',
                            user_type='TA', email='lhod@gmail.com')
        ta_user_model = User.objects.filter(username='lhod')[0]
        self.ta_model = TA.objects.create(account_ID=ta_user_model)

        section = Section.objects.create(course_ID=self.course_model, section_num=100, MeetingTimes='1:00',
                                         ta_account_id=self.ta_model)

        self.course = CourseClass.ConcreteCourse(self.course_model)
        self.ta: AbstractUser = TAUser(self.ta_model)
        self.wrapper = SectionClass.ConcreteSection(section)

    def test_success(self):
        tamodel_userkey = self.wrapper.getTA().getID()
        tamodel = TA.objects.get(account_ID__account_ID=tamodel_userkey)
        self.assertEqual(self.ta_model, tamodel)


class TestSetTA(TestCase):

    def setUp(self) -> None:
        self.course_model = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                                  description='something', credits=4)

        User.objects.create(username='lhod', password='password', first_name="luke", last_name='hodory',
                            user_type='TA', email='lhod@gmail.com')
        ta_user_model = User.objects.filter(username='lhod')[0]
        self.ta_model = TA.objects.create(account_ID=ta_user_model)

        User.objects.create(username='jhod', password='password', first_name="jake", last_name='hodory',
                            user_type='Admin', email='jhod@gmail.com')
        admin_user_model = User.objects.filter(username='jhod')[0]
        self.admin_model = TA.objects.create(account_ID=admin_user_model)

        section = Section.objects.create(course_ID=self.course_model, section_num=100, MeetingTimes='1:00',
                                         ta_account_id=self.ta_model)

        self.course = CourseClass.ConcreteCourse(self.course_model)
        self.ta: AbstractUser = TAUser(self.ta_model)
        self.wrapper = SectionClass.ConcreteSection(section)

    def test_not_ta(self):
        with self.assertRaises(TypeError, msg="user assigned not ta"):
            self.wrapper.setTA(self.admin_model)


class TestGetMeetTime(TestCase):
    def setUp(self) -> None:
        self.course_model = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                                  description='something', credits=4)
        section = Section.objects.create(course_ID=self.course_model, section_num=100, MeetingTimes='1:00')
        section2 = Section.objects.create(course_ID=self.course_model, section_num=0, MeetingTimes='')
        section3 = Section.objects.create(course_ID=self.course_model, section_num=-1, MeetingTimes='0')
        self.course = CourseClass.ConcreteCourse(self.course_model)
        self.wrapper = SectionClass.ConcreteSection(section)
        self.wrapper2 = SectionClass.ConcreteSection(section2)
        self.wrapper3 = SectionClass.ConcreteSection(section3)

    def test_success(self):
        self.assertEqual('1:00', self.wrapper.getMeetTime())

    def test_empty(self):
        self.assertEqual('', self.wrapper2.getMeetTime())

    def test_zero(self):
        self.assertEqual('0', self.wrapper3.getMeetTime())


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

    def test_long(self):
        with self.assertRaises(ValueError, msg=""):
            self.wrapper.setMeetTime('11111111111111111111111111111111111111111111111111111111')

from django.test import TestCase
from app.models import Section, Course
from classes.Sections.SectionClass import AbstractSection, ConcreteSection
from django.core.exceptions import ObjectDoesNotExist


class SectionTest(TestCase):
    pass


class TestGetParent(TestCase):
    def setUp(self) -> None:
        self.course_model = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                                  description="", credits=4)
        self.course_model2 = Course.objects.create(name='Advanced Nonsense', semester='Spring', year=2022,
                                                   description="", credits=4)
        section = Section.objects.create(self.course_model.course_ID, section_num=100, MeetingTimes='12:00')
        section2 = Section.objects.create(self.course_model2.course_ID, section_num=200, MeetingTimes='1:00')
        self.course: AbstractCourse = ConcreteCourse(course)
        self.wrapper: AbstractSection = ConcreteSection(section)
        self.wrapper2: AbstractSection = ConcreteSection(section2)

    def test_success(self):
        self.assertEqual(self.course.getCourseID(),
                         self.wrapper.getParentCourse())  # TODO check getCourseID after merge

    def test_delete_course(self):
        self.course_model.delete()
        with self.assertRaises(ObjectDoesNotExist, msg="Section parent does not exist"):
            self.wrapper.getParentCourse()

    def test_delete_section(self):  # TODO check if this should be left out
        self.section2.delete()
        with self.assertRaises(ObjectDoesNotExist, msg="Section does not exist"):
            self.wrapper2.getParentCourse()
    # TODO add test for invalid course if needed
    # TODO add more tests if needed


class TestGetSectionNum(TestCase):
    def setUp(self) -> None:
        course = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                       description="idk lol", credits=4)
        section = Section.objects.create(course.course_ID, section_num=100, MeetingTimes='12:00')
        section2 = Section.objects.create(course.course_ID, section_num=None, MeetingTimes='12:00')
        section2 = Section.objects.create(course.course_ID, section_num=11111111111111111, MeetingTimes='12:00')
        self.course: AbstractCourse = ConcreteCourse(course)
        self.wrapper: AbstractSection = ConcreteSection(section)
        self.wrapper2: AbstractSection = ConcreteSection(section2)

    def test_success(self):
        self.assertEqual(100, self.wrapper.getSectionNumber())

    def test_no_number(self):
        self.assertRaises(TypeError, self.wrapper2.getSectionNumber())  # TODO check if correct error type

    def test_invalid_number(self):
        self.assertRaises(ValueError, self.wrapper3.getSectionNumber())  # TODO check if correct error type

    # TODO add more tests if needed

class TestSetSectionNum(TestCase):
    pass


class TestGetTA(TestCase):
    pass


class TestSetTA(TestCase):
    pass


class TestGetMeetTime(TestCase):
    pass


class TestSetMeetTime(TestCase):
    pass

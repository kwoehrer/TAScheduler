from django.test import TestCase
from app.models import Section, Course
from classes.Sections.SectionClass import AbstractSection, ConcreteSection


class SectionTest(TestCase):
    pass


class TestGetParent(TestCase):
    def setUp(self) -> None:
        course = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                       description="idk lol", credits=4)
        section_model = Section.objects.create(course.course_ID)
        self.wrapper : AbstractSection = ConcreteSection(section_model)

    def test_success(self):
    def test_delete_model(self):


class TestGetSectionNum(TestCase):
    pass


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

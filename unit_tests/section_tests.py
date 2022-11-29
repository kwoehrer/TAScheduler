from django.test import TestCase
from app.models import Section, Course


class SectionTest(TestCase):
    pass


class TestGetParent(TestCase):
    def setUp(self) -> None:
        Course.objects.create(course_ID=101, name='Intro to Nonsense', semester='Spring', year=2022)
        Section.objects.filter(course_ID=101)


class TestGetSectionNum(TestCase):
    pass


class TestSetSectionNum(TestCase):
    pass


class test_get_TA(TestCase):
    pass


class test_set_TA(TestCase):
    pass


class test_get_meet_time(TestCase):
    pass


class test_set_meet_time(TestCase):
    pass

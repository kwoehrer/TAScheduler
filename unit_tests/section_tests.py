from django.test import TestCase
from app.models import Section

class SectionTest(TestCase):
    pass

class test_get_parent(TestCase):
    def setUp(self):
        Section.objects.create(course_ID=, section_num=456, MeetingTimes='12:00', ta_account_id=)

class test_get_section_num(TestCase):
    pass
class test_set_section_num(TestCase):
    pass
class test_get_TA(TestCase):
    pass
class test_set_TA(TestCase):
    pass
class test_get_meet_time(TestCase):
    pass
class test_set_meet_time(TestCase):
    pass
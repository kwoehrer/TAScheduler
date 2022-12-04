from django.test import TestCase
from app.models import Section, Course, User

#from classes.Sections.temp_course_class import AbstractCourse, ConcreteCourse
#from classes.Sections.temp_section_class import AbstractSection, ConcreteSection
from classes.Users.users import AbstractUser, InstructorUser, TAUser

from django.core.exceptions import ObjectDoesNotExist

import classes.Sections.temp_section_class as SectionClass
import classes.Sections.temp_course_class as CourseClass
#import classes.Users.users as UserClass

class TestGetParent(TestCase):
    def setUp(self) -> None:
        self.course_model = Course.objects.create(name='Intro to Nonsense', semester='Spring', year=2022,
                                                  description="", credits=4)
        self.course_model2 = Course.objects.create(name='Advanced Nonsense', semester='Spring', year=2022,
                                                   description="", credits=4)
        section = Section.objects.create(self.course_model.course_ID, section_num=100, MeetingTimes='12:00')
        section2 = Section.objects.create(self.course_model2.course_ID, section_num=200, MeetingTimes='1:00')

        self.course = CourseClass.ConcreteCourse(self.course_model)
        self.wrapper = CourseClass.ConcreteSection(section)
        self.wrapper2 = CourseClass.ConcreteSection(section2)

    def test_success(self):
        self.assertEqual(self.course.getCourseID(), self.wrapper.getParentCourse())
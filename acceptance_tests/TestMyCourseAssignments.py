from django.test import TestCase, Client
from app.models import *
from classes.Users.users import InstructorUser, TAUser
import classes.Sections.temp_course_class as CourseClass

'''
As an Instructor or TA, I want to be able navigate the My Course Assignments Page
-----------------------------------------------------------------------
SCENARIO: As an Instructor or TA, I want to be able to correctly view course information if I log into the Section Summary page
GIVEN The user is an Instructor and is logged in and at the Section Summary page
THEN my courses should be displayed with correct information
-----------------------------------------------------------------------
'''


class TestInstructorSectionSummaryPage(TestCase):
    client = None

    def setUp(self):
        self.client = Client()
        course_model = Course.objects.create(name='Introduction to Programming I', semester='Spring', year=2022,
                                             description='Intro to Programming', credits=4)
        self.course = CourseClass.ConcreteCourse(course_model)
        course_model.save()

    def test_assignmentInfo(self):
        response = self.client.get('/MyCourseAssignments')
        self.assertContains(response, self.course.get_course_id())
        self.assertContains(response, self.course.get_course_name())
        self.assertContains(response, self.course.get_semester())
        self.assertContains(response, self.course.get_year())
        self.assertContains(response, self.course.get_sections())


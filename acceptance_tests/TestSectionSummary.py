from django.test import TestCase, Client
from app.models import *
from classes.Users.users import AdminUser, InstructorUser, TAUser
import classes.Sections.temp_section_class as SectionClass
import classes.Sections.temp_course_class as CourseClass

'''
As an Admin, I want to be able navigate the Section Summary Page
-----------------------------------------------------------------------
SCENARIO: As an Admin, I want to be able to correctly view course information if I log into the Section Summary page
GIVEN The user is an Admin and is logged in and at the Section Summary page
THEN all courses should be displayed with correct information
-----------------------------------------------------------------------
'''


class TestAdminSectionSummaryPage(TestCase):
    client = None
    admin = None

    def setUp(self):
        self.client = Client()
        self.course_model1 = Course.objects.create(name='Introduction to Programming I', semester='Spring', year=2022,
                                                   description='something', credits=4)
        section1 = Section.objects.create(course_ID=self.course_model1, section_num=100, TA="Davidson Peter",
                                          MeetingTimes="MWF 9:00AM - 9:50AM")
        self.course = CourseClass.ConcreteCourse(self.course_model1)
        self.wrapper = SectionClass.ConcreteSection(section1)
        section1.save()

        self.course_model2 = Course.objects.create(name='Introduction to Programming II', semester='Spring', year=2022,
                                                   description='something1', credits=4)
        section2 = Section.objects.create(course_ID=self.course_model2, section_num=200, TA="David Miles",
                                          MeetingTimes="MWF 10:00AM - 10:50AM")
        self.course = CourseClass.ConcreteCourse(self.course_model2)
        self.wrapper = SectionClass.ConcreteSection(section2)
        section2.save()

        self.course_model3 = Course.objects.create(name='Introduction to Programming III', semester='Spring', year=2022,
                                                   description='something2', credits=4)
        section3 = Section.objects.create(course_ID=self.course_model3, section_num=300, TA="Jeffrey Adams",
                                          MeetingTimes="MWF 11:00AM - 11:50AM")

        section3.save()

        self.course_model4 = Course.objects.create(name='Introduction to Compilers', semester='Spring', year=2022,
                                                   description='something4', credits=4)
        section4 = Section.objects.create(course_ID=self.course_model4, section_num=400, TA="Jeffrey Adams",
                                          MeetingTimes="MWF 11:00AM - 11:50AM")

        section4.save()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave',
                            user_type='Admin',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.admin: AdminUser = AdminUser(user_model)

    def test_ViewCourseCourseSummary(self):
        courses = [self.course_model1, self.course_model2, self.course_model3, self.course_model4]
        response = self.client.get('/SectionSummary')
        for course in courses:
            self.assertContains(response, course.getParentCourse())
            self.assertContains(response, course.getSectionNumber())
            self.assertContains(response, course.getMeetTime())
            self.assertContains(response, course.getTA())


'''
As an Instructor, I want to be able navigate the Section Summary Page
-----------------------------------------------------------------------
SCENARIO: As an Instructor, I want to be able to correctly view course information if I log into the Section Summary page
GIVEN The user is an Instructor and is logged in and at the Section Summary page
THEN all courses should be displayed with correct information
-----------------------------------------------------------------------
'''


class TestInstructorSectionSummaryPage(TestCase):
    client = None
    admin = None

    def setUp(self):
        self.client = Client()
        self.course_model1 = Course.objects.create(name='Introduction to Programming I', semester='Spring', year=2022,
                                                   description='something', credits=4)
        section1 = Section.objects.create(course_ID=self.course_model1, section_num=100, TA="Davidson Peter",
                                          MeetingTimes="MWF 9:00AM - 9:50AM")
        self.course = CourseClass.ConcreteCourse(self.course_model1)
        self.wrapper = SectionClass.ConcreteSection(section1)
        section1.save()

        self.course_model2 = Course.objects.create(name='Introduction to Programming II', semester='Spring', year=2022,
                                                   description='something1', credits=4)
        section2 = Section.objects.create(course_ID=self.course_model2, section_num=200, TA="David Miles",
                                          MeetingTimes="MWF 10:00AM - 10:50AM")
        self.course = CourseClass.ConcreteCourse(self.course_model2)
        self.wrapper = SectionClass.ConcreteSection(section2)
        section2.save()

        self.course_model3 = Course.objects.create(name='Introduction to Programming III', semester='Spring', year=2022,
                                                   description='something2', credits=4)
        section3 = Section.objects.create(course_ID=self.course_model3, section_num=300, TA="Jeffrey Adams",
                                          MeetingTimes="MWF 11:00AM - 11:50AM")

        section3.save()

        self.course_model4 = Course.objects.create(name='Introduction to Compilers', semester='Spring', year=2022,
                                                   description='something4', credits=4)
        section4 = Section.objects.create(course_ID=self.course_model4, section_num=400, TA="Jeffrey Adams",
                                          MeetingTimes="MWF 11:00AM - 11:50AM")

        section4.save()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave',
                            user_type='Admin',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_object)
        self.instructor: InstructorUser = InstructorUser(user_model)

    def test_ViewCourseCourseSummary(self):
        courses = [self.course_model1, self.course_model2, self.course_model3, self.course_model4]
        response = self.client.get('/SectionSummary')
        for course in courses:
            self.assertContains(response, course.getParentCourse())
            self.assertContains(response, course.getSectionNumber())
            self.assertContains(response, course.getMeetTime())
            self.assertContains(response, course.getTA())


'''
As a TA, I want to be able navigate the Section Summary Page
-----------------------------------------------------------------------
SCENARIO: As a TA, I want to be able to correctly view course information if I log into the Section Summary page
GIVEN The user is a TA and is logged in and at the Section Summary page
THEN all courses should be displayed with correct information
-----------------------------------------------------------------------
'''


class TestTASectionSummaryPage(TestCase):
    client = None
    admin = None

    def setUp(self):
        self.client = Client()
        self.course_model1 = Course.objects.create(name='Introduction to Programming I', semester='Spring', year=2022,
                                                   description='something', credits=4)
        section1 = Section.objects.create(course_ID=self.course_model1, section_num=100, TA="Davidson Peter",
                                          MeetingTimes="MWF 9:00AM - 9:50AM")
        self.course = CourseClass.ConcreteCourse(self.course_model1)
        self.wrapper = SectionClass.ConcreteSection(section1)
        section1.save()

        self.course_model2 = Course.objects.create(name='Introduction to Programming II', semester='Spring', year=2022,
                                                   description='something1', credits=4)
        section2 = Section.objects.create(course_ID=self.course_model2, section_num=200, TA="David Miles",
                                          MeetingTimes="MWF 10:00AM - 10:50AM")
        self.course = CourseClass.ConcreteCourse(self.course_model2)
        self.wrapper = SectionClass.ConcreteSection(section2)
        section2.save()

        self.course_model3 = Course.objects.create(name='Introduction to Programming III', semester='Spring', year=2022,
                                                   description='something2', credits=4)
        section3 = Section.objects.create(course_ID=self.course_model3, section_num=300, TA="Jeffrey Adams",
                                          MeetingTimes="MWF 11:00AM - 11:50AM")

        self.course_model4 = Course.objects.create(name='Introduction to Compilers', semester='Spring', year=2022,
                                                   description='something4', credits=4)
        section4 = Section.objects.create(course_ID=self.course_model4, section_num=400, TA="Jeffrey Adams",
                                          MeetingTimes="MWF 11:00AM - 11:50AM")

        section4.save()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave',
                            user_type='Admin',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_object)
        self.ta: TAUser = TAUser(user_model)

    def test_ViewCourseCourseSummary(self):
        courses = [self.course_model1, self.course_model2, self.course_model3, self.course_model4]
        response = self.client.get('/SectionSummary')
        for course in courses:
            self.assertContains(response, course.getParentCourse())
            self.assertContains(response, course.getSectionNumber())
            self.assertContains(response, course.getMeetTime())

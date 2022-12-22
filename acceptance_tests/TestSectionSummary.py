from django.test import TestCase, Client
from app.models import *
from classes.Users.users import AdminUser, InstructorUser, TAUser
from classes.Sections.SectionClass import AbstractSection, ConcreteSection

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
        spring_course = Section.objects.create(name="Introduction to Programming", section="103",
                                               TA="Richard White", MeetingTimes="MWF 9:00AM - 9:50AM")
        self.course1: AbstractSection = ConcreteSection(spring_course)
        spring_course.save()

        summer_course = Section.objects.create(name="Introduction to Programming II", section="203",
                                               TA="David Miles", MeetingTimes="MWF 9:00AM - 9:50AM")
        self.course2: AbstractSection = ConcreteSection(summer_course)
        summer_course.save()

        winter_course = Section.objects.create(name="Introduction to Programming III",
                                               section="303",
                                               TA="Jeffrey Adams", MeetingTimes="TF 11:00AM - 11:50AM")
        self.course3: AbstractSection = ConcreteSection(winter_course)
        winter_course.save()

        special_course = Section.objects.create(name="Introduction to Compilers",
                                                section="403",
                                                TA="Cameroon Davis", MeetingTimes="F 12:30PM - 1:20PM")

        self.course4: AbstractSection = ConcreteSection(special_course)
        special_course.save()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave',
                            user_type='Admin',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.admin: AdminUser = AdminUser(user_model)

    def test_ViewCourseCourseSummary(self):
        courses = [self.course1, self.course2, self.course3, self.course4]
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
        spring_course = Section.objects.create(name="Introduction to Programming", section="103",
                                               TA="Richard White", MeetingTimes="MWF 9:00AM - 9:50AM")
        self.course1: AbstractSection = ConcreteSection(spring_course)
        spring_course.save()

        summer_course = Section.objects.create(name="Introduction to Programming II", section="203",
                                               TA="David Miles", MeetingTimes="MWF 9:00AM - 9:50AM")
        self.course2: AbstractSection = ConcreteSection(summer_course)
        summer_course.save()

        winter_course = Section.objects.create(name="Introduction to Programming III",
                                               section="303",
                                               TA="Jeffrey Adams", MeetingTimes="TF 11:00AM - 11:50AM")
        self.course3: AbstractSection = ConcreteSection(winter_course)
        winter_course.save()

        special_course = Section.objects.create(name="Introduction to Compilers",
                                                section="403",
                                                TA="Cameroon Davis", MeetingTimes="F 12:30PM - 1:20PM")

        self.course4: AbstractSection = ConcreteSection(special_course)
        special_course.save()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave',
                            user_type='Admin',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.admin: AdminUser = AdminUser(user_model)

    def test_ViewCourseCourseSummary(self):
        courses = [self.course1, self.course2, self.course3, self.course4]
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
        spring_course = Section.objects.create(name="Introduction to Programming", section="103",
                                               TA="Richard White", MeetingTimes="MWF 9:00AM - 9:50AM")
        self.course1: AbstractSection = ConcreteSection(spring_course)
        spring_course.save()

        summer_course = Section.objects.create(name="Introduction to Programming II", section="203",
                                               TA="David Miles", MeetingTimes="MWF 9:00AM - 9:50AM")
        self.course2: AbstractSection = ConcreteSection(summer_course)
        summer_course.save()

        winter_course = Section.objects.create(name="Introduction to Programming III",
                                               section="303",
                                               TA="Jeffrey Adams", MeetingTimes="TF 11:00AM - 11:50AM")
        self.course3: AbstractSection = ConcreteSection(winter_course)
        winter_course.save()

        special_course = Section.objects.create(name="Introduction to Compilers",
                                                section="403",
                                                TA="Cameroon Davis", MeetingTimes="F 12:30PM - 1:20PM")

        self.course4: AbstractSection = ConcreteSection(special_course)
        special_course.save()
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave',
                            user_type='Admin',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.admin: AdminUser = AdminUser(user_model)

    def test_ViewCourseCourseSummary(self):
        courses = [self.course1, self.course2, self.course3, self.course4]
        response = self.client.get('/SectionSummary')
        for course in courses:
            self.assertContains(response, course.getParentCourse())
            self.assertContains(response, course.getSectionNumber())
            self.assertContains(response, course.getMeetTime())
            self.assertContains(response, course.getTA())

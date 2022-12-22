from django.test import TestCase, Client
from app.models import *
from classes.Users.users import AdminUser, InstructorUser, TAUser
from classes.Sections.SectionClass import AbstractSection, ConcreteSection

'''
As an Admin, I want to be able to navigate to the Section page
----------------------------------------------------
Scenario: Navigate to the Section Page
Acceptance Criteria 1:
GIVEN: The user is an Admin and is logged in and at the Section Page view
THEN: They should be able to view the details of a course correctly
---------------------------------------------------
Scenario: Navigate to the Home Page
Acceptance Criteria 2:
GIVEN: The user is an Admin and is logged in and at the Section Page view
AND: They can click on "Return to Home"
THEN: They will be navigated to the "Search Home"
----------------------------------------------------
'''


class TestAdminSectionPage(TestCase):
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

        self.client.login(username='John_Doe', password='password')

    def test_ViewCourseSpringCourseSectionSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course1.getParentCourse())
        self.assertContains(response, self.course1.getSectionNumber())
        self.assertContains(response, self.course1.getMeetTime())
        self.assertContains(response, self.course1.getTA())

    def test_ViewCourseSummerCourseSectionSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course2.getParentCourse())
        self.assertContains(response, self.course2.getSectionNumber())
        self.assertContains(response, self.course2.getMeetTime())
        self.assertContains(response, self.course2.getTA())

    def test_ViewCourseWinterCourseSectionSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course3.getParentCourse())
        self.assertContains(response, self.course3.getSectionNumber())
        self.assertContains(response, self.course3.getMeetTime())
        self.assertContains(response, self.course3.getTA())

    def test_ViewCourseSpecialCourseSectionSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course4.getParentCourse())
        self.assertContains(response, self.course4.getSectionNumber())
        self.assertContains(response, self.course4.getMeetTime())
        self.assertContains(response, self.course4.getTA())

    def test_Section_to_HomeSearch(self):
        # Make a GET request to /searchStates/UserSearch
        response = self.client.get("/Section")

        # Check that the response was a redirect to page /searchStates/SearchHome
        self.assertRedirects(response, 'home', status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

        # Follow the redirect and check that the final URL is '/searchStates/SearchHome'
        response = response.follow()
        self.assertEqual(response.url, 'home')


'''
As an Instructor, I want to be able to navigate to the Section page
----------------------------------------------------
Scenario: Navigate to the Section Page
Acceptance Criteria 1:
GIVEN: The user is an Instructor and is logged in and at the Section Page view
THEN: They should be able to view the details of a course correctly
---------------------------------------------------
Scenario: Navigate to the Home Page
Acceptance Criteria 2:
GIVEN: The user is an Instructor and is logged in and at the Section Page view
AND: They can click on "Return to Home"
THEN: They will be navigated to the "Search Home"
----------------------------------------------------
'''


class TestInstructorSectionPage(TestCase):
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
                            user_type='Instructor',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_object)
        self.instructor: InstructorUser = InstructorUser(user_model)

        self.client.login(username='John_Doe', password='password')

    def test_ViewCourseSpringCourseSectionSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course1.getParentCourse())
        self.assertContains(response, self.course1.getSectionNumber())
        self.assertContains(response, self.course1.getMeetTime())
        self.assertContains(response, self.course1.getTA())

    def test_ViewCourseSummerCourseSectionSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course2.getParentCourse())
        self.assertContains(response, self.course2.getSectionNumber())
        self.assertContains(response, self.course2.getMeetTime())
        self.assertContains(response, self.course2.getTA())

    def test_ViewCourseWinterCourseSectionSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course3.getParentCourse())
        self.assertContains(response, self.course3.getSectionNumber())
        self.assertContains(response, self.course3.getMeetTime())
        self.assertContains(response, self.course3.getTA())

    def test_ViewCourseSpecialCourseSectionSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course4.getParentCourse())
        self.assertContains(response, self.course4.getSectionNumber())
        self.assertContains(response, self.course4.getMeetTime())
        self.assertContains(response, self.course4.getTA())

    def test_Course_to_HomeSearch(self):
        # Make a GET request to /searchStates/UserSearch
        response = self.client.get("/Section")

        # Check that the response was a redirect to page /searchStates/SearchHome
        self.assertRedirects(response, 'home', status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

        # Follow the redirect and check that the final URL is '/searchStates/SearchHome'
        response = response.follow()
        self.assertEqual(response.url, 'home')


'''
As a TA, I want to be able to navigate to the Section page
----------------------------------------------------
Scenario: Navigate to the Section Page
Acceptance Criteria 1:
GIVEN: The user is a TA and is logged in and at the Section Page view
THEN: They should be able to view the details of a course correctly
---------------------------------------------------
Scenario: Navigate to the Home Page
Acceptance Criteria 2:
GIVEN: The user is a TA and is logged in and at the Section Page view
AND: They can click on "Return to Home"
THEN: They will be navigated to the "Search Home"
----------------------------------------------------
'''


class TestTASectionPage(TestCase):
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
                            user_type='TA',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_object)
        self.admin: TAUser = TAUser(user_model)

        self.client.login(username='John_Doe', password='password')

    def test_ViewCourseSpringCourseSectionSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course1.getParentCourse())
        self.assertContains(response, self.course1.getSectionNumber())
        self.assertContains(response, self.course1.getMeetTime())
        self.assertContains(response, self.course1.getTA())

    def test_ViewCourseSummerCourseSectionSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course2.getParentCourse())
        self.assertContains(response, self.course2.getSectionNumber())
        self.assertContains(response, self.course2.getMeetTime())
        self.assertContains(response, self.course2.getTA())

    def test_ViewCourseWinterCourseSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course3.getParentCourse())
        self.assertContains(response, self.course3.getSectionNumber())
        self.assertContains(response, self.course3.getMeetTime())
        self.assertContains(response, self.course3.getTA())

    def test_ViewCourseSpecialCourseSectionSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course4.getParentCourse())
        self.assertContains(response, self.course4.getSectionNumber())
        self.assertContains(response, self.course4.getMeetTime())
        self.assertContains(response, self.course4.getTA())

    def test_Section_to_HomeSearch(self):
        # Make a GET request to /searchStates/UserSearch
        response = self.client.get("/Section")

        # Check that the response was a redirect to page /searchStates/SearchHome
        self.assertRedirects(response, 'home', status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

        # Follow the redirect and check that the final URL is '/searchStates/SearchHome'
        response = response.follow()
        self.assertEqual(response.url, 'home')

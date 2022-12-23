from django.test import TestCase, Client
from app.models import *
from classes.Users.users import AdminUser, InstructorUser, TAUser
import classes.Sections.temp_section_class as SectionClass
import classes.Sections.temp_course_class as CourseClass

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
        self.course_model1 = Course.objects.create(name='Introduction to Programming I', semester='Spring', year=2022,
                                                   description='Intro to Programming', credits=4)
        section1 = Section.objects.create(course_ID=self.course_model1, section_num=100, TA="Davidson Peter",
                                          MeetingTimes="MWF 9:00AM - 9:50AM")
        self.course = CourseClass.ConcreteCourse(self.course_model1)
        self.wrapper = SectionClass.ConcreteSection(section1)
        section1.save()

        self.course_model2 = Course.objects.create(name='Introduction to Programming II', semester='Spring', year=2022,
                                                   description='Intro to Object-Oriented Principles', credits=4)
        section2 = Section.objects.create(course_ID=self.course_model2, section_num=200, TA="David Miles",
                                          MeetingTimes="MWF 10:00AM - 10:50AM")
        self.course = CourseClass.ConcreteCourse(self.course_model2)
        self.wrapper = SectionClass.ConcreteSection(section2)
        section2.save()

        self.course_model3 = Course.objects.create(name='Introduction to Programming III', semester='Spring', year=2022,
                                                   description='Data Structures', credits=4)
        section3 = Section.objects.create(course_ID=self.course_model3, section_num=300, TA="Jeffrey Adams",
                                          MeetingTimes="MWF 11:00AM - 11:50AM")

        section3.save()

        self.course_model4 = Course.objects.create(name='Introduction to Compilers', semester='Spring', year=2022,
                                                   description='Intro to Compiler Theory', credits=4)
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

        self.client.login(username='John_Doe', password='password')

    def test_ViewCourseSpringCourseSectionSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course_model1.getParentCourse())
        self.assertContains(response, self.course_model1.getSectionNumber())
        self.assertContains(response, self.course_model1.getMeetTime())
        self.assertContains(response, self.course_model1.getTA())

    def test_ViewCourseSummerCourseSectionSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course_model2.getParentCourse())
        self.assertContains(response, self.course_model2.getSectionNumber())
        self.assertContains(response, self.course_model2.getMeetTime())
        self.assertContains(response, self.course_model2.getTA())

    def test_ViewCourseWinterCourseSectionSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course_model3.getParentCourse())
        self.assertContains(response, self.course_model3.getSectionNumber())
        self.assertContains(response, self.course_model3.getMeetTime())
        self.assertContains(response, self.course_model3.getTA())

    def test_ViewCourseSpecialCourseSectionSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course_model4.getParentCourse())
        self.assertContains(response, self.course_model4.getSectionNumber())
        self.assertContains(response, self.course_model4.getMeetTime())
        self.assertContains(response, self.course_model4.getTA())

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
    instructor = None

    def setUp(self):
        self.client = Client()
        self.course_model1 = Course.objects.create(name='Introduction to Programming I', semester='Spring', year=2022,
                                                   description='Intro to Programming', credits=4)
        section1 = Section.objects.create(course_ID=self.course_model1, section_num=100, TA="Davidson Peter",
                                          MeetingTimes="MWF 9:00AM - 9:50AM")
        self.course = CourseClass.ConcreteCourse(self.course_model1)
        self.wrapper = SectionClass.ConcreteSection(section1)
        section1.save()

        self.course_model2 = Course.objects.create(name='Introduction to Programming II', semester='Spring', year=2022,
                                                   description='Intro to Object-Oriented Principles', credits=4)
        section2 = Section.objects.create(course_ID=self.course_model2, section_num=200, TA="David Miles",
                                          MeetingTimes="MWF 10:00AM - 10:50AM")
        self.course = CourseClass.ConcreteCourse(self.course_model2)
        self.wrapper = SectionClass.ConcreteSection(section2)
        section2.save()

        self.course_model3 = Course.objects.create(name='Introduction to Programming III', semester='Spring', year=2022,
                                                   description='Data Structures', credits=4)
        section3 = Section.objects.create(course_ID=self.course_model3, section_num=300, TA="Jeffrey Adams",
                                          MeetingTimes="MWF 11:00AM - 11:50AM")

        section3.save()

        self.course_model4 = Course.objects.create(name='Introduction to Compilers', semester='Spring', year=2022,
                                                   description='Intro to Compiler Theory', credits=4)
        section4 = Section.objects.create(course_ID=self.course_model4, section_num=400, TA="Jeffrey Adams",
                                          MeetingTimes="MWF 11:00AM - 11:50AM")

        section4.save()

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
        self.assertContains(response, self.course_model1.getParentCourse())
        self.assertContains(response, self.course_model1.getSectionNumber())
        self.assertContains(response, self.course_model1.getMeetTime())
        self.assertContains(response, self.course_model1.getTA())

    def test_ViewCourseSummerCourseSectionSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course_model2.getParentCourse())
        self.assertContains(response, self.course_model2.getSectionNumber())
        self.assertContains(response, self.course_model2.getMeetTime())
        self.assertContains(response, self.course_model2.getTA())

    def test_ViewCourseWinterCourseSectionSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course_model3.getParentCourse())
        self.assertContains(response, self.course_model3.getSectionNumber())
        self.assertContains(response, self.course_model3.getMeetTime())
        self.assertContains(response, self.course_model3.getTA())

    def test_ViewCourseSpecialCourseSectionSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course_model4.getParentCourse())
        self.assertContains(response, self.course_model4.getSectionNumber())
        self.assertContains(response, self.course_model4.getMeetTime())
        self.assertContains(response, self.course_model4.getTA())

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
    ta = None

    def setUp(self):
        self.client = Client()
        self.course_model1 = Course.objects.create(name='Introduction to Programming I', semester='Spring', year=2022,
                                                   description='Intro to Programming', credits=4)
        section1 = Section.objects.create(course_ID=self.course_model1, section_num=100, TA="Davidson Peter",
                                          MeetingTimes="MWF 9:00AM - 9:50AM")
        self.course = CourseClass.ConcreteCourse(self.course_model1)
        self.wrapper = SectionClass.ConcreteSection(section1)
        section1.save()

        self.course_model2 = Course.objects.create(name='Introduction to Programming II', semester='Spring', year=2022,
                                                   description='Intro to Object-Oriented Principles', credits=4)
        section2 = Section.objects.create(course_ID=self.course_model2, section_num=200, TA="David Miles",
                                          MeetingTimes="MWF 10:00AM - 10:50AM")
        self.course = CourseClass.ConcreteCourse(self.course_model2)
        self.wrapper = SectionClass.ConcreteSection(section2)
        section2.save()

        self.course_model3 = Course.objects.create(name='Introduction to Programming III', semester='Spring', year=2022,
                                                   description='Data Structures', credits=4)
        section3 = Section.objects.create(course_ID=self.course_model3, section_num=300, TA="Jeffrey Adams",
                                          MeetingTimes="MWF 11:00AM - 11:50AM")

        section3.save()

        self.course_model4 = Course.objects.create(name='Introduction to Compilers', semester='Spring', year=2022,
                                                   description='Intro to Compiler Theory', credits=4)
        section4 = Section.objects.create(course_ID=self.course_model4, section_num=400, TA="Jeffrey Adams",
                                          MeetingTimes="MWF 11:00AM - 11:50AM")

        section4.save()

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
        self.assertContains(response, self.course_model1.getParentCourse())
        self.assertContains(response, self.course_model1.getSectionNumber())
        self.assertContains(response, self.course_model1.getMeetTime())
        self.assertContains(response, self.course_model1.getTA())

    def test_ViewCourseSummerCourseSectionSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course_model2.getParentCourse())
        self.assertContains(response, self.course_model2.getSectionNumber())
        self.assertContains(response, self.course_model2.getMeetTime())
        self.assertContains(response, self.course_model2.getTA())

    def test_ViewCourseWinterCourseSectionSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course_model3.getParentCourse())
        self.assertContains(response, self.course_model3.getSectionNumber())
        self.assertContains(response, self.course_model3.getMeetTime())
        self.assertContains(response, self.course_model3.getTA())

    def test_ViewCourseSpecialCourseSectionSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course_model4.getParentCourse())
        self.assertContains(response, self.course_model4.getSectionNumber())
        self.assertContains(response, self.course_model4.getMeetTime())
        self.assertContains(response, self.course_model4.getTA())

    def test_Section_to_HomeSearch(self):
        # Make a GET request to /searchStates/UserSearch
        response = self.client.get("/Section")

        # Check that the response was a redirect to page /searchStates/SearchHome
        self.assertRedirects(response, 'home', status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

        # Follow the redirect and check that the final URL is '/searchStates/SearchHome'
        response = response.follow()
        self.assertEqual(response.url, 'home')

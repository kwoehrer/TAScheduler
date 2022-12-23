from django.test import TestCase, Client
from app.models import *
from classes.Users.users import AdminUser, InstructorUser, TAUser
from classes.Courses.CoursesClass import AbstractCourse, ConcreteCourse

'''
As an Admin, I want to be able to navigate to the Search Home page
----------------------------------------------------
Scenario: Navigate to the Course Search Page
GIVEN: The user is an Admin and is logged in and at the Course Results Page view
AND: They can click on "Return to Search Page"
THEN: They will be navigated to the "Search Home"
----------------------------------------------------
'''


class TestAdminSearchHomePage(TestCase):
    client = None
    admin = None

    def setUp(self):
        self.client = Client()
        spring_course = Course.objects.create(name="Introduction to Programming", semester="Spring", year="2022",
                                              description="Programming Analysis", instructor="Dr.Schulz", section="103",
                                              TA="Richard White")
        self.course1: AbstractCourse = ConcreteCourse(spring_course)
        spring_course.save()

        summer_course = Course.objects.create(name="Introduction to Programming II", semester="Summer", year="2022",
                                              description="Programming Analysis Advanced", instructor="Dr.Borland",
                                              section="203",
                                              TA="David Miles")
        self.course2: AbstractCourse = ConcreteCourse(summer_course)
        summer_course.save()

        winter_course = Course.objects.create(name="Introduction to Programming III", semester="Summer", year="2022",
                                              description="Data Structures and Algorithms", instructor="Dr.Page",
                                              section="303",
                                              TA="Jeffrey Adams")
        self.course3: AbstractCourse = ConcreteCourse(winter_course)
        winter_course.save()

        special_course = Course.objects.create(name="Introduction to Compilers", semester="Special", year="2022",
                                               description="Semantics and Parsing", instructor="Dr.Carter",
                                               section="403",
                                               TA="Cameroon Davis")
        self.course4: AbstractCourse = ConcreteCourse(special_course)
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

    def test_ViewCourseSpringCourseSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course1.get_course_id())
        self.assertContains(response, self.course1.get_course_name())
        self.assertContains(response, self.course1.get_semester())
        self.assertContains(response, self.course1.get_year())
        self.assertContains(response, self.course1.get_description())
        self.assertContains(response, self.course1.get_instructors())
        self.assertContains(response, self.course1.get_sections())
        self.assertContains(response, self.course1.get_tas())

    def test_ViewCourseSummerCourseSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course2.get_course_id())
        self.assertContains(response, self.course2.get_course_name())
        self.assertContains(response, self.course2.get_semester())
        self.assertContains(response, self.course2.get_year())
        self.assertContains(response, self.course2.get_description())
        self.assertContains(response, self.course2.get_instructors())
        self.assertContains(response, self.course2.get_sections())
        self.assertContains(response, self.course2.get_tas())

    def test_ViewCourseWinterCourseSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course3.get_course_id())
        self.assertContains(response, self.course3.get_course_name())
        self.assertContains(response, self.course3.get_semester())
        self.assertContains(response, self.course3.get_year())
        self.assertContains(response, self.course3.get_description())
        self.assertContains(response, self.course3.get_instructors())
        self.assertContains(response, self.course3.get_sections())
        self.assertContains(response, self.course3.get_tas())

    def test_ViewCourseSpecialCourseSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course4.get_course_id())
        self.assertContains(response, self.course4.get_course_name())
        self.assertContains(response, self.course4.get_semester())
        self.assertContains(response, self.course4.get_year())
        self.assertContains(response, self.course4.get_description())
        self.assertContains(response, self.course4.get_instructors())
        self.assertContains(response, self.course4.get_sections())
        self.assertContains(response, self.course4.get_tas())

    def test_CourseSearch_to_HomeSearch(self):
        # Make a GET request to /searchStates/UserSearch
        response = self.client.get("/searchStates/CourseSearchResults")

        # Check that the response was a redirect to page /searchStates/SearchHome
        self.assertRedirects(response, '/searchStates/SearchHome', status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

        # Follow the redirect and check that the final URL is '/searchStates/SearchHome'
        response = response.follow()
        self.assertEqual(response.url, '/searchStates/SearchHome')


'''
As an Instructor, I want to be able to navigate to the Search Home page
----------------------------------------------------
Scenario: Navigate to the Course Search Page
GIVEN: The user is an Instructor and is logged in and at the Course Results Page view
AND: They can click on "Return to Search Page"
THEN: They will be navigated to the "Search Home"
----------------------------------------------------
'''


class TestInstructorSearchHomePage(TestCase):
    client = None
    admin = None

    def setUp(self):
        self.client = Client()
        spring_course = Course.objects.create(name="Introduction to Programming", semester="Spring", year="2022",
                                              description="Programming Analysis", instructor="Dr.Schulz", section="103",
                                              TA="Richard White")
        self.course1: AbstractCourse = ConcreteCourse(spring_course)
        spring_course.save()

        summer_course = Course.objects.create(name="Introduction to Programming II", semester="Summer", year="2022",
                                              description="Programming Analysis Advanced", instructor="Dr.Borland",
                                              section="203",
                                              TA="David Miles")
        self.course2: AbstractCourse = ConcreteCourse(summer_course)
        summer_course.save()

        winter_course = Course.objects.create(name="Introduction to Programming III", semester="Summer", year="2022",
                                              description="Data Structures and Algorithms", instructor="Dr.Page",
                                              section="303",
                                              TA="Jeffrey Adams")
        self.course3: AbstractCourse = ConcreteCourse(winter_course)
        winter_course.save()

        special_course = Course.objects.create(name="Introduction to Compilers", semester="Special", year="2022",
                                               description="Semantics and Parsing", instructor="Dr.Carter",
                                               section="403",
                                               TA="Cameroon Davis")
        self.course4: AbstractCourse = ConcreteCourse(special_course)
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave',
                            user_type='Instructor',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_object)
        self.instructor: InstructorUser = InstructorUser(user_model)

        self.client.login(username='John_Doe', password='password')

    def test_ViewCourseSpringCourseSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course1.get_course_id())
        self.assertContains(response, self.course1.get_course_name())
        self.assertContains(response, self.course1.get_semester())
        self.assertContains(response, self.course1.get_year())
        self.assertContains(response, self.course1.get_description())
        self.assertContains(response, self.course1.get_instructors())
        self.assertContains(response, self.course1.get_sections())
        self.assertContains(response, self.course1.get_tas())

    def test_ViewCourseSummerCourseSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course2.get_course_id())
        self.assertContains(response, self.course2.get_course_name())
        self.assertContains(response, self.course2.get_semester())
        self.assertContains(response, self.course2.get_year())
        self.assertContains(response, self.course2.get_description())
        self.assertContains(response, self.course2.get_instructors())
        self.assertContains(response, self.course2.get_sections())
        self.assertContains(response, self.course2.get_tas())

    def test_ViewCourseWinterCourseSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course3.get_course_id())
        self.assertContains(response, self.course3.get_course_name())
        self.assertContains(response, self.course3.get_semester())
        self.assertContains(response, self.course3.get_year())
        self.assertContains(response, self.course3.get_description())
        self.assertContains(response, self.course3.get_instructors())
        self.assertContains(response, self.course3.get_sections())
        self.assertContains(response, self.course3.get_tas())

    def test_ViewCourseSpecialCourseSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course4.get_course_id())
        self.assertContains(response, self.course4.get_course_name())
        self.assertContains(response, self.course4.get_semester())
        self.assertContains(response, self.course4.get_year())
        self.assertContains(response, self.course4.get_description())
        self.assertContains(response, self.course4.get_instructors())
        self.assertContains(response, self.course4.get_sections())
        self.assertContains(response, self.course4.get_tas())

    def test_CourseSearch_to_HomeSearch(self):
        # Make a GET request to /searchStates/UserSearch
        response = self.client.get("/searchStates/CourseSearchResults")

        # Check that the response was a redirect to page /searchStates/SearchHome
        self.assertRedirects(response, '/searchStates/SearchHome', status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

        # Follow the redirect and check that the final URL is '/searchStates/SearchHome'
        response = response.follow()
        self.assertEqual(response.url, '/searchStates/SearchHome')


'''
As a TA, I want to be able to navigate to the Search Home page
----------------------------------------------------
Scenario: Navigate to the Course Search Page
GIVEN: The user is a TA and is logged in and at the Course Results Page view
AND: They can click on "Return to Search Page"
THEN: They will be navigated to the "Search Home"
----------------------------------------------------
'''


class TestATASearchHomePage(TestCase):
    client = None
    admin = None

    def setUp(self):
        self.client = Client()
        spring_course = Course.objects.create(name="Introduction to Programming", semester="Spring", year="2022",
                                              description="Programming Analysis", instructor="Dr.Schulz", section="103",
                                              TA="Richard White")
        self.course1: AbstractCourse = ConcreteCourse(spring_course)
        spring_course.save()

        summer_course = Course.objects.create(name="Introduction to Programming II", semester="Summer", year="2022",
                                              description="Programming Analysis Advanced", instructor="Dr.Borland",
                                              section="203",
                                              TA="David Miles")
        self.course2: AbstractCourse = ConcreteCourse(summer_course)
        summer_course.save()

        winter_course = Course.objects.create(name="Introduction to Programming III", semester="Summer", year="2022",
                                              description="Data Structures and Algorithms", instructor="Dr.Page",
                                              section="303",
                                              TA="Jeffrey Adams")
        self.course3: AbstractCourse = ConcreteCourse(winter_course)
        winter_course.save()

        special_course = Course.objects.create(name="Introduction to Compilers", semester="Special", year="2022",
                                               description="Semantics and Parsing", instructor="Dr.Carter",
                                               section="403",
                                               TA="Cameroon Davis")
        self.course4: AbstractCourse = ConcreteCourse(special_course)
        User.objects.create(username='John_Doe', password="password", first_name="John",
                            last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave',
                            user_type='TA',
                            email='johnDoe@aol.com')
        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = TA.objects.create(account_ID=user_object)
        self.admin: TAUser = TAUser(user_model)

        self.client.login(username='John_Doe', password='password')

    def test_ViewCourseSpringCourseSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course1.get_course_id())
        self.assertContains(response, self.course1.get_course_name())
        self.assertContains(response, self.course1.get_semester())
        self.assertContains(response, self.course1.get_year())
        self.assertContains(response, self.course1.get_description())
        self.assertContains(response, self.course1.get_instructors())
        self.assertContains(response, self.course1.get_sections())
        self.assertContains(response, self.course1.get_tas())

    def test_ViewCourseSummerCourseSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course2.get_course_id())
        self.assertContains(response, self.course2.get_course_name())
        self.assertContains(response, self.course2.get_semester())
        self.assertContains(response, self.course2.get_year())
        self.assertContains(response, self.course2.get_description())
        self.assertContains(response, self.course2.get_instructors())
        self.assertContains(response, self.course2.get_sections())
        self.assertContains(response, self.course2.get_tas())

    def test_ViewCourseWinterCourseSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course3.get_course_id())
        self.assertContains(response, self.course3.get_course_name())
        self.assertContains(response, self.course3.get_semester())
        self.assertContains(response, self.course3.get_year())
        self.assertContains(response, self.course3.get_description())
        self.assertContains(response, self.course3.get_instructors())
        self.assertContains(response, self.course3.get_sections())
        self.assertContains(response, self.course3.get_tas())

    def test_ViewCourseSpecialCourseSummary(self):
        response = self.client.get('/searchStates/CourseSummary')
        self.assertContains(response, self.course4.get_course_id())
        self.assertContains(response, self.course4.get_course_name())
        self.assertContains(response, self.course4.get_semester())
        self.assertContains(response, self.course4.get_year())
        self.assertContains(response, self.course4.get_description())
        self.assertContains(response, self.course4.get_instructors())
        self.assertContains(response, self.course4.get_sections())
        self.assertContains(response, self.course4.get_tas())

    def test_CourseSearch_to_HomeSearch(self):
        # Make a GET request to /searchStates/UserSearch
        response = self.client.get("/searchStates/CourseSearchResults")

        # Check that the response was a redirect to page /searchStates/SearchHome
        self.assertRedirects(response, '/searchStates/SearchHome', status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

        # Follow the redirect and check that the final URL is '/searchStates/SearchHome'
        response = response.follow()
        self.assertEqual(response.url, '/searchStates/SearchHome')

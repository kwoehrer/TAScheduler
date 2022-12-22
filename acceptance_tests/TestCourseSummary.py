from django.test import TestCase, Client
from app.models import *
from classes.Users.users import AdminUser, InstructorUser, TAUser
from classes.Courses.CoursesClass import AbstractCourse, ConcreteCourse

'''
As an Admin, I want to be able navigate the Course Search Summary Page
-----------------------------------------------------------------------
SCENARIO: As an Admin, I want to be able to correctly view course information if I log into the Course Search Summary page
GIVEN The user is an Admin and is logged in and at the Course Search Summary page
THEN all courses should be displayed with correct information
-----------------------------------------------------------------------
'''


class TestCourseSearchAdmin(TestCase):
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
                            user_type='Admin',
                            email='johnDoe@aol.com')

        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.admin: AdminUser = AdminUser(user_model)
        user_model.save()

        self.client.post("/", {"username": self.admin.getUsername(), "password": self.admin.getPassword()})

    def test_ViewCourseCourseSummary(self):
        courses = [self.course1, self.course2, self.course3, self.course4]
        response = self.client.get('/some-page/')
        for course in courses:
            self.assertContains(response, course.get_course_id())
            self.assertContains(response, course.get_course_name())
            self.assertContains(response, course.get_semester())
            self.assertContains(response, course.get_year())
            self.assertContains(response, course.get_description())
            self.assertContains(response, course.get_instructors())
            self.assertContains(response, course.get_sections())
            self.assertContains(response, course.get_tas())


'''
As an Instructor, I want to be able navigate the Course Search Summary Page
-----------------------------------------------------------------------
SCENARIO: As an Instructor, I want to be able to correctly view course information if I log into the Course Search Summary page
GIVEN The user is an Instructor and is logged in and at the Course Search Summary page
THEN all courses should be displayed with correct information
-----------------------------------------------------------------------
'''


class TestCourseSearchInstructor(TestCase):
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
                            user_type='Admin',
                            email='johnDoe@aol.com')

        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_object)
        self.instructor: InstructorUser = InstructorUser(user_model)
        user_model.save()

        self.client.post("/", {"username": self.instructor.getUsername(), "password": self.instructor.getPassword()})

    def test_ViewCourseCourseSummary(self):
        courses = [self.course1, self.course2, self.course3, self.course4]
        response = self.client.get('/some-page/')
        for course in courses:
            self.assertContains(response, course.get_course_id())
            self.assertContains(response, course.get_course_name())
            self.assertContains(response, course.get_semester())
            self.assertContains(response, course.get_year())
            self.assertContains(response, course.get_description())
            self.assertContains(response, course.get_instructors())
            self.assertContains(response, course.get_sections())
            self.assertContains(response, course.get_tas())


'''
As a TA, I want to be able navigate the Course Search Summary Page
-----------------------------------------------------------------------
SCENARIO: As a TA, I want to be able to correctly view course information if I log into the Course Search Summary page
GIVEN The user is a TA and is logged in and at the Course Search Summary page
THEN all courses should be displayed with correct information
-----------------------------------------------------------------------
'''


class TestCourseSearchTA(TestCase):
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
        self.ta: TAUser = TAUser(user_model)
        user_model.save()

        self.client.post("/", {"username": self.ta.getUsername(), "password": self.ta.getPassword()})

    def test_ViewCourseCourseSummary(self):
        courses = [self.course1, self.course2, self.course3, self.course4]
        response = self.client.get('/some-page/')
        for course in courses:
            self.assertContains(response, course.get_course_id())
            self.assertContains(response, course.get_course_name())
            self.assertContains(response, course.get_semester())
            self.assertContains(response, course.get_year())
            self.assertContains(response, course.get_description())
            self.assertContains(response, course.get_instructors())
            self.assertContains(response, course.get_sections())
            self.assertContains(response, course.get_tas())

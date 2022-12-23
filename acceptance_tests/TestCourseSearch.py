from django.test import TestCase, Client
from app.models import *
from classes.Users.users import AdminUser, InstructorUser, TAUser
from classes.Courses.CoursesClass import AbstractCourse, ConcreteCourse

'''
As an Admin, I want to be able navigate the Users Page and Query a Course
-----------------------------------------------------------------------
SCENARIO: As an Admin, I want to be able to navigate to the Course Search page
GIVEN The user is an Admin and is logged in and at the Course Search page
WHEN a course is of type Fall needs to be queried
WHEN course can be found with valid fields in a list of all courses
AND "Search for Course" is clicked
THEN course can be viewed
-----------------------------------------------------------------------
SCENARIO: As an Admin, I want to be able to navigate to the Course Search page
GIVEN The user is an Admin and is logged in and at the Course Search page
WHEN a course is of type Spring needs to be queried
WHEN course can be found with valid fields in a list of all courses
AND "Search for Course" is clicked
THEN course can be viewed
-----------------------------------------------------------------------
SCENARIO: As an Admin, I want to be able to navigate to the Course Search page
GIVEN The user is an Admin and is logged in and at the Course Search page
WHEN a course is of type Winter needs to be queried
WHEN course can be found with valid fields in a list of all courses
AND "Search for Course" is clicked
THEN course can be viewed
-----------------------------------------------------------------------
SCENARIO: As an Admin, I want to be able to navigate to the Course Search page
GIVEN The user is an Admin and is logged in and at the Course Search page
WHEN a course is of type Special needs to be queried
WHEN course can be found with valid fields in a list of all courses
AND "Search for Course" is clicked
THEN course can be viewed
-----------------------------------------------------------------------
As an Admin, I want to be able navigate to the Search Home Page
-----------------------------------------------------------------------
Scenario: As an Admin, I am currently in the Course Search Page
GIVEN: The user is an Admin and is logged in and at the Course Search page
AND:They can click on "Return to Search Page"
THEN: They will be navigated to the "Search Home" page
'''


class TestCourseSearchAdmin(TestCase):
    def setUp(self):
        self.client = Client()

        spring_course = Course.objects.create(name="Introduction to Programming", semester="Spring", year="2022",
                                              description="Programming Analysis", credits="3")
        self.course1: AbstractCourse = ConcreteCourse(spring_course)
        spring_course.save()

        summer_course = Course.objects.create(name="Introduction to Programming II", semester="Summer", year="2022",
                                              description="Programming Analysis Advanced", credits="3")
        self.course2: AbstractCourse = ConcreteCourse(summer_course)
        summer_course.save()

        winter_course = Course.objects.create(name="Introduction to Programming III", semester="Summer", year="2022",
                                              description="Data Structures and Algorithms", credits="3")
        self.course3: AbstractCourse = ConcreteCourse(winter_course)
        winter_course.save()

        special_course = Course.objects.create(name="Introduction to Compilers", semester="Special", year="2022",
                                               description="Semantics and Parsing", credits="3")
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
        user_model.save()

        self.client.post("/", {"username": self.admin.getUsername(), "password": self.admin.getPassword()})

    def test_EmptyName(self):
        resp = self.client.post('/searchStates/CourseSearch',
                                {"name": " ", "semester": "Summer", "year": "2022",
                                 "description": "Programming Analysis", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for name field",
                         "An error message was not displayed when name was left blank")

    def test_EmptySemester(self):
        resp = self.client.post('/searchStates/CourseSearch',
                                {"name": "Introduction to Programming", "semester": " ", "year": "2022",
                                 "description": "Programming Analysis", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for semester field",
                         "An error message was not displayed when semester was left blank")

    def test_EmptyYear(self):
        resp = self.client.post('/searchStates/CourseSearch',
                                {"name": "Introduction to Programming", "semester": "Summer", "year": "2022",
                                 "description": " ", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for description field",
                         "An error message was not displayed when description was left blank")

    def test_InvalidName(self):
        resp = self.client.post('/searchStates/CourseSearch',
                                {"name": "123", "semester": "Summer", "year": "2022",
                                 "description": "Programming Analysis", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for name field",
                         "An error message was not displayed when name had invalid type")

    def test_InvalidSemester(self):
        resp = self.client.post('/searchStates/CourseSearch',
                                {"name": "Introduction to Programming", "semester": "123", "year": "2022",
                                 "description": "Programming Analysis", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for semester field",
                         "An error message was not displayed when semester had invalid type")

    def test_InvalidYear(self):
        resp = self.client.post('/searchStates/CourseSearch',
                                {"name": "Introduction to Programming", "semester": "Summer", "year": "123",
                                 "description": "Programming Analysis", "credits": "Name"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for name field",
                         "An error message was not displayed when year had invalid type")

    def test_querySpringCourse(self):
        self.client.post('/searchStates/CourseSearch',
                         {"name": "Introduction to Programming", "semester": "Spring", "year": "2022",
                          "description": "Programming Analysis", "credits": "3"})

        self.assertEqual(Course.objects.get(name="Introduction to Programming", semester="Summer", year="2022",
                                            description="Programming Analysis", credits="3").name,
                         self.course1,
                         msg="Course was not successfully queried")

    def test_querySummerCourse(self):
        self.client.post('/searchStates/CourseSearch',
                         {"name": "Introduction to Programming II", "semester": "Summer", "year": "2022",
                          "description": "Programming Analysis Advanced", "credits": "3"})

        self.assertEqual(Course.objects.get(name="Introduction to Programming II", semester="Summer", year="2022",
                                            description="Programming Analysis Advanced", credits="3").name,
                         self.course2,
                         msg="Course was not successfully queried")

    def test_queryWinterCourse(self):
        self.client.post('/searchStates/CourseSearch',
                         {"name": "Introduction to Programming III", "semester": "Summer", "year": "2022",
                          "description": "Data Structures and Algorithms", "credits": "3"})

        self.assertEqual(Course.objects.get(name="Introduction to Programming III", semester="Summer", year="2022",
                                            description="Data Structures and Algorithms", credits="3").name,
                         self.course3,
                         msg="Course was not successfully queried")

    def test_querySpecialCourse(self):
        self.client.post('/searchStates/CourseSearch',
                         {"name": "Introduction to Compilers", "semester": "Special", "year": "2022",
                          "description": "Semantics and Parsing", "credits": "3"})

        self.assertEqual(Course.objects.create(name="Introduction to Compilers", semester="Special", year="2022",
                                               description="Semantics and Parsing", credits="3"),
                         self.course4,
                         msg="Course was not successfully queried")


'''
As an Instructor, I want to be able navigate the Users Page and Query a Course
-----------------------------------------------------------------------
SCENARIO: As an AInstructor, I want to be able to navigate to the Course Search page
GIVEN The user is an Instructor and is logged in and at the Course Search page
WHEN a course is of type Fall needs to be queried
WHEN course can be found with valid fields in a list of all courses
AND "Search for Course" is clicked
THEN course can be viewed
-----------------------------------------------------------------------
SCENARIO: As an Instructor, I want to be able to navigate to the Course Search page
GIVEN The user is an Instructor and is logged in and at the Course Search page
WHEN a course is of type Spring needs to be queried
WHEN course can be found with valid fields in a list of all courses
AND "Search for Course" is clicked
THEN course can be viewed
-----------------------------------------------------------------------
SCENARIO: As an Instructor, I want to be able to navigate to the Course Search page
GIVEN The user is an Instructor and is logged in and at the Course Search page
WHEN a course is of type Winter needs to be queried
WHEN course can be found with valid fields in a list of all courses
AND "Search for Course" is clicked
THEN course can be viewed
-----------------------------------------------------------------------
SCENARIO: As an Instructor, I want to be able to navigate to the Course Search page
GIVEN The user is an Instructor and is logged in and at the Course Search page
WHEN a course is of type Special needs to be queried
WHEN course can be found with valid fields in a list of all courses
AND "Search for Course" is clicked
THEN course can be viewed
-----------------------------------------------------------------------
As an Instructor, I want to be able navigate to the Search Home Page
-----------------------------------------------------------------------
Scenario: As an Instructor, I am currently in the Course Search Page
GIVEN: The user is an Admin and is logged in and at the Course Search page
AND:They can click on "Return to Search Page"
THEN: They will be navigated to the "Search Home" page
'''


class TestCourseSearchInstructor(TestCase):
    def setUp(self):
        self.client = Client()

        spring_course = Course.objects.create(name="Introduction to Programming", semester="Spring", year="2022",
                                              description="Programming Analysis", credits="3")
        self.course1: AbstractCourse = ConcreteCourse(spring_course)
        spring_course.save()

        summer_course = Course.objects.create(name="Introduction to Programming II", semester="Summer", year="2022",
                                              description="Programming Analysis Advanced", credits="3")
        self.course2: AbstractCourse = ConcreteCourse(summer_course)
        summer_course.save()

        winter_course = Course.objects.create(name="Introduction to Programming III", semester="Summer", year="2022",
                                              description="Data Structures and Algorithms", credits="3")
        self.course3: AbstractCourse = ConcreteCourse(winter_course)
        winter_course.save()

        special_course = Course.objects.create(name="Introduction to Compilers", semester="Special", year="2022",
                                               description="Semantics and Parsing", credits="3")
        self.course4: AbstractCourse = ConcreteCourse(special_course)
        special_course.save()

        User.objects.create(username='John_Doe', password="password", first_name="John",
                            last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave',
                            user_type='Instructor',
                            email='johnDoe@aol.com')

        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Instructor.objects.create(account_ID=user_object)
        self.instructor: InstructorUser = InstructorUser(user_model)
        user_model.save()

        self.client.post("/", {"username": self.instructor.getUsername(), "password": self.instructor.getPassword()})

    def test_EmptyName(self):
        resp = self.client.post('/searchStates/CourseSearch',
                                {"name": " ", "semester": "Summer", "year": "2022",
                                 "description": "Programming Analysis", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for name field",
                         "An error message was not displayed when name was left blank")

    def test_EmptySemester(self):
        resp = self.client.post('/searchStates/CourseSearch',
                                {"name": "Introduction to Programming", "semester": " ", "year": "2022",
                                 "description": "Programming Analysis", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for semester field",
                         "An error message was not displayed when semester was left blank")

    def test_EmptyYear(self):
        resp = self.client.post('/searchStates/CourseSearch',
                                {"name": "Introduction to Programming", "semester": "Summer", "year": "2022",
                                 "description": " ", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for description field",
                         "An error message was not displayed when description was left blank")

    def test_InvalidName(self):
        resp = self.client.post('/searchStates/CourseSearch',
                                {"name": "123", "semester": "Summer", "year": "2022",
                                 "description": "Programming Analysis", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for name field",
                         "An error message was not displayed when name had invalid type")

    def test_InvalidSemester(self):
        resp = self.client.post('/searchStates/CourseSearch',
                                {"name": "Introduction to Programming", "semester": "123", "year": "2022",
                                 "description": "Programming Analysis", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for semester field",
                         "An error message was not displayed when semester had invalid type")

    def test_InvalidYear(self):
        resp = self.client.post('/searchStates/CourseSearch',
                                {"name": "Introduction to Programming", "semester": "Summer", "year": "123",
                                 "description": "Programming Analysis", "credits": "Name"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for name field",
                         "An error message was not displayed when year had invalid type")

    def test_querySpringCourse(self):
        self.client.post('/searchStates/CourseSearch',
                         {"name": "Introduction to Programming", "semester": "Spring", "year": "2022",
                          "description": "Programming Analysis", "credits": "3"})

        self.assertEqual(Course.objects.get(name="Introduction to Programming", semester="Summer", year="2022",
                                            description="Programming Analysis", credits="3").name,
                         self.course1,
                         msg="Course was not successfully queried")

    def test_querySummerCourse(self):
        self.client.post('/searchStates/CourseSearch',
                         {"name": "Introduction to Programming II", "semester": "Summer", "year": "2022",
                          "description": "Programming Analysis Advanced", "credits": "3"})

        self.assertEqual(Course.objects.get(name="Introduction to Programming II", semester="Summer", year="2022",
                                            description="Programming Analysis Advanced", credits="3").name,
                         self.course2,
                         msg="Course was not successfully queried")

    def test_queryWinterCourse(self):
        self.client.post('/searchStates/CourseSearch',
                         {"name": "Introduction to Programming III", "semester": "Summer", "year": "2022",
                          "description": "Data Structures and Algorithms", "credits": "3"})

        self.assertEqual(Course.objects.get(name="Introduction to Programming III", semester="Summer", year="2022",
                                            description="Data Structures and Algorithms", credits="3").name,
                         self.course3,
                         msg="Course was not successfully queried")

    def test_querySpecialCourse(self):
        self.client.post('/searchStates/CourseSearch',
                         {"name": "Introduction to Compilers", "semester": "Special", "year": "2022",
                          "description": "Semantics and Parsing", "credits": "3"})

        self.assertEqual(Course.objects.create(name="Introduction to Compilers", semester="Special", year="2022",
                                               description="Semantics and Parsing", credits="3"),
                         self.course4,
                         msg="Course was not successfully queried")


'''
As a TA, I want to be able navigate the Users Page and Query a Course
-----------------------------------------------------------------------
SCENARIO: As a TA, I want to be able to navigate to the Course Search page
GIVEN The user is a TA and is logged in and at the Course Search page
WHEN a course is of type Fall needs to be queried
WHEN course can be found with valid fields in a list of all courses
AND "Search for Course" is clicked
THEN course can be viewed
-----------------------------------------------------------------------
SCENARIO: As a TA, I want to be able to navigate to the Course Search page
GIVEN The user is a TA and is logged in and at the Course Search page
WHEN a course is of type Spring needs to be queried
WHEN course can be found with valid fields in a list of all courses
AND "Search for Course" is clicked
THEN course can be viewed
-----------------------------------------------------------------------
SCENARIO: As a TA, I want to be able to navigate to the Course Search page
GIVEN The user is a TA and is logged in and at the Course Search page
WHEN a course is of type Winter needs to be queried
WHEN course can be found with valid fields in a list of all courses
AND "Search for Course" is clicked
THEN course can be viewed
-----------------------------------------------------------------------
SCENARIO: As a TA, I want to be able to navigate to the Course Search page
GIVEN The user is a TA and is logged in and at the Course Search page
WHEN a course is of type Special needs to be queried
WHEN course can be found with valid fields in a list of all courses
AND "Search for Course" is clicked
THEN course can be viewed
-----------------------------------------------------------------------
As a TA, I want to be able navigate to the Search Home Page
-----------------------------------------------------------------------
Scenario: As a TA, I am currently in the Course Search Page
GIVEN: The user is a TA and is logged in and at the Course Search page
AND:They can click on "Return to Search Page"
THEN: They will be navigated to the "Search Home" page
'''


class TestCourseSearchTA(TestCase):
    def setUp(self):
        self.client = Client()

        spring_course = Course.objects.create(name="Introduction to Programming", semester="Spring", year="2022",
                                              description="Programming Analysis", credits="3")
        self.course1: AbstractCourse = ConcreteCourse(spring_course)
        spring_course.save()

        summer_course = Course.objects.create(name="Introduction to Programming II", semester="Summer", year="2022",
                                              description="Programming Analysis Advanced", credits="3")
        self.course2: AbstractCourse = ConcreteCourse(summer_course)
        summer_course.save()

        winter_course = Course.objects.create(name="Introduction to Programming III", semester="Summer", year="2022",
                                              description="Data Structures and Algorithms", credits="3")
        self.course3: AbstractCourse = ConcreteCourse(winter_course)
        winter_course.save()

        special_course = Course.objects.create(name="Introduction to Compilers", semester="Special", year="2022",
                                               description="Semantics and Parsing", credits="3")
        self.course4: AbstractCourse = ConcreteCourse(special_course)
        special_course.save()

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

    def test_EmptyName(self):
        resp = self.client.post('/searchStates/CourseSearch',
                                {"name": " ", "semester": "Summer", "year": "2022",
                                 "description": "Programming Analysis", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for name field",
                         "An error message was not displayed when name was left blank")

    def test_EmptySemester(self):
        resp = self.client.post('/searchStates/CourseSearch',
                                {"name": "Introduction to Programming", "semester": " ", "year": "2022",
                                 "description": "Programming Analysis", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for semester field",
                         "An error message was not displayed when semester was left blank")

    def test_EmptyYear(self):
        resp = self.client.post('/searchStates/CourseSearch',
                                {"name": "Introduction to Programming", "semester": "Summer", "year": "2022",
                                 "description": " ", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for description field",
                         "An error message was not displayed when description was left blank")

    def test_InvalidName(self):
        resp = self.client.post('/searchStates/CourseSearch',
                                {"name": "123", "semester": "Summer", "year": "2022",
                                 "description": "Programming Analysis", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for name field",
                         "An error message was not displayed when name had invalid type")

    def test_InvalidSemester(self):
        resp = self.client.post('/searchStates/CourseSearch',
                                {"name": "Introduction to Programming", "semester": "123", "year": "2022",
                                 "description": "Programming Analysis", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for semester field",
                         "An error message was not displayed when semester had invalid type")

    def test_InvalidYear(self):
        resp = self.client.post('/searchStates/CourseSearch',
                                {"name": "Introduction to Programming", "semester": "Summer", "year": "123",
                                 "description": "Programming Analysis", "credits": "Name"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for name field",
                         "An error message was not displayed when year had invalid type")

    def test_querySpringCourse(self):
        self.client.post('/searchStates/CourseSearch',
                         {"name": "Introduction to Programming", "semester": "Spring", "year": "2022",
                          "description": "Programming Analysis", "credits": "3"})

        self.assertEqual(Course.objects.get(name="Introduction to Programming", semester="Summer", year="2022",
                                            description="Programming Analysis", credits="3").name,
                         self.course1,
                         msg="Course was not successfully queried")

    def test_querySummerCourse(self):
        self.client.post('/searchStates/CourseSearch',
                         {"name": "Introduction to Programming II", "semester": "Summer", "year": "2022",
                          "description": "Programming Analysis Advanced", "credits": "3"})

        self.assertEqual(Course.objects.get(name="Introduction to Programming II", semester="Summer", year="2022",
                                            description="Programming Analysis Advanced", credits="3").name,
                         self.course2,
                         msg="Course was not successfully queried")

    def test_queryWinterCourse(self):
        self.client.post('/searchStates/CourseSearch',
                         {"name": "Introduction to Programming III", "semester": "Summer", "year": "2022",
                          "description": "Data Structures and Algorithms", "credits": "3"})

        self.assertEqual(Course.objects.get(name="Introduction to Programming III", semester="Summer", year="2022",
                                            description="Data Structures and Algorithms", credits="3").name,
                         self.course3,
                         msg="Course was not successfully queried")

    def test_querySpecialCourse(self):
        self.client.post('/searchStates/CourseSearch',
                         {"name": "Introduction to Compilers", "semester": "Special", "year": "2022",
                          "description": "Semantics and Parsing", "credits": "3"})

        self.assertEqual(Course.objects.create(name="Introduction to Compilers", semester="Special", year="2022",
                                               description="Semantics and Parsing", credits="3"),
                         self.course4,
                         msg="Course was not successfully queried")

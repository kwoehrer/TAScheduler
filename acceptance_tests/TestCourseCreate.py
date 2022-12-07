from django.test import TestCase, Client

from app.models import Course, User, Admin
from classes.Courses.CoursesClass import ConcreteCourse, AbstractCourse
from classes.Users.users import AdminUser

'''
SCENARIO: As an Admin, I want to be able to navigate to the Create Account page
---------------------------------------------------------------------------------
Acceptance Criteria 1:
GIVEN course has an existing ID in the database
WHEN a valid fields are entered
AND a course with the same fields already exists
THEN course is not created
---------------------------------------------------------------------------------
Acceptance Criteria 2:
GIVEN course has an existing ID in the database
WHEN the fields are entered
AND and one of the fields are invalid
THEN course is not created
---------------------------------------------------------------------------------
Acceptance Criteria 3:
GIVEN course has an existing ID in the database
WHEN the fields are entered
AND and one of the fields is not provided
THEN course is not created
---------------------------------------------------------------------------------
Acceptance Criteria 4:
GIVEN The course has an existing ID in the database
WHEN user enters valid fields
AND specifies course type as Spring
THEN course of type Spring is created
---------------------------------------------------------------------------------
Acceptance Criteria 5:
GIVEN The course has an existing ID in the database
WHEN user enters valid fields
AND specifies course type as Summer
THEN course of type Summer is created
---------------------------------------------------------------------------------
Acceptance Criteria 6:
GIVEN The course has an existing ID in the database
WHEN user enters valid fields
AND specifies course type as Winter
THEN course of type Winter is created
---------------------------------------------------------------------------------
Acceptance Criteria 7:
GIVEN The course has an existing ID in the database
WHEN user enters valid fields
AND specifies course type as Special
THEN course of type Special is created
---------------------------------------------------------------------------------
SCENARIO: As an Admin, I want to be able to navigate to the Create Account page
----------------------------------------------------
GIVEN: The user is an Admin and is logged in and at the home page
AND:They can click on "Return to Course Management Page"
THEN: They will be navigated to the "Course Management" page
----------------------------------------------------
'''


class TestCreateCourse(TestCase):

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

    def test_duplicateCourse(self):
        new_course = Course.objects.create(self.course1)
        self.course1: AbstractCourse = ConcreteCourse(new_course)
        new_course.save()

        resp = self.client.post('/CourseCreate/',
                                {new_course})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Duplicate Course already exists")
        self.assertEqual(self.course1.get_course_id(), Course.objects.get(account_ID=self.course1).course_ID,
                         "Database was "
                         "not changed")

    def test_EmptyName(self):
        resp = self.client.post('/CourseCreate/',
                                {"name": " ", "semester": "Summer", "year": "2022",
                                 "description": "Programming Analysis", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for name field",
                         "An error message was not displayed when name was left blank")

    def test_EmptySemester(self):
        resp = self.client.post('/CourseCreate/',
                                {"name": "Introduction to Programming", "semester": " ", "year": "2022",
                                 "description": "Programming Analysis", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for semester field",
                         "An error message was not displayed when semester was left blank")

    def test_EmptyYear(self):
        resp = self.client.post('/CourseCreate/',
                                {"name": "Introduction to Programming", "semester": "Summer", "year": "2022",
                                 "description": " ", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for description field",
                         "An error message was not displayed when description was left blank")

    def test_EmptyDescription(self):
        resp = self.client.post('/CourseCreate/',
                                {"name": "Introduction to Programming", "semester": "Summer", "year": "2022",
                                 "description": "Programming Analysis", "credits": " "})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for credit field",
                         "An error message was not displayed when name was left blank")

    def test_EmptyCredits(self):
        resp = self.client.post('/CourseCreate/',
                                {"name": " ", "semester": "Summer", "year": "2022",
                                 "description": "Programming Analysis", "credits": " "})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for name field",
                         "An error message was not displayed when name was left blank")

    def test_InvalidName(self):
        resp = self.client.post('/CourseCreate/',
                                {"name": "123", "semester": "Summer", "year": "2022",
                                 "description": "Programming Analysis", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for name field",
                         "An error message was not displayed when name had invalid type")

    def test_InvalidSemester(self):
        resp = self.client.post('/CourseCreate/',
                                {"name": "Introduction to Programming", "semester": "123", "year": "2022",
                                 "description": "Programming Analysis", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for semester field",
                         "An error message was not displayed when semester had invalid type")

    def test_InvalidYear(self):
        resp = self.client.post('/CourseCreate/',
                                {"name": "Introduction to Programming", "semester": "Summer", "year": "123",
                                 "description": "Programming Analysis", "credits": "Name"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for name field",
                         "An error message was not displayed when year had invalid type")

    def test_InvalidDescription(self):
        resp = self.client.post('/CourseCreate/',
                                {"name": "Introduction to Programming", "semester": "Summer", "year": "2022",
                                 "description": "123", "credits": "Name"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for name field",
                         "An error message was not displayed when description had invalid type")

    def test_InvalidCredits(self):
        resp = self.client.post('/CourseCreate/',
                                {"name": "Introduction to Programming", "semester": "Summer", "year": "2022",
                                 "description": "Programming Analysis", "credits": "Name"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for name field",
                         "An error message was not displayed when credit had invalid type")

    def test_createSpringCourse(self):
        self.client.post('/CourseCreate/',
                         {"name": "Introduction to Programming", "semester": "Spring", "year": "2022",
                          "description": "Programming Analysis", "credits": "3"})

        self.assertEqual(Course.objects.create(name="Introduction to Programming", semester="Summer", year="2022",
                                               description="Programming Analysis", credits="3").name,
                         self.course1.get_course_name(),
                         msg="Course was not successfully created")

    def test_createSummerCourse(self):
        self.client.post('/CourseCreate/',
                         {"name": "Introduction to Programming II", "semester": "Summer", "year": "2022",
                          "description": "Programming Analysis Advanced", "credits": "3"})

        self.assertEqual(Course.objects.create(name="Introduction to Programming II", semester="Summer", year="2022",
                                               description="Programming Analysis Advanced", credits="3").name,
                         self.course2.get_course_name(),
                         msg="Course was not successfully created")

    def test_createWinterCourse(self):
        self.client.post('/CourseCreate/',
                         {"name": "Introduction to Programming III", "semester": "Summer", "year": "2022",
                          "description": "Data Structures and Algorithms", "credits": "3"})

        self.assertEqual(Course.objects.create(name="Introduction to Programming III", semester="Summer", year="2022",
                                               description="Data Structures and Algorithms", credits="3").name,
                         self.course3.get_course_name(),
                         msg="Course was not successfully created")

    def test_createSpecialCourse(self):
        self.client.post('/CourseCreate/',
                         {"name": "Introduction to Compilers", "semester": "Special", "year": "2022",
                          "description": "Semantics and Parsing", "credits": "3"})

        self.assertEqual(Course.objects.create(name="Introduction to Compilers", semester="Special", year="2022",
                                               description="Semantics and Parsing", credits="3"),
                         self.course4.get_course_name(),
                         msg="Course was not successfully created")


class TestDeleteAccountPage(TestCase):

    def test_CourseCreate_to_Course_Management(self):

        response = self.client.post('/', {'username': 'Micheal_Johnson', 'password': 'password3'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "/AccountDelete")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/AdminCourseMng")

        try:
            self.assertTrue(response.url, "/AdminCourseMng")
        except AssertionError as msg:
            print(msg)

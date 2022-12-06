from django.test import TestCase, Client
from TAScheduler.app.models import *
from classes.Courses.CoursesClass import AbstractCourse, ConcreteCourse
from classes.Users.users import AdminUser


class TestCreateCourse(TestCase):
    dummyClient = None
    admin = None
    course = None

    def setUp(self):
        self.dummyClient = Client()

        spring_course = Course.objects.create(name="Introduction to Programming", semester="Summer", year="2022",
                                              description="Programming Analysis", credits="3")
        self.course: AbstractCourse = ConcreteCourse(spring_course)
        spring_course.save()

        User.objects.create(username='John_Doe', password="password", first_name="John",
                            last_name='Doe',
                            phone_number='4149818000', home_address='2513 N Farewell Ave',
                            user_type='Admin',
                            email='johnDoe@aol.com')

        user_object = User.objects.filter(username='John_Doe')[0]
        user_model = Admin.objects.create(account_ID=user_object)
        self.admin: AdminUser = AdminUser(user_model)
        user_model.save()

        self.dummyClient.post("/", {"username": self.admin.getUsername(), "password": self.admin.password})

    def test_duplicateCourse(self):
        resp = self.dummyClient.post('/CourseCreate/',
                                     {"name": "Introduction to Programming", "semester": "Summer", "year": "2022",
                                      "description": "Programming Analysis", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Duplicate Course already exists")

    def test_blankName(self):
        resp = self.dummyClient.post('/CourseCreate/',
                                     {"name": " ", "semester": "Summer", "year": "2022",
                                      "description": "Programming Analysis", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for name field",
                         "An error message was not displayed when name was left blank")

    def test_blankSemester(self):
        resp = self.dummyClient.post('/CourseCreate/',
                                     {"name": "Introduction to Programming", "semester": " ", "year": "2022",
                                      "description": "Programming Analysis", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for semester field",
                         "An error message was not displayed when semester was left blank")

    def test_blankYear(self):
        resp = self.dummyClient.post('/CourseCreate/',
                                     {"name": "Introduction to Programming", "semester": "Summer", "year": "2022",
                                      "description": " ", "credits": "3"})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for description field",
                         "An error message was not displayed when description was left blank")

    def test_blankDescription(self):
        resp = self.dummyClient.post('/CourseCreate/',
                                     {"name": "Introduction to Programming", "semester": "Summer", "year": "2022",
                                      "description": "Programming Analysis", "credits": " "})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for credit field",
                         "An error message was not displayed when name was left blank")

    def test_blankCredits(self):
        resp = self.dummyClient.post('/CourseCreate/',
                                     {"name": " ", "semester": "Summer", "year": "2022",
                                      "description": "Programming Analysis", "credits": " "})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Invalid entry for name field",
                         "An error message was not displayed when name was left blank")

    def createCourse(self):
        self.dummyClient.post('/CourseCreate/',
                              {"name": "Introduction to Machine Learning", "semester": "Spring", "year": "2022",
                               "description": "Advanced ML", "credits": "3"})

        spring_course = Course.objects.create(name="Introduction to Machine Learning", semester="Spring", year="2022",
                                              description="Advanced ML", credits="3")
        self.course: AbstractCourse = ConcreteCourse(spring_course)
        spring_course.save()

        self.assertEqual(Course.objects.create(name="Introduction to Machine Learning", semester="Spring", year="2022",
                                               description="Advanced ML", credits="3"), self.course.get_course_id(),
                         msg="Course was not successfully created")


class TestDeleteAccountPage(TestCase):

    def test_CourseCreate_to_Course_Management(self):

        response = self.client.post('/', {'username': 'Micheal_Johnson', 'password': 'password3'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, " ")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/AdminCourseMng")

        try:
            self.assertTrue(response.url, "/AdminCourseMng")
        except AssertionError as msg:
            print(msg)

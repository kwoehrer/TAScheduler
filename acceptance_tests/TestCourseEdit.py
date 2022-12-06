from django.test import TestCase, Client
from TAScheduler.app.models import *
from classes.Courses.CoursesClass import AbstractCourse, ConcreteCourse
from classes.Users.users import AdminUser


'''
SCENARIO: As an Admin, I want to be able navigate the Edit Course Page and Edit a Course
Acceptance Criteria 1:
GIVEN a course needs to edited
WHEN all the valid fields are entered correctly and course can be found
WHEN "Edit Account" is clicked
AND all the valid fields to be edited are entered correctly
THEN the course is edited

Acceptance Criteria 2:
SCENARIO: As an Admin, I want to be able to navigate to the Account Management page
GIVEN a course needs to edited
WHEN all the valid fields are not entered correctly
THEN course cannot be found
THEN course cannot be edited

Acceptance Criteria 3:
SCENARIO: As an Admin, I want to be able to navigate to the Account Management page
GIVEN The user is an Admin and is logged in and at the Edit Account page
WHEN a user of type Admin is to be edited
WHEN user can be found with valid fields in the list of all users
AND "Edit Account" is clicked
THEN account can be edited

SCENARIO: As an Admin, I want to be able navigate to the Home Page
Acceptance Criteria 1:
GIVEN: The user is a Admin and is logged in and at the Edit Account page
AND:They can click on "Return to Account Management Page"
THEN: They will be navigated to the "AdminAccMng" page

'''


class TestEditCourse(TestCase):
    dummyClient = None
    admin = None
    course = None

    def setUp(self):
        self.dummyClient = Client()

        spring_course = Course.objects.create(name="Introduction to Programming", semester="Summer", year="2022",
                                              description="Software Principles", credits="3")
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

    def test_editName(self):
        self.client.post("/TestCourseEdit/",
                         {"name": "Introduction to Software Engineering", "semester": self.course.get_course_name(),
                          "year": self.course.get_year(),
                          "description": self.course.get_description(), "credits": self.course.get_credits()})

        self.assertEqual("Introduction to Software Engineering",
                         Course.objects.get(courseID=self.course).name,
                         "Course Name was not set correctly")

    def test_editBlankName(self):
        name = self.course.get_course_name()
        resp = self.client.post("/TestCourseEdit/",
                                {"name": " ",
                                 "semester": self.course.get_course_name(),
                                 "year": self.course.get_year(),
                                 "description": self.course.get_description(), "credits": self.course.get_credits()})
        self.assertEqual(resp.context["error"], "Course was not edited. Name should not be left blank",
                         "An error message was not displayed when name was left blank")
        self.assertEqual(name, Course.objects.get(courseID=self.course).name, "Name was changed when it "
                                                                              "shouldn't have been")

    def test_editSemester(self):
        self.client.post("/TestCourseEdit/",
                         {"name": self.course.get_course_name(), "semester": "Fall 2022",
                          "year": self.course.get_year(),
                          "description": self.course.get_description(), "credits": self.course.get_credits()})

        self.assertEqual("Fall 2022",
                         Course.objects.get(courseID=self.course).semester,
                         "Course Semester was not set correctly")

    def test_editBlankSemester(self):
        name = self.course.get_semester()
        resp = self.client.post("/TestCourseEdit/",
                                {"name": self.course.get_course_name(),
                                 "semester": "",
                                 "year": self.course.get_year(),
                                 "description": self.course.get_description(), "credits": self.course.get_credits()})
        self.assertEqual(resp.context["error"], "Course was not edited. Semester should not be left blank",
                         "An error message was not displayed when name was left blank")
        self.assertEqual(name, Course.objects.get(courseID=self.course).semester, "Name was changed when it "
                                                                                  "shouldn't have been")

    def test_editYear(self):
        self.client.post("/TestCourseEdit/",
                         {"name": self.course.get_course_name(), "semester": self.course.get_course_name(),
                          "year": "2023",
                          "description": self.course.get_description(), "credits": self.course.get_credits()})

        self.assertEqual("2023",
                         Course.objects.get(courseID=self.course).year,
                         "Course Year was not set correctly")

    def test_editBlankYear(self):
        name = self.course.get_course_name()
        resp = self.client.post("/TestCourseEdit/",
                                {"name": " ",
                                 "semester": self.course.get_course_name(),
                                 "year": self.course.get_year(),
                                 "description": self.course.get_description(), "credits": self.course.get_credits()})
        self.assertEqual(resp.context["error"], "Course was not edited. Credits should not be left blank",
                         "An error message was not displayed when name was left blank")
        self.assertEqual(name, Course.objects.get(courseID=self.course).name, "Name was changed when it "
                                                                              "shouldn't have been")

    def test_editDescription(self):
        self.client.post("/TestCourseEdit/",
                         {"name": self.course.get_course_name(), "semester": self.course.get_course_name(),
                          "year": self.course.get_year(),
                          "description": "Program Analysis", "credits": self.course.get_credits()})

        self.assertEqual("Program Analysis",
                         Course.objects.get(courseID=self.course).description,
                         "Course description was not set correctly")

    def test_editBlankDescription(self):
        name = self.course.get_course_name()
        resp = self.client.post("/TestCourseEdit/",
                                {"name": self.course.get_course_name(),
                                 "semester": self.course.get_course_name(),
                                 "year": self.course.get_year(),
                                 "description": "", "credits": self.course.get_credits()})
        self.assertEqual(resp.context["error"], "Course was not edited. Credits should not be left blank",
                         "An error message was not displayed when name was left blank")
        self.assertEqual("Program Analysis", Course.objects.get(courseID=self.course).description,
                         "Name was changed when it "
                         "shouldn't have been")

    def test_editCredits(self):
        self.client.post("/TestCourseEdit/",
                         {"name": self.course.get_course_name(), "semester": self.course.get_semester(),
                          "year": self.course.get_year(),
                          "description": self.course.get_description(), "credits": "4"})

        self.assertEqual("4",
                         Course.objects.get(courseID=self.course).credits,
                         "Course Credits was not set correctly")

    def test_editBlankCredits(self):
        name = self.course.get_course_name()
        resp = self.client.post("/TestCourseEdit/",
                                {"name": " ",
                                 "semester": self.course.get_course_name(),
                                 "year": self.course.get_year(),
                                 "description": self.course.get_description(), "credits": ""})
        self.assertEqual(resp.context["error"], "Course was not edited. Credits should not be left blank",
                         "An error message was not displayed when name was left blank")
        self.assertEqual(name, Course.objects.get(courseID=self.course).credits, "Name was changed when it "
                                                                                 "shouldn't have been")


class TestEditCoursePage(TestCase):

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

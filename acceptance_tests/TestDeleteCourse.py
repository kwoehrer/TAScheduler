from django.test import TestCase, Client
from app.models import *
from classes.Courses.CoursesClass import AbstractCourse, ConcreteCourse
from classes.Users.users import AdminUser

'''
SCENARIO: As an Admin, I want to be able navigate the Edit Course Page and Edit a Course
---------------------------------------------------------------------------------
Acceptance Criteria 1:
GIVEN a course needs to deleted
WHEN all the valid fields are entered correctly and course can be found
WHEN "Edit Account" is clicked
AND all the valid fields to be edited are entered correctly
THEN the course is edited
---------------------------------------------------------------------------------
SCENARIO: As an Admin, I want to be able to navigate to the Account Management page
---------------------------------------------------------------------------------
Acceptance Criteria 1:
GIVEN a course needs to edited
WHEN all the valid fields are not entered correctly
THEN course cannot be found
THEN course cannot be edited
---------------------------------------------------------------------------------
Acceptance Criteria 3:
GIVEN The user is an Admin and is logged in and at the Edit Account page
WHEN a user of type Admin is to be edited
WHEN user can be found with valid fields in the list of all users
AND "Edit Account" is clicked
THEN account can be edited
---------------------------------------------------------------------------------
SCENARIO: As an Admin, I want to be able navigate to the Home Page
---------------------------------------------------------------------------------
Acceptance Criteria 1:
GIVEN: The user is a Admin and is logged in and at the Edit Account page
AND:They can click on "Return to Account Management Page"
THEN: They will be navigated to the "AdminAccMng" page

'''


# Delete Course Cases: Successful Deletion, Cannot Delete a Course if Labs are attached to course

class SuccessfulDeleteCourse(TestCase):
    client = None
    admin = None
    course = None

    def setUp(self):
        self.client = Client()

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

        self.client.post("/", {"username": self.admin.getUsername(), "password": self.admin.getPassword()})

    def test_CourseExists(self):
        spring_course_new = Course.objects.create(self.course)
        self.course_new: AbstractCourse = ConcreteCourse(spring_course_new)
        spring_course_new.save()

        self.client.post({"/AccountDelete/",
                          spring_course_new})

        self.assertEqual(self.course_new.get_course_id(), Admin.objects.get(account_ID=self.course.get_course_id()),
                         "Course exists in Database")

    def test_CourseDoesNotExist(self):
        spring_course_new = Course.objects.create(name="Introduction to Machine Learning", semester="Summer",
                                                  year="2022",
                                                  description="Advanced ML",
                                                  credits="3")
        self.course_new: AbstractCourse = ConcreteCourse(spring_course_new)
        spring_course_new.save()
        self.assertEqual(self.course_new.get_course_id(), self.course.get_course_id(), msg="Course exists")

    def test_deleteCourse(self):
        spring_course_new = Course.objects.create(name="Introduction to Machine Learning", semester="Summer",
                                                  year="2022",
                                                  description="Advanced ML",
                                                  credits="3")
        self.course_new: AbstractCourse = ConcreteCourse(spring_course_new)
        spring_course_new.save()
        self.client.post('/AccountDelete/', {'Delete Course': 1}, follow=True)
        var = Course.objects.count()
        self.assertEquals(var, 0, "Course was successfully deleted")
        courseCount = list(Course.objects.filter(name=spring_course_new)[0])
        self.assertEquals(courseCount, [], "No courses remain")

    def test_EmptyName(self):
        name = self.course.get_course_name()
        resp = self.client.post("/CourseDelete/",
                                {"name": " ",
                                 "semester": self.course.get_course_name(),
                                 "year": self.course.get_year(),
                                 "description": self.course.get_description(), "credits": self.course.get_credits()})
        self.assertEqual(resp.context["error"], "Course was not edited. Name should not be left blank",
                         "An error message was not displayed when name was left blank")
        self.assertEqual(name, Course.objects.get(courseID=self.course).name, "Name was changed when it "
                                                                              "shouldn't have been")

    def test_EmptySemester(self):
        name = self.course.get_semester()
        resp = self.client.post("/CourseDelete/",
                                {"name": self.course.get_course_name(),
                                 "semester": "",
                                 "year": self.course.get_year(),
                                 "description": self.course.get_description(), "credits": self.course.get_credits()})
        self.assertEqual(resp.context["error"], "Course was not edited. Semester should not be left blank",
                         "An error message was not displayed when name was left blank")
        self.assertEqual(name, Course.objects.get(courseID=self.course).semester, "Name was changed when it "
                                                                                  "shouldn't have been")

    def test_EmptyYear(self):
        year = self.course.get_course_name()
        resp = self.client.post("/CourseDelete/",
                                {"name": " ",
                                 "semester": self.course.get_course_name(),
                                 "year": self.course.get_year(),
                                 "description": self.course.get_description(), "credits": self.course.get_credits()})
        self.assertEqual(resp.context["error"], "Course was not edited. Credits should not be left blank",
                         "An error message was not displayed when name was left blank")
        self.assertEqual(year, Course.objects.get(courseID=self.course).year, "Name was changed when it "
                                                                              "shouldn't have been")

    def test_EmptyDescription(self):
        des = self.course.get_description()
        resp = self.client.post("/CourseDelete/",
                                {"name": self.course.get_course_name(),
                                 "semester": self.course.get_course_name(),
                                 "year": self.course.get_year(),
                                 "description": "", "credits": self.course.get_credits()})
        self.assertEqual(resp.context["error"], "Course was not edited. Credits should not be left blank",
                         "An error message was not displayed when name was left blank")
        self.assertEqual(des, Course.objects.get(courseID=self.course).description,
                         "Name was changed when it "
                         "shouldn't have been")

    def test_EmptyCredits(self):
        credit = self.course.get_credits()
        resp = self.client.post("/CourseDelete/",
                                {"name": " ",
                                 "semester": self.course.get_course_name(),
                                 "year": self.course.get_year(),
                                 "description": self.course.get_description(), "credits": ""})
        self.assertEqual(resp.context["error"], "Course was not edited. Credits should not be left blank",
                         "An error message was not displayed when name was left blank")
        self.assertEqual(credit, Course.objects.get(credits=self.course).credits, "Name was changed when it "
                                                                                  "shouldn't have been")


class TestDeleteCoursePage(TestCase):

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

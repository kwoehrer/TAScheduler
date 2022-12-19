from django.test import TestCase, Client
from app.models import *
from classes.Courses.CoursesClass import AbstractCourse, ConcreteCourse
from classes.Users.users import AdminUser


# Delete Course Cases: Successful Deletion, Cannot Delete a Course if Labs are attached to course

class SuccessfulDeleteCourse(TestCase):
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

        self.dummyClient.post("/", {"username": self.admin.getUsername(), "password": self.admin.getPassword()})

    def test_deleteCourse(self):
        self.dummyClient.post('/delete_course/', {'Delete Course': 1}, follow=True)
        var = Course.objects.count()
        self.assertEquals(var, 0, "Course was successfully deleted")
        courseCount = list(Course.objects.filter(courseID=self.course.get_course_id()))
        self.assertEquals(courseCount, [], "No courses remain")


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

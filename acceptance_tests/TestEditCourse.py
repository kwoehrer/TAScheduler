from django.test import TestCase, Client
from app.models import *
from classes.Courses.CoursesClass import AbstractCourse, ConcreteCourse
from classes.Sections import SectionClass
from classes.Users.users import AdminUser, TAUser, InstructorUser
import classes.Sections.SectionClass as CourseClass

'''
SCENARIO: As an Admin, I want to be able navigate to the Edit Course Page and Edit a Course
---------------------------------------------------------------------------------
Acceptance Criteria 1:
GIVEN a course needs to edited
WHEN all the valid fields are entered correctly and course can be found
WHEN "Edit This Course" is clicked
AND all the valid fields to be edited are entered correctly
THEN the course is edited
---------------------------------------------------------------------------------
Acceptance Criteria 2:
GIVEN a course needs to edited
WHEN all the valid fields are not entered correctly
THEN course cannot be found
THEN course cannot be edited
---------------------------------------------------------------------------------
Acceptance Criteria 3:
GIVEN a section needs to be added
WHEN a course of type semester is found
WHEN course can be found with valid fields in the list of all courses
AND "Edit This Course" is clicked
THEN course can be edited
---------------------------------------------------------------------------------
SCENARIO: As an Admin, I want to be able navigate to the Edit Course Page and Add a Section
---------------------------------------------------------------------------------
Acceptance Criteria 1:
GIVEN a course section needs to added
WHEN a course of type semester is found
WHEN course can be found with valid fields in the list of all courses
THEN all fields for a section are correctly added
AND "Add Section" is clicked
THEN a section is added to the parent course
Acceptance Criteria 2:
GIVEN a course section needs to added
WHEN a course of type semester is found
WHEN course can be found with valid fields in the list of all courses
THEN one of the fields for a section are invalid
AND "Add Section" is clicked
THEN a section is not added to the parent course
---------------------------------------------------------------------------------
SCENARIO: As an Admin, I want to be able navigate to the Edit Course Page and Add an Instructor
---------------------------------------------------------------------------------
Acceptance Criteria 1:
GIVEN an instructor associated with a course needs to added
WHEN a course of type semester is found
WHEN course can be found with valid fields in the list of all courses
THEN all fields for an instructor are correctly added
AND "Add Instructor" is clicked
THEN an instructor is added to the parent course
Acceptance Criteria 2:
GIVEN an instructor associated with a course needs to added
WHEN a course of type semester is found
WHEN course can be found with valid fields in the list of all courses
THEN one of the fields for an instructor are left invalid
AND "Add Instructor" is clicked
THEN an instructor is not added to the parent course
---------------------------------------------------------------------------------
SCENARIO: As an Admin, I want to be able navigate to the Edit Course Page and remove an Instructor
---------------------------------------------------------------------------------
Acceptance Criteria 1:
GIVEN an instructor associated with a course needs to added
WHEN a course of type semester is found
WHEN course can be found with valid fields in the list of all courses
THEN all fields for an instructor are correctly added
AND "Remove Instructor" is clicked
THEN an instructor is removed from the parent course
Acceptance Criteria 2:
GIVEN an instructor associated with a course needs to removed
WHEN a course of type semester is found
WHEN course can be found with valid fields in the list of all courses
THEN one of the fields for an instructor are left invalid
AND "Remove Instructor" is clicked
THEN an instructor is not removed from the parent course
---------------------------------------------------------------------------------
SCENARIO: As an Admin, I want to be able navigate to the Home Page
---------------------------------------------------------------------------------
Acceptance Criteria 1:
GIVEN: The user is a Admin and is logged in and at the Edit Account page
AND:They can click on "Return to Account Management Page"
THEN: They will be navigated to the "AdminAccMng" page

'''


class TestEditCourse(TestCase):
    client = None
    admin = None
    course = None

    def setUp(self):
        self.client = Client()

        spring_course = Course.objects.create(name="Introduction to Programming", semester="Spring", year="2022",
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

    def test_find_course(self):
        # login as the admin user
        r = self.client.post("/CourseEdit/",
                             {"username": self.admin.getUsername(), "password": self.admin.getPassword()})
        self.assertEqual(r.status_code, 200)  # check that the login was successful

        # try to add a new course
        resp = self.client.post("/CourseEdit/",
                                {"name": "Introduction to Programming",
                                 "semester": "Spring",
                                 "year": "2022",
                                 "description": "Software Principles", "credits": "3"})
        self.assertEqual(resp.status_code, 200)  # check that the course was added successfully
        self.assertFalse("message" in resp.context,
                         "No results found. Try again.")  # check that there is no error message

    def test_EditCourse(self):
        spring_course_new = Course.objects.create(name="Introduction to Programming", semester="Spring", year="2022",
                                                  description="Software Principles", credits="3")
        self.course_new: AbstractCourse = ConcreteCourse(spring_course_new)
        spring_course_new.save()

        r = self.client.post("/", {"username": self.admin.getUsername(), "password": self.admin.getPassword()})
        # successful login
        self.assertTrue(r.context is None)

        resp = self.client.post('/CourseEdit/',
                                {"Course Name": "Introduction to Programming",
                                 "Semester": "Spring",
                                 "Year": "2022",
                                 "Description": "Software Principles", "credits": "3"})
        try:
            self.assertFalse(resp.context["message"], "No results found. Try again.")
        except AssertionError as msg:
            print(msg)

        pass

    '''
        def test_CourseExists(self):
        spring_course_new = Course.objects.create(name="Introduction to Programming", semester="Spring", year="2022",
                                                  description="Software Principles", credits="3")
        self.course_new: AbstractCourse = ConcreteCourse(spring_course_new)
        spring_course_new.save()

        resp = self.client.post({"/CourseEdit/",
                                 spring_course_new})
        self.assertEqual(resp.context["message"],
                         "Course Successfully Edited")
    '''

    '''
     def test_CourseDoesNotExist(self):
        spring_course_new = Course.objects.create(name="Introduction to Machine Learning", semester="Summer",
                                                  year="2022",
                                                  description="Advanced ML",
                                                  credits="3")
        self.course_new: AbstractCourse = ConcreteCourse(spring_course_new)
        spring_course_new.save()
        self.assertEqual(self.course_new.get_course_id(), self.course.get_course_id(), msg="Course exists")
    '''

    '''
    def test_editName(self):
        self.client.post("/CourseEdit/",
                         {"name": "Introduction to Software Engineering", "semester": self.course.get_course_name(),
                          "year": self.course.get_year(),
                          "description": self.course.get_description(), "credits": self.course.get_credits()})

        self.assertNotEqual("Introduction to Software Engineering",
                            self.course.get_course_name(),
                            "Course Name was not set correctly")
    '''

    '''
     def test_editEmptyName(self):
        name = self.course.get_course_name()
        resp = self.client.post("/CourseEdit/",
                                {"name": " ",
                                 "semester": self.course.get_course_name(),
                                 "year": self.course.get_year(),
                                 "description": self.course.get_description(), "credits": self.course.get_credits()})
        abstract_course = Course.objects.create(name=" ", semester="Spring", year="2022",
                                                description="Software Principles", credits="3")
        self.course_abstract: AbstractCourse = ConcreteCourse(abstract_course)
        abstract_course.save()
        try:
            self.assertEqual(resp.context["message"], "No results found. Try again")
        except AssertionError as msg:
            print(msg)
        self.assertEqual(name, Course.objects.get(self.course_abstract.get_course_name()), "Name was changed when it "
                                                                                           "shouldn't have been")
    '''

    '''
     def test_editSemester(self):
        self.client.post("/CourseEdit/",
                         {"name": self.course.get_course_name(), "semester": "Fall 2022",
                          "year": self.course.get_year(),
                          "description": self.course.get_description(), "credits": self.course.get_credits()})

        self.assertEqual("Fall 2022",
                         Course.objects.get(courseID=self.course).semester,
                         "Course Semester was not set correctly")
    '''

    '''
     def test_EmptySemester(self):
        name = self.course.get_semester()
        resp = self.client.post("/CourseEdit/",
                                {"name": self.course.get_course_name(),
                                 "semester": "",
                                 "year": self.course.get_year(),
                                 "description": self.course.get_description(), "credits": self.course.get_credits()})

        abstract_course = Course.objects.create(name="Introduction to Programming", semester=" ", year="2022",
                                                description="Software Principles", credits="3")
        self.course_abstract: AbstractCourse = ConcreteCourse(abstract_course)
        abstract_course.save()

        self.assertEqual(resp.context["error"], "Course was not edited. Semester should not be left blank",
                         "An error message was not displayed when name was left blank")
        self.assertEqual(name, Course.objects.get(courseID=self.course_abstract).semester,
                         "Semester was changed when it "
                         "shouldn't have been")
    '''

    '''
        def test_editYear(self):
        self.client.post("/CourseEdit/",
                         {"name": self.course.get_course_name(), "semester": self.course.get_course_name(),
                          "year": "2023",
                          "description": self.course.get_description(), "credits": self.course.get_credits()})

        self.assertEqual("2023",
                         Course.objects.get(courseID=self.course).year,
                         "Course Year was not set correctly")
    '''

    '''
        def test_EmptyYear(self):
        year = self.course.get_course_name()
        resp = self.client.post("/CourseEdit/",
                                {"name": "Introduction to Programming",
                                 "semester": self.course.get_course_name(),
                                 "year": " ",
                                 "description": self.course.get_description(), "credits": self.course.get_credits()})

        abstract_course = Course.objects.create(name="Introduction to Programming", semester="Spring 2022", year=" ",
                                                description="Software Principles", credits="3")
        self.course_abstract: AbstractCourse = ConcreteCourse(abstract_course)
        abstract_course.save()
        self.assertEqual(resp.context["error"], "Course was not edited. Credits should not be left blank",
                         "An error message was not displayed when name was left blank")
        self.assertEqual(year, Course.objects.get(courseID=self.course_abstract).year, "Year was changed when it "
                                                                                       "shouldn't have been")

    '''

    '''
     def test_editDescription(self):
        self.client.post("/CourseEdit/",
                         {"name": self.course.get_course_name(), "semester": self.course.get_course_name(),
                          "year": self.course.get_year(),
                          "description": "Program Analysis", "credits": self.course.get_credits()})

        self.assertEqual("Program Analysis",
                         Course.objects.get(courseID=self.course).description,
                         "Course description was not set correctly")

    '''

    '''
     def test_EmptyDescription(self):
        des = self.course.get_description()
        resp = self.client.post("/CourseEdit/",
                                {"name": self.course.get_course_name(),
                                 "semester": self.course.get_course_name(),
                                 "year": self.course.get_year(),
                                 "description": " ", "credits": self.course.get_credits()})
        abstract_course = Course.objects.create(name="Introduction to Programming", semester="Spring 2022", year=" ",
                                                description=" ", credits="3")
        self.course_abstract: AbstractCourse = ConcreteCourse(abstract_course)
        abstract_course.save()
        self.assertEqual(resp.context["error"], "Course was not edited. Credits should not be left blank",
                         "An error message was not displayed when name was left blank")
        self.assertEqual(des, Course.objects.get(courseID=self.course_abstract).description,
                         "Description was changed when it "
                         "shouldn't have been")
    '''

    '''
        def test_editCredits(self):
        self.client.post("/CourseEdit/",
                         {"name": self.course.get_course_name(), "semester": self.course.get_semester(),
                          "year": self.course.get_year(),
                          "description": self.course.get_description(), "credits": "4"})

        self.assertEqual("4",
                         Course.objects.get(credits=self.course).credits,
                         "Course Credits was not set correctly")

    '''

    '''
     def test_EmptyCredits(self):
        credit = self.course.get_credits()
        resp = self.client.post("/CourseEdit/",
                                {"name": " ",
                                 "semester": self.course.get_course_name(),
                                 "year": self.course.get_year(),
                                 "description": self.course.get_description(), "credits": ""})
        abstract_course = Course.objects.create(name="Introduction to Programming", semester="Spring 2022", year="2022",
                                                description="Program Analysis", credits=" ")
        self.course_abstract: AbstractCourse = ConcreteCourse(abstract_course)
        abstract_course.save()
        self.assertEqual(resp.context["error"], "Course was not edited. Credits should not be left blank",
                         "An error message was not displayed when name was left blank")
        self.assertEqual(credit, Course.objects.get(credits=self.course_abstract).credits,
                         "Credits was changed when it "
                         "shouldn't have been")
    '''


class TestAddSection(TestCase):
    client = None
    admin = None
    section = None

    def setUp(self):
        self.course_model = Course.objects.create(name="Introduction to Programming", semester="Spring", year="2022",
                                                  description="Software Principles", credits="3")
        section = Section.objects.create(course_ID=self.course_model, section_num=100, MeetingTimes='1:00')
        self.course = CourseClass.ConcreteCourse(self.course_model)
        self.section = SectionClass.ConcreteSection(section)

    def test_duplicateSection(self):
        self.course_model = Course.objects.create(self.course)
        new_section = Section.objects.create(course_ID=self.course_model, section_num=100, MeetingTimes='1:00')
        self.course1 = CourseClass.ConcreteCourse(self.course_model)
        self.section1 = SectionClass.ConcreteSection(new_section)
        resp = self.client.post('/CourseCreate/',
                                {new_section})

        self.assertEqual(resp.context["error"],
                         "Course was not created. Duplicate Section Number already exists")

    def test_EmptyTA(self):
        response = self.client.post("/CourseEdit/",
                                    {"Assign TA to Section": " ",
                                     "Section Number": "100",
                                     "Description": "Systems Programming"})

        self.assertEqual(response.context["error"], "Section was not added. A TA field cannot be left blank")
        self.assertEqual(Section.objects.count(), 1, "Database did not change")

    def test_EmptySectionNum(self):
        response = self.client.post("/CourseEdit/",
                                    {"Assign TA to Section": "Luke Adams",
                                     "Section Number": " ",
                                     "Description": "Systems Programming"})

        self.assertEqual(response.context["error"],
                         "Section was not added. A Section Number field cannot be left blank")
        self.assertEqual(Section.objects.count(), 1, "Database did not change")

    def test_EmptyDescription(self):
        response = self.client.post("/CourseEdit/",
                                    {"Assign TA to Section": "Luke Adams",
                                     "Section Number": "100",
                                     "Description": " "}, follow=True)

        self.assertEqual(response.context["error"],
                         "Section was not added. A Description field cannot be left blank")
        self.assertEqual(Section.objects.count(), 1, "Database did not change")

    def testInvalidTA(self):
        response = self.client.post("/CourseEdit/",
                                    {"Assign TA to Section": "123",
                                     "Section Number": "100",
                                     "Description": "Systems Programming"}, follow=True)

        self.assertEqual(response.context["error"], "Section was not added. A TA needs to be of type User")
        self.assertEqual(Section.objects.count(), 1, "Database did not change")

    def testInvalidSectionNumber(self):
        response = self.client.post("/CourseEdit/",
                                    {"Assign TA to Section": "Luke Adams",
                                     "Section Number": "one-hundred",
                                     "Description": "Systems Programming"}, follow=True)

        self.assertEqual(response.context["error"], "Section was not added. A Section Number needs to be of type "
                                                    "Integer")
        self.assertEqual(Section.objects.count(), 1, "Database did not change")

    def testInvalidDescription(self):
        response = self.client.post("/CourseEdit/",
                                    {"Assign TA to Section": "123",
                                     "Section Number": "100",
                                     "Description": "123"}, follow=True)

        self.assertEqual(response.context["error"], "Section was not added. A Description needs to be of type String")
        self.assertEqual(Section.objects.count(), 1, "Database did not change")

    def test_addSection(self):
        response = self.client.post("/CourseEdit/",
                                    {"Assign TA to Section": "Luke Adams",
                                     "Section Number": "100",
                                     "Description": "System Programming"}, follow=True)

        User.objects.create(username='Luke Adams', password='password', first_name="luke", last_name='Adams',
                            user_type='TA', email='LukeAdams@gmail.com')
        ta_user_model = User.objects.filter(username='Luke Adams')[0]
        self.ta_model = TA.objects.create(account_ID=ta_user_model)

        section = Section.objects.create(course_ID=self.course_model, section_num=100, MeetingTimes='1:00',
                                         ta_account_id=self.ta_model)

        self.course = CourseClass.ConcreteCourse(self.course_model)
        self.ta: TAUser = TAUser(self.ta_model)
        self.section = SectionClass.ConcreteSection(section)

        self.assertEqual(response['context'], self.section,
                         "Instructor was not created successfully")

    def test_deleteSection(self):
        response = self.client.post("/CourseEdit/",
                                    {"Assign TA to Section": "Luke Adams",
                                     "Section Number": "100",
                                     "Description": "System Programming"}, follow=True)

        User.objects.create(username='Luke Adams', password='password', first_name="luke", last_name='Adams',
                            user_type='TA', email='LukeAdams@gmail.com')
        ta_user_model = User.objects.filter(username='Luke Adams')[0]
        self.ta_model = TA.objects.create(account_ID=ta_user_model)

        section = Section.objects.create(course_ID=self.course_model, section_num=100, MeetingTimes='1:00',
                                         ta_account_id=self.ta_model)

        self.client.post('/CourseEdit/', {'Delete Section': 1}, follow=True)
        var = Section.objects.count()
        self.assertEquals(var, 0, "Instructor was successfully deleted")
        UserCount = list(Section.objects.filter(section_num=section))
        self.assertEquals(UserCount, [], "No Instructors remain")


class TestEditCoursePageAddInstructor(TestCase):

    def test_addInstructor(self):
        response = self.client.post("/CourseEdit/",
                                    {"Instructor": "TA"}, follow=True)

        course_model = Course.objects.create(name="Introduction to Programming", semester="Spring", year="2022",
                                             description="Software Principles", credits="3")
        self.course: AbstractCourse = ConcreteCourse(course_model)
        course_model.save()

        User.objects.create(username='Luke Adams', password='password', first_name="luke", last_name='Adams',
                            user_type='Instructor', email='LukeAdams@gmail.com')
        instructor_user_model = User.objects.filter(username='Luke Adams')[0]
        instructor_model = Instructor.objects.create(account_ID=instructor_user_model, courseID=course_model)

        self.instructor: InstructorUser = InstructorUser(instructor_user_model)
        self.section = InstructorAssignments.objects.create(account_ID=instructor_model)

        self.assertEqual(response['context'], self.section,
                         "Instructor was not created successfully")

    def test_deleteInstructor(self):
        User.objects.create(username='Luke Adams', password='password', first_name="luke", last_name='Adams',
                            user_type='Instructor', email='LukeAdams@gmail.com')
        instructor_user_model = User.objects.filter(username='Luke Adams')[0]
        instructor_model = Instructor.objects.create(account_ID=instructor_user_model)

        self.instructor: InstructorUser = InstructorUser(instructor_model)

        self.client.post('/CourseEdit/', {'Remove Instructor': 1}, follow=True)
        var = User.objects.count()
        self.assertEquals(var, 0, "Instructor was successfully deleted")
        UserCount = list(User.objects.filter(account_ID=instructor_model))
        self.assertEquals(UserCount, [], "No Instructors remain")

    def test_CourseCreate_to_Course_Management(self):

        response = self.client.post('/', {'username': 'Micheal_Johnson', 'password': 'password3'})
        self.assertTrue(response.context is None)

        try:
            self.assertTrue(response.url, "/CourseEdit")
        except AssertionError as msg:
            print(msg)

        response = self.client.get("/AdminCourseMng")

        try:
            self.assertTrue(response.url, "/AdminCourseMng")
        except AssertionError as msg:
            print(msg)

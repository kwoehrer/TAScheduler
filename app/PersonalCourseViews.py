from django.shortcuts import render
from django.views import View

from app.models import User, Instructor, TA
from classes.Courses.CoursesClass import ConcreteCourse
from classes.Users.users import InstructorUser, TAUser


class MyCourses(View):
    def get(self, request):
        t = None
        curr_user_model = User.objects.get(account_ID=request.session['current_user_account_id'])
        user_type = curr_user_model.user_type
        logged_user = None
        if user_type == "TA":
            curr_user_model = TA.objects.get(account_ID=curr_user_model)
            logged_user = TAUser(curr_user_model)

            concrete_course_list = list()
            course_list = logged_user.getCourses()
            section_dict = dict()

            for course in course_list:
                course = ConcreteCourse(course)
                for section in course.get_sections():
                    if section.getTA().getID() == logged_user.getID():
                        if course.get_course_id() not in section_dict:
                            section_dict[course.get_course_id()] = list()
                        section_dict[course.get_course_id()].append(section.getSectionNumber())
                concrete_course_list.append(course)

            print(section_dict)
            return render(request, "MyCourseAssignments.html",
                          {"my_courses": concrete_course_list, "my_sections": section_dict })
        elif user_type == "Instructor":
            curr_user_model = Instructor.objects.get(account_ID=curr_user_model)
            logged_user = InstructorUser(curr_user_model)
            course_list = logged_user.getCourses()
            concrete_course_list = list()

            for course in course_list:
                concrete_course_list.append(course)
            return render(request, "MyCourseAssignments.html", {"my_courses": concrete_course_list})

        if logged_user == None:
            return render(request, "login.html",
                          {'message': "Please login to access  your personal course assignments."})

    def post(self, request):
        pass

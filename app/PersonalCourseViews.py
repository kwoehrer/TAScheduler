from django.shortcuts import render
from django.views import View

from app.models import User, Admin, Instructor, TA, Course
from classes.Courses.CoursesClass import ConcreteCourse
from classes.Users.users import InstructorUser, TAUser, AdminUser


class MyCourses(View):
    def get(self, request):
        t = None
        curr_user_model = User.objects.get(account_ID=request.session['current_user_account_id'])
        user_type = curr_user_model.user_type
        logged_user = None
        if user_type == "TA":
            curr_user_model = TA.objects.get(account_ID=curr_user_model)
            logged_user = TAUser(curr_user_model)
        elif user_type == "Instructor":
            curr_user_model = Instructor.objects.get(account_ID=curr_user_model)
            logged_user = InstructorUser(curr_user_model)
        elif user_type == "Admin":
            curr_user_model = Admin.objects.get(account_ID=curr_user_model)
            logged_user = AdminUser(curr_user_model)

        if logged_user == None:
            return render(request, "login.html", {'message': "Please login to access  your personal course assignments."})

        #Create course array
        course_list = logged_user.getCourses()

        return render(request, "MyCourseAssignments.html", {"my_courses": course_list})

    def post(self, request):
        pass
from django.shortcuts import render
from django.views import View

from app.models import User, Course
from classes.Courses.CoursesClass import ConcreteCourse


# https://codinggear.blog/how-to-create-superuser-in-django/

class CourseSummary(View):
    def get(self, request):
        course_model = Course.objects.get(course_ID=request.GET.get('current_course'))
        course_wrapper = ConcreteCourse(course_model)

        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA":
            t = "./CourseSummaryStates/TACourseSummary.html"
        elif user_type == "Instructor":
            t = "./CourseSummaryStates/InstructorCourseSummary.html"
        elif user_type == "Admin":
            t = "./CourseSummaryStates/AdminCourseSummary.html"

        if t == None:
            return render(request, "login.html", {'message': "An unknown error has occurred."})
        else:
            return render(request, "CourseSummary.html", {'State': t, 'course': course_wrapper})

    def post(self, request):
        course_model = Course.objects.get(course_ID=request.POST.get('current_course'))
        course_wrapper = ConcreteCourse(course_model)

        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA":
            t = "./CourseSummaryStates/TACourseSummary.html"'course_wrapper'
        elif user_type == "Instructor":
            t = "./CourseSummaryStates/InstructorCourseSummary.html"
        elif user_type == "Admin":
            t = "./CourseSummaryStates/AdminCourseSummary.html",

        if t == None:
            return render(request, "login.html", {'message': "An unknown error has occurred."})
        else:
            return render(request, "CourseSummary.html", {'State': t, 'course': course_wrapper})

from django.shortcuts import render
from django.views import View

from app.models import User, Admin, Instructor, TA, Course, Section
from classes.Courses.CoursesClass import ConcreteCourse, AbstractCourse
from classes.Factories.AccountFactory import AbstractAccountFactory, ConcreteAccountFactory
from classes.Factories.CourseFactory import ConcreteCourseFactory, AbstractCourseFactory
from classes.Sections.SectionClass import ConcreteSection
from classes.Users.users import TAUser, AbstractUser, AdminUser, InstructorUser

# https://codinggear.blog/how-to-create-superuser-in-django/

class CourseSummary(View):
    def get(self, request):
        course_model = Course.objects.get(account_ID=request.GET.get(['current_course']))
        course_wrapper = Course.ConcreteCourse(course_model)

        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA":
            t = render(request, "./CourseSummaryStates/TACourseSummary.html",
                       {'course_wrapper': course_wrapper})
        elif user_type == "Instructor":
            t = render(request, "./CourseSummaryStates/InstructorCourseSummary.html",
                       {'course_wrapper': course_wrapper})
        elif user_type == "Admin":
            t = render(request, "./CourseSummaryStates/AdminCourseSummary.html",
                       {'course_wrapper': course_wrapper})

        if t == None:
            return render(request, "login.html", {'message': "An unknown error has occurred."})
        else:
            return render(request, "CourseSummary.html", {'State': t})

    def post(self, request):
        course_model = Course.objects.get(account_ID=request.POST.get(['current_course']))
        course_wrapper = Course.ConcreteCourse(course_model)

        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA":
            t = render(request, "./CourseSummaryStates/TACourseSummary.html",
                       {'course_wrapper': course_wrapper})
        elif user_type == "Instructor":
            t = render(request, "./CourseSummaryStates/InstructorCourseSummary.html",
                       {'course_wrapper': course_wrapper})
        elif user_type == "Admin":
            t = render(request, "./CourseSummaryStates/AdminCourseSummary.html",
                       {'course_wrapper': course_wrapper})

        if t == None:
            return render(request, "login.html", {'message': "An unknown error has occurred."})
        else:
            return render(request, "CourseSummary.html", {'State': t})
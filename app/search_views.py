from django.shortcuts import render
from django.views import View

from app.models import User, Admin, Instructor, TA, Course, Section
from classes.Courses.CoursesClass import ConcreteCourse, AbstractCourse
from classes.Factories.AccountFactory import AbstractAccountFactory, ConcreteAccountFactory
from classes.Factories.CourseFactory import ConcreteCourseFactory, AbstractCourseFactory
from classes.Sections.SectionClass import ConcreteSection
from classes.Users.users import TAUser, AbstractUser, AdminUser, InstructorUser


class SearchHome(View):
    def get(self, request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA" or  user_type == "Instructor" or user_type == "Admin":
            t = "poopy"

        if t == None:
            return render(request, "login.html", {'message': "Please login to access search page."})
        else:
            return render(request, "searchStates/SearchHome.html", {})

    def post(self, request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA" or  user_type == "Instructor" or user_type == "Admin":
            t = "hehexd"

        if t == None:
            return render(request, "login.html", {'message': "Please login to access search page."})
        else:
            return render(request, "searchStates/SearchHome.html", {})

class SearchUser(View):
    def get(self, request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA" or  user_type == "Instructor" or user_type == "Admin":
            t = "hehexd"

        if t == None:
            return render(request, "login.html", {'message': "Please login to access search page."})
        else:
            return render(request, "searchStates/UserSearch.html", {})
    def post(self, request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA" or  user_type == "Instructor" or user_type == "Admin":
            t = "hehexd"

        if t == None:
            return render(request, "login.html", {'message': "Please login to access search page."})
        else:
            return render(request, "searchStates/UserSearch.html", {})

class SearchCourse(View):
    pass
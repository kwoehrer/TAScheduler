from django.shortcuts import render
from django.template.loader import get_template
from django.views import View
from django.core import serializers

from app.models import Instructor, Admin, User
from classes.Users.users import TAUser, AbstractUser, AdminUser, InstructorUser


class Login(View):
    def get(self,request):
        return render(request, "login.html",{})

    def post(self, request):
        #Verify user information in login
        query = User.objects.filter(username=request.POST['username'], password=request.POST['password'])

        logged_user: AbstractUser = None
        if len(query) > 0:
            logged_user_model: User = query[0]
            user_type = logged_user_model.user_type
            #determine type of user instance
            if user_type == "TA":
                logged_user = TAUser(logged_user_model)
            elif user_type == "Instructor":
                logged_user = InstructorUser(logged_user_model)
            elif user_type == "Admin":
                logged_user = AdminUser(logged_user_model)
        else:
            return render(request,"login.html",{'message': "Invalid Username or Password."})

        if logged_user == None:
            return render(request,"login.html",{'message': "An unknown error has occurred."})

        #Store as logged user
        request.session["current_user_account_id"] = query[0].account_ID

        context = {}

        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA":
            t = './homeStates/TAHome.html'
        elif user_type == "Instructor":
            t = './homeStates/InstructorHome.html'
        elif user_type == "Admin":
            t = './homeStates/AdminHome.html'

        if t == None:
            return render(request,"login.html",{'message': "An unknown error has occurred."})
        else:
            return render(request,"home.html",{'HomeState':t})

class Home(View):
    def get(self,request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA":
            t = './homeStates/TAHome.html'
        elif user_type == "Instructor":
            t = './homeStates/InstructorHome.html'
        elif user_type == "Admin":
            t = './homeStates/AdminHome.html'

        if t == None:
            return render(request, "login.html", {'message': "An unknown error has occurred."})
        else:
            return render(request,"home.html",{'HomeState':t})

class LogOut(View):
    def get(self, request):
        request.session["current_user_account_id"] = None
        return render(request, 'login.html', {'message': "You have been logged out of the system."})

    def post(self, request):
        # Verify user information in login
        request.session["current_user_account_id"] = None
        return render(request, 'login.html', {'message': "You have been logged out of the system."})

class AccountManagement(View):
    def get(self, request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "Admin":
            t = './AccountManagementStates/AdminAccMng.html'

        if t == None:
            return render(request, "login.html", {'message': "An unknown error has occurred."})
        else:
            return render(request,"AccountManagement.html",{'State':t})


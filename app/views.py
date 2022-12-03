from django.shortcuts import render
from django.template.loader import get_template
from django.views import View
from django.core import serializers

from app.models import Instructor, Admin, User
from classes.Factories.AccountFactory import AbstractAccountFactory, ConcreteAccountFactory
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

    def post(self,request):
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

class CreateAccount(View):
    def get(self, request):
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type != "Admin":
            return render(request, "login.html", {'message': "An unknown error has occurred."})
        else:
            return render(request, "AccountCreate.html", {})

    def post(self, request):
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type != "Admin":
            return render(request, "login.html", {'message': "An unknown error has occurred."})
        else:
            return render(request, "AccountCreate.html", {})

class AccountFactoryCreate(View):
    def get(self, request):
        pass

    def post(self, request):
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type != "Admin":
            return render(request, "login.html", {'message': "An unknown error has occurred."})

        acc_fact: AbstractAccountFactory = ConcreteAccountFactory()
        # Can make this assumption due to narrowing conversion above.
        curr_user: AbstractUser = AdminUser(User.objects.get(account_ID=request.session['current_user_account_id']))
        new_user_attributes = dict()

        #Initialize values based on form input.
        new_user_attributes['email'] = request.POST.get('email')
        new_user_attributes['username'] = request.POST.get('username')
        new_user_attributes['password'] = request.POST.get('password')
        new_user_attributes['first_name'] = request.POST.get('first_name')
        new_user_attributes['last_name'] = request.POST.get('last_name')
        new_user_attributes['phone_number'] = request.POST.get('phone_number')
        new_user_attributes['home_address'] = request.POST.get('home_address')
        new_user_attributes['user_type'] = request.POST.get('user_type')
        try:
            acc_fact.create_account(curr_user, new_user_attributes)
        except Exception as e:
            return render(request, "AccountCreate.html", {"message": e.__str__})

        return render(request, "AccountCreate.html", {"message": "Success"})

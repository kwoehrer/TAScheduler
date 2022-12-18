from django.shortcuts import render
from django.views import View

from app.models import User, Admin, Instructor, TA
from classes.Users.users import InstructorUser, TAUser, AdminUser


class Profile(View):
    def get(self, request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type

        user_id = request.GET.get('user')
        user_model = User.objects.get(account_ID=user_id)

        user_wrapped = None

        if user_type == "TA":
            t = "ProfileStates/TAViewState.html"
        elif user_type == "Instructor":
            t = "ProfileStates/InstrViewState.html"
        elif user_type == "Admin":
            t = "ProfileStates/AdminViewState.html"

        if user_model.user_type == "TA":
            user_model = TA.objects.get(account_ID=user_model)
            user_wrapped = TAUser(user_model)
        elif user_model.user_type == "Instructor":
            user_model = Instructor.objects.get(account_ID=user_model)
            user_wrapped = InstructorUser(user_model)
        elif user_model.user_type == "Admin":
            user_model = Admin.objects.get(account_ID=user_model)
            user_wrapped = AdminUser(user_model)

        if t == None:
            return render(request, "login.html", {'message': "Please login to access search page."})
        else:
            return render(request, "UserProfile.html", {'State': t, 'user': user_wrapped})

    def post(self, request):
        pass


class PersonalProfile(View):
    def get(self, request):
        t = None
        t = user = User.objects.get(account_ID=request.session['current_user_account_id'])
        if user.user_type == "TA":
            user_model = TA.objects.get(account_ID=user)
            user_wrapped = TAUser(user_model)
        elif user.user_type == "Instructor":
            user_model = Instructor.objects.get(account_ID=user)
            user_wrapped = InstructorUser(user_model)
        elif user.user_type == "Admin":
            user_model = Admin.objects.get(account_ID=user)
            user_wrapped = AdminUser(user_model)

        if t == None:
            return render(request, "login.html", {'message': "Please login to access search page."})
        else:
            return render(request, "MyUserProfile.html", { 'user': user_wrapped})

    def post(self, request):
        pass

class EditMyProfile(View):
    def get(self, request):
        t = None
        t = user = User.objects.get(account_ID=request.session['current_user_account_id'])
        if user.user_type == "TA":
            user_model = TA.objects.get(account_ID=user)
            user_wrapped = TAUser(user_model)
        elif user.user_type == "Instructor":
            user_model = Instructor.objects.get(account_ID=user)
            user_wrapped = InstructorUser(user_model)
        elif user.user_type == "Admin":
            user_model = Admin.objects.get(account_ID=user)
            user_wrapped = AdminUser(user_model)

        if t == None:
            return render(request, "login.html", {'message': "Please login to access search page."})
        else:
            return render(request, "EditMyUserProfile.html", {'user': user_wrapped})

    def post(self, request):




        t = None
        t = user = User.objects.get(account_ID=request.session['current_user_account_id'])
        if user.user_type == "TA":
            user_model = TA.objects.get(account_ID=user)
            user_wrapped = TAUser(user_model)
        elif user.user_type == "Instructor":
            user_model = Instructor.objects.get(account_ID=user)
            user_wrapped = InstructorUser(user_model)
        elif user.user_type == "Admin":
            user_model = Admin.objects.get(account_ID=user)
            user_wrapped = AdminUser(user_model)

        if t == None:
            return render(request, "login.html", {'message': "Please login to access search page."})
        else:
            return render(request, "EditMyUserProfile.html", {'user': user_wrapped})

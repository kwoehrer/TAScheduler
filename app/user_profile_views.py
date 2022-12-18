from django.shortcuts import render
from django.views import View

from app.models import User, Admin, Instructor, TA, Course
from classes.Courses.CoursesClass import ConcreteCourse
from classes.Users.users import InstructorUser, TAUser, AdminUser

class Profile(View):
    def get(self, request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type

        user_id = request.GET.get('user')
        user_model = User.objects.get(account_ID=user_id)

        user_wrapped = None
        if user_type == "TA":
            user_model = TA.objects.get(account_ID=user_model)
            user_wrapped = TAUser(user_model)
            t = "ProfileStates/TAViewState.html"
        elif user_type == "Instructor":
            user_model = Instructor.objects.get(account_ID=user_model)
            user_wrapped = InstructorUser(user_model)
            t = "ProfileStates/InstrViewState.html"
        elif user_type == "Admin":
            user_model = Admin.objects.get(account_ID=user_model)
            user_wrapped = AdminUser(user_model)
            t = "ProfileStates/AdminViewState.html"


        if t == None:
            return render(request, "login.html", {'message': "Please login to access search page."})
        else:
            return render(request, "UserProfile.html", {'State': t, 'user':user_wrapped})

    def post(self, request):
       pass

from django.shortcuts import render
from django.template.loader import get_template
from django.views import View

from app.models import Instructor, Admin, User
from classes.Users.users import TAUser, AbstractUser



class Login(View):
    def get(self,request):
        return render(request, "login.html",{})

    def post(self, request):
        #Verify user information in login
        query = User.objects.filter(username=request.POST['username'], password=request.POST['password'])

        logged_user: AbstractUser = None
        print(query)
        if len(query) > 0:
            logged_user_model: User = query[0]
            user_type = logged_user_model.user_type
            #determine type of user instance
            if user_type == "TA":
                logged_user = TAUser(logged_user_model)
            elif user_type == "Instructor":
                logged_user = Instructor(logged_user_model)
            elif user_type == "Admin":
                logged_user = Admin(logged_user_model)
        else:
            return render(request,"login.html",{'message': "Invalid Username or Password."})

        if logged_user == None:
            return render(request,"login.html",{'message': "An unknown error has occurred."})

        #Store as logged user
        request.session["current_user"] = logged_user

        context = {}

        t = None
        user_type = request.session['current_user'].get
        if user_type == "TA":
            t = get_template('./homeStates/TAHome.html')
        elif user_type == "Instructor":
            t = get_template('./homeStates/InstructorHome.html')
        elif user_type == "Admin":
            t = get_template('./homeStates/AdminHome.html')

        if(t == None):
            return render(request,"login.html",{'message': "An unknown error has occurred."})
        else:
            HomeState = t.render(context=context)
            return render(request,"home.html",{'HomeState':HomeState})
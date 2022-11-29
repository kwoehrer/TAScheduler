from django.shortcuts import render
from django.template.loader import get_template
from django.views import View
from models import User

class Login(View):
    def get(self,request):
        return render(request, "login.html",{})

    def post(self, request):
        #Create user in session - create session based on user id
        #Verify user information in login
        query = User.objects.get(username=request.POST['username'], password=request.POST['password'])
        loggedUser: AbstractUser = None
        if len(query) > 0:
            logged_user_model: User = query[0]
            user_type = logged_user_model.user_type
            #determine type of user instance
            if user_type == "TA":
                loggedUser = TA_User(logged_user_model) #TODO with vedants implementation
            elif user_type == "Instructor":
                loggedUser = Instructor(logged_user_model) #TODO wth vedants implementation
            elif user_type == "Admin":
                loggedUser = Admin(logged_user_model)  #TODO with vedants implementation
        else:
            #TODO Invalid username/password

        if loggedUser == None:
            #TODO Return back to login with unknown error

        #Store as logged user
        request.session["current_user"] = loggedUser

        context = {}

        t = None
        user_type = request.session['current_user'].get #TODO Match with vedants implementation
        if user_type == "TA":
            loggedUser = TA_User(logged_user_model)  # TODO with vedants implementation
            t = get_template('./homeStates/TAHome.html')
        elif user_type == "Instructor":
            loggedUser = Instructor(logged_user_model)  # TODO wth vedants implementation
            t = get_template('./homeStates/InstructorHome.html')
        elif user_type == "Admin":
            loggedUser = Admin(logged_user_model)  # TODO with vedants implementation
            t = get_template('./homeStates/AdminHome.html')

        if(t == None):
            #TODO Return to home page with an error
        else:
            HomeState = t.render(context=context)
            return render(request,"home.html",{'HomeState':HomeState})
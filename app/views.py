from django.shortcuts import render
from django.views import View

from app.models import User, Admin, Instructor, TA
from classes.Factories.AccountFactory import AbstractAccountFactory, ConcreteAccountFactory
from classes.Users.users import TAUser, AbstractUser, AdminUser, InstructorUser


class Login(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        # Verify user information in login
        query = User.objects.filter(username=request.POST['username'], password=request.POST['password'])

        logged_user: AbstractUser = None
        if len(query) > 0:
            logged_user_model: User = query[0]
            user_type = logged_user_model.user_type
            # determine type of user instance
            if user_type == "TA":
                logged_user = TAUser(logged_user_model)
            elif user_type == "Instructor":
                logged_user = InstructorUser(logged_user_model)
            elif user_type == "Admin":
                logged_user = AdminUser(logged_user_model)
        else:
            return render(request, "login.html", {'message': "Invalid Username or Password."})

        if logged_user == None:
            return render(request, "login.html", {'message': "An unknown error has occurred."})

        # Store as logged user
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
            return render(request, "login.html", {'message': "An unknown error has occurred."})
        else:
            return render(request, "home.html", {'HomeState': t})


class Home(View):
    def get(self, request):
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
            return render(request, "home.html", {'HomeState': t})

    def post(self, request):
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
            return render(request, "home.html", {'HomeState': t})


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
            return render(request, "AccountManagement.html", {'State': t})


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
            return render(request, "login.html",
                          {'message': "User has been logged out due to accessing admin content on non-admin account."})

        acc_fact: AbstractAccountFactory = ConcreteAccountFactory()
        # Can make this assumption due to narrowing conversion above.
        curr_user: AbstractUser = AdminUser(User.objects.get(account_ID=request.session['current_user_account_id']))
        new_user_attributes = dict()

        # Initialize values based on form input.
        new_user_attributes['email'] = str(request.POST.get('email'))
        new_user_attributes['username'] = str(request.POST.get('username'))
        new_user_attributes['password'] = str(request.POST.get('password'))
        new_user_attributes['first_name'] = str(request.POST.get('first_name'))
        new_user_attributes['last_name'] = str(request.POST.get('last_name'))
        new_user_attributes['phone_number'] = str(request.POST.get('phone'))
        new_user_attributes['home_address'] = str(request.POST.get('home_address'))
        new_user_attributes['user_type'] = str(request.POST.get('user_type'))

        try:
            acc_fact.create_account(curr_user, new_user_attributes)
        except Exception as e:
            return render(request, "AccountCreate.html", {"bad_message": e.__str__})

        return render(request, "AccountCreate.html", {"good_message": "Account Successfully Created."})


class DeleteAccount(View):
    def get(self, request):
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type != "Admin":
            return render(request, "login.html",
                          {'message': "User has been logged out due to accessing admin content on non-admin account."})
        else:
            return render(request, "AccountDelete.html", {"page_state_title": "Query For An Account To Delete"})

    def post(self, request):
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type != "Admin":
            return render(request, "login.html",
                          {'message': "User has been logged out due to accessing admin content on non-admin account."})
        # FILTER USERS HERE
        email_query = request.POST.get('email')
        username_query = request.POST.get('username')
        name_query = request.POST.get('name')
        user_type_query = request.POST.get('user_type')

        total_query = None
        if email_query is not None and email_query != '':
            total_query = User.objects.filter(email=email_query)

        if username_query is not None and username_query != '':
            if total_query is None:
                total_query = User.objects.filter(username=username_query)
            else:
                total_query = total_query.filter(username=username_query)
        if name_query is not None and name_query != '':
            first_name = name_query.split(' ')[0]
            last_name = name_query.split(' ')[1]
            if total_query is None:
                total_query = User.objects.filter(first_name=first_name)
                total_query = total_query.filter(last_name=last_name)
            else:
                total_query = total_query.filter(first_name=first_name)
                total_query = total_query.filter(last_name=last_name)
        if user_type_query is not None and user_type_query != '':
            if total_query is None:
                total_query = User.objects.filter(user_type=user_type_query)
            else:
                total_query = total_query.filter(user_type=user_type_query)

        # GET A LIST OF ALL USERS
        acc_model_list = list(total_query)
        acc_list = []

        for account_model in acc_model_list:
            # Evaluate user type and create the correct subtype. Then append to list.
            if user_type_query == "Admin":
                curr_obj = Admin.objects.get(account_ID=account_model.account_ID)
                acc_list.append(AdminUser(curr_obj))
            elif user_type_query == "Instructor":
                curr_obj = Instructor.objects.get(account_ID=account_model.account_ID)
                acc_list.append(InstructorUser(curr_obj))
            elif user_type_query == "TA":
                curr_obj = TA.objects.get(account_ID=account_model.account_ID)
                acc_list.append(TAUser(curr_obj))

        return render(request, "AccountDelete.html",
                      {"page_state_title": "Select An Account To Delete", 'query_accounts': acc_list})


class AccountFactoryDelete(View):
    def get(self, request):
        pass

    def post(self, request):
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type != "Admin":
            return render(request, "login.html",
                          {'message': "User has been logged out due to accessing admin content on non-admin account."})

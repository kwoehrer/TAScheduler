from django.shortcuts import render
from django.views import View

from app.admin import AdminUser
from app.models import User, Admin, Instructor, TA
from classes.Users.users import InstructorUser, TAUser


class SearchHome(View):
    def get(self, request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA" or user_type == "Instructor" or user_type == "Admin":
            t = "poopy"

        if t == None:
            return render(request, "login.html", {'message': "Please login to access search page."})
        else:
            return render(request, "searchStates/SearchHome.html", {})

    def post(self, request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA" or user_type == "Instructor" or user_type == "Admin":
            t = "hehexd"

        if t == None:
            return render(request, "login.html", {'message': "Please login to access search page."})
        else:
            return render(request, "searchStates/SearchHome.html", {})


class SearchUser(View):
    def get(self, request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA" or user_type == "Instructor" or user_type == "Admin":
            t = "hehexd"

        if t == None:
            return render(request, "login.html", {'message': "Please login to access search page."})
        else:
            return render(request, "searchStates/UserSearch.html", {'page_state_title': "User Search Form"})

    def post(self, request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA" or user_type == "Instructor" or user_type == "Admin":
            t = "hehexd"

        if t == None:
            return render(request, "login.html", {'message': "Please login to access search page."})
        else:
            return render(request, "searchStates/UserSearch.html", {'page_state_title': "User Search Form"})


class SearchUserResults(View):
    def get(self, request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA" or user_type == "Instructor" or user_type == "Admin":
            t = "hehexd"

        if t == None:
            return render(request, "login.html", {'message': "Please login to access search page."})
        else:
            return render(request, "searchStates/UserSearch.html",
                          {'page_state_title': "User Search Results", 'bad_message': "No Results Found.. Try Again"})

    def post(self, request):
        # Validate user login
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA" or user_type == "Instructor" or user_type == "Admin":
            t = "hehexd"
        if t == None:
            return render(request, "login.html", {'message': "Please login to access search page."})

        # Query database for users and put into array
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

        return render(request, "searchStates/UserSearchResults.html", {'page_state_title': "User Search Results",'query_users':acc_list})


class SearchCourse(View):
    def get(self, request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA" or user_type == "Instructor" or user_type == "Admin":
            t = "hehexd"

        if t == None:
            return render(request, "login.html", {'message': "Please login to access search page."})
        else:
            return render(request, "searchStates/UserSearchResults.html", {'page_state_title': "User Search Results"})

    def post(self, request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA" or user_type == "Instructor" or user_type == "Admin":
            t = "hehexd"

        if t == None:
            return render(request, "login.html", {'message': "Please login to access search page."})
        else:
            return render(request, "searchStates/UserSearchResults.html", {'page_state_title': "User Search Results"})

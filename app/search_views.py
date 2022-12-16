from django.shortcuts import render
from django.views import View

from app.models import User


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

class SearchUserResult(View):
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



class SearchCourse(View):
    pass

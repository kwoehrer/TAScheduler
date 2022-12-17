from django.shortcuts import render
from django.views import View

from app.models import User, Admin, Instructor, TA, Course
from classes.Courses.CoursesClass import ConcreteCourse
from classes.Users.users import InstructorUser, TAUser, AdminUser


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
            return render(request, "searchStates/UserSearch.html", {'page_state_title': "User Search"})

    def post(self, request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA" or user_type == "Instructor" or user_type == "Admin":
            t = "hehexd"

        if t == None:
            return render(request, "login.html", {'message': "Please login to access search page."})
        else:
            return render(request, "searchStates/UserSearch.html", {'page_state_title': "User Search"})


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
        first_name_query = request.POST.get('first_name')
        last_name_query = request.POST.get('last_name')
        user_type_query = request.POST.get('user_type')

        total_query = None
        if email_query is not None and email_query != '':
            total_query = User.objects.filter(email=email_query)

        if username_query is not None and username_query != '':
            if total_query is None:
                total_query = User.objects.filter(username=username_query)
            else:
                total_query = total_query.filter(username=username_query)
        if first_name_query is not None and first_name_query != '':
            if total_query is None:
                total_query = User.objects.filter(first_name=first_name_query)
            else:
                total_query = total_query.filter(first_name=first_name_query)
        if last_name_query is not None and last_name_query != '':
            if total_query is None:
                total_query = User.objects.filter(last_name=last_name_query)
            else:
                total_query = total_query.filter(last_name=last_name_query)
        if user_type_query is not None and user_type_query != '':
            if user_type_query == "All Users":
                if total_query is None:
                    total_query = User.objects.all()
            else:
                if total_query is None:
                    total_query = User.objects.filter(user_type=user_type_query)
                else:
                    total_query = total_query.filter(user_type=user_type_query)

        acc_model_list = list(total_query)
        acc_list = []
        for account_model in acc_model_list:
            # Evaluate user type and create the correct subtype. Then append to list.
            if account_model.user_type == "Admin":
                curr_obj = Admin.objects.get(account_ID=account_model.account_ID)
                acc_list.append(AdminUser(curr_obj))
            elif account_model.user_type == "Instructor":
                curr_obj = Instructor.objects.get(account_ID=account_model.account_ID)
                acc_list.append(InstructorUser(curr_obj))
            elif account_model.user_type == "TA":
                curr_obj = TA.objects.get(account_ID=account_model.account_ID)
                acc_list.append(TAUser(curr_obj))

        if len(acc_list) == 0:
            return render(request, "searchStates/UserSearch.html", {"bad_message": "No results found. Try again.",
                                                                    "page_state_title": "User Search"})
        return render(request, "searchStates/UserSearchResults.html",
                      {'page_state_title': "User Search Results", 'query_users': acc_list})


class SearchCourse(View):
    def get(self, request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA" or user_type == "Instructor" or user_type == "Admin":
            t = "hehexd"

        if t == None:
            return render(request, "login.html", {'message': "Please login to access search page."})
        else:
            return render(request, "searchStates/CourseSearch.html", {'page_state_title': "Course Search"})

    def post(self, request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA" or user_type == "Instructor" or user_type == "Admin":
            t = "hehexd"

        if t == None:
            return render(request, "login.html", {'message': "Please login to access search page."})
        else:
            return render(request, "searchStates/CourseSearch.html", {'page_state_title': "Course Search"})

class SearchCourseResults(View):
    def get(self, request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA" or user_type == "Instructor" or user_type == "Admin":
            t = "hehexd"

        if t == None:
            return render(request, "login.html", {'message': "Please login to access search page."})

        # FILTER COURSE HERE
        name_query = request.GET.get('name')
        semester_query = request.GET.get('semester')
        year_query = request.GET.get('year')

        total_query = None
        if name_query is not None and name_query != '':
            total_query = Course.objects.filter(name=name_query)

        if semester_query is not None and semester_query != '':
            if total_query is None:
                if semester_query == "All Semesters":
                    total_query = Course.objects.all()
                else:
                    total_query = Course.objects.filter(semester=semester_query)
            else:
                if semester_query != "All Semesters":
                    total_query = total_query.filter(semester=semester_query)
        if year_query is not None and year_query != '':
            if total_query is None:
                total_query = Course.objects.filter(year=year_query)
            else:
                total_query = total_query.filter(year=year_query)

        # GET A LIST OF ALL USERS
        course_model_list = list(total_query)
        course_list = []

        for crs_model in course_model_list:
            course_list.append(ConcreteCourse(crs_model))

        if len(course_list) == 0:
            return render(request, "searchStates/CourseSearch.html", {"bad_message": "No results found. Try again.",
                                                         "page_state_title": "Course Search"})

        return render(request, "searchStates/courseSearchResults.html",
                      {"page_state_title": "Course Search Results", 'query_courses': course_list})

    def post(self, request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA" or user_type == "Instructor" or user_type == "Admin":
            t = "hehexd"

        if t == None:
            return render(request, "login.html", {'message': "Please login to access search page."})
        else:
            return render(request, "searchStates/CourseSearchResults.html", {'page_state_title': "User Search Results"})


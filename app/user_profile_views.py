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
            return render(request, "MyUserProfile.html", {'user': user_wrapped})

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

        user_to_edit_wrapper = None

        if user.user_type == "Admin":
            user_to_edit_model = Admin.objects.get(account_ID=user)
            user_to_edit_wrapper = AdminUser(user_to_edit_model)
        elif user.user_type == "Instructor":
            user_to_edit_model = Instructor.objects.get(account_ID=user)
            user_to_edit_wrapper = InstructorUser(user_to_edit_model)
        elif user.user_type == "TA":
            user_to_edit_model = TA.objects.get(account_ID=user)
            user_to_edit_wrapper = TAUser(user_to_edit_model)

        try:
            if request.POST.get('user_type') != '':
                user_to_edit_wrapper.setUserType(request.POST.get('user_type'))
            if request.POST.get('last_name') != '':
                user_to_edit_wrapper.setLastName(request.POST.get('last_name'))
            if request.POST.get('first_name') != '':
                user_to_edit_wrapper.setFirstName(request.POST.get('first_name'))
            if request.POST.get('phone_number') != '':
                user_to_edit_wrapper.setPhoneNumber(request.POST.get('phone_number'))
            if request.POST.get('home_address') != '':
                user_to_edit_wrapper.setHomeAddress(request.POST.get('home_address'))
            if request.POST.get('password') != '':
                user_to_edit_wrapper.setPassword(request.POST.get('password'))
            if request.POST.get('email') != '':
                user_to_edit_wrapper.setEmail(request.POST.get('email'))
        except Exception as e:
            msg = "Could not edit account due to " + str(e.__str__())
            return render(request, "EditMyUserProfile.html", {"user": user_to_edit_wrapper, "bad_message": msg})

        updated_wrapper = None

        if user.user_type == "Admin":
            user_to_edit_model = Admin.objects.get(account_ID=user)
            updated_wrapper = AdminUser(user_to_edit_model)
        elif user.user_type == "Instructor":
            user_to_edit_model = Instructor.objects.get(account_ID=user)
            updated_wrapper = InstructorUser(user_to_edit_model)
        elif user.user_type == "TA":
            user_to_edit_model = TA.objects.get(account_ID=user)
            updated_wrapper = TAUser(user_to_edit_model)

        return render(request, "MyUserProfile.html", {"user": updated_wrapper,
                                                      "good_message": "Account Successfully Edited."})

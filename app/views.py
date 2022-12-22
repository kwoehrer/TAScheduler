from django.shortcuts import render
from django.views import View

from app.models import User, Admin, Instructor, TA, Course, Section
from classes.Courses.CoursesClass import ConcreteCourse, AbstractCourse
from classes.Factories.AccountFactory import AbstractAccountFactory, ConcreteAccountFactory
from classes.Factories.CourseFactory import ConcreteCourseFactory, AbstractCourseFactory
from classes.Sections.SectionClass import ConcreteSection
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
        admin_model = Admin.objects.get(account_ID=request.session['current_user_account_id'])
        curr_user: AbstractUser = AdminUser(admin_model)
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

        if len(acc_list) == 0:
            return render(request, "AccountDelete.html", {"bad_message": "No results found. Try again.",
                                                          "page_state_title": "Query For An Account To Delete"})

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

        acc_fact: AbstractAccountFactory = ConcreteAccountFactory()
        # Can make this assumption due to narrowing conversion above.
        admin_model = Admin.objects.get(account_ID=request.session['current_user_account_id'])
        curr_user: AbstractUser = AdminUser(admin_model)
        user_to_delete_id = request.POST.get('acc_id')
        user_to_delete_type = request.POST.get('acc_type')
        user_to_delete_wrapper: AbstractUser = None

        if user_to_delete_type == "Admin":
            user_to_delete_model = Admin.objects.get(account_ID__account_ID=user_to_delete_id)
            user_to_delete_wrapper = AdminUser(user_to_delete_model)
        elif user_to_delete_type == "Instructor":
            user_to_delete_model = Instructor.objects.get(account_ID__account_ID=user_to_delete_id)
            user_to_delete_wrapper = InstructorUser(user_to_delete_model)
        elif user_to_delete_type == "TA":
            user_to_delete_model = TA.objects.get(account_ID__account_ID=user_to_delete_id)
            user_to_delete_wrapper = TAUser(user_to_delete_model)
        try:
            acc_fact.delete_account(curr_user, user_to_delete_wrapper)
        except Exception as e:
            msg = "Could not delete account due to " + str(e.__str__())
            return render(request, "AccountDelete.html", {"bad_message": msg})

        return render(request, "AccountDelete.html", {"page_state_title": "Query For An Account To Delete",
                                                      "good_message": "Account Successfully Deleted."})


class EditAccount(View):
    def get(self, request):
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type != "Admin":
            return render(request, "login.html",
                          {'message': "User has been logged out due to accessing admin content on non-admin account."})
        else:
            return render(request, "AccountEdit.html", {"page_state_title": "Query For An Account To Edit"})

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
                try:
                    curr_obj = TA.objects.get(account_ID=account_model.account_ID)
                    acc_list.append(TAUser(curr_obj))
                except:
                    print("SQL TA object error")

        if len(acc_list) == 0:
            return render(request, "AccountEdit.html", {"bad_message": "No results found. Try again.",
                                                        "page_state_title": "Query For An Account To Edit"})

        return render(request, "AccountEdit.html",
                      {"page_state_title": "Select An Account To Edit", 'query_accounts': acc_list})


class AccountEditActive(View):

    def get(self):
        pass

    def post(self, request):
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type != "Admin":
            return render(request, "login.html",
                          {'message': "User has been logged out due to accessing admin content on non-admin account."})

        user_to_edit_id = request.POST.get('acc_id')
        user_to_edit_id = request.POST.get('acc_id')
        user_to_edit = User.objects.get(account_ID=user_to_edit_id)


        if user_to_edit.user_type == "Admin":
            user_to_edit_model = Admin.objects.get(account_ID__account_ID=user_to_edit_id)
            user_to_edit_wrapper = AdminUser(user_to_edit_model)
        elif user_to_edit.user_type == "Instructor":
            user_to_edit_model = Instructor.objects.get(account_ID__account_ID=user_to_edit_id)
            user_to_edit_wrapper = InstructorUser(user_to_edit_model)
        elif user_to_edit.user_type == "TA":
            user_to_edit_model = TA.objects.get(account_ID__account_ID=user_to_edit_id)
            user_to_edit_wrapper = TAUser(user_to_edit_model)

        try:
            user_to_edit_wrapper.setUserType(request.POST.get('user_type'))
            user_to_edit_wrapper.setLastName(request.POST.get('last_name'))
            user_to_edit_wrapper.setFirstName(request.POST.get('first_name'))
            # Have to check phone number before passing in because django changes none to empty strings. Thanks django
            if request.POST.get('phone_number') != '':
                user_to_edit_wrapper.setPhoneNumber(request.POST.get('phone_number'))

            user_to_edit_wrapper.setHomeAddress(request.POST.get('home_address'))

            # Have to check password before passing in because django changes none to empty strings. Thanks django
            if request.POST.get('password') != '':
                user_to_edit_wrapper.setPassword(request.POST.get('password'))

            user_to_edit_wrapper.setUsername(request.POST.get('username'))
            user_to_edit_wrapper.setEmail(request.POST.get('email'))
        except Exception as e:
            msg = "Could not edit account due to " + str(e.__str__())
            return render(request, "AccountEdit.html", {"bad_message": msg})

        return render(request, "AccountEdit.html", {"page_state_title": "Query For An Account To Edit",
                                                    "good_message": "Account Successfully Edited."})


class CourseManagement(View):
    def get(self, request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "Admin":
            t = './CourseManagementStates/AdminCourseMng.html'

        if t == None:
            return render(request, "login.html", {'message': "An unknown error has occurred."})
        else:
            return render(request, "CourseManagement.html", {'State': t})


class CreateCourse(View):
    def get(self, request):
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type != "Admin":
            return render(request, "login.html", {'message': "An unknown error has occurred."})
        else:
            return render(request, "CourseCreate.html", {})

    def post(self, request):
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type != "Admin":
            return render(request, "login.html", {'message': "An unknown error has occurred."})
        else:
            return render(request, "CourseCreate.html", {})


class CourseFactoryCreate(View):
    def get(self, request):
        pass

    def post(self, request):
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type != "Admin":
            return render(request, "login.html",
                          {'message': "User has been logged out due to accessing admin content on non-admin account."})

        course_fact: AbstractCourseFactory = ConcreteCourseFactory()
        # Can make this assumption due to narrowing conversion above.
        admin_model = Admin.objects.get(account_ID=request.session['current_user_account_id'])
        curr_user: AbstractUser = AdminUser(admin_model)
        new_course_attributes = dict()

        # Initialize values based on form input.
        new_course_attributes['name'] = str(request.POST.get('name'))
        new_course_attributes['semester'] = str(request.POST.get('semester'))
        new_course_attributes['year'] = int(request.POST.get('year'))
        new_course_attributes['description'] = str(request.POST.get('description'))
        new_course_attributes['credits'] = int(request.POST.get('credit'))

        try:
            course_fact.create_course(curr_user, new_course_attributes)
        except Exception as e:
            return render(request, "CourseCreate.html", {"bad_message": e.__str__})

        return render(request, "CourseCreate.html", {"good_message": "Course Successfully Created."})


class DeleteCourse(View):
    def get(self, request):
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type != "Admin":
            return render(request, "login.html",
                          {'message': "User has been logged out due to accessing admin content on non-admin account."})
        else:
            return render(request, "CourseDelete.html", {"page_state_title": "Query For A Course To Delete"})

    def post(self, request):
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type != "Admin":
            return render(request, "login.html",
                          {'message': "User has been logged out due to accessing admin content on non-admin account."})
        # FILTER COURSE HERE
        name_query = request.POST.get('name')
        semester_query = request.POST.get('semester')
        year_query = request.POST.get('year')
        credit_query = request.POST.get('credit')
        desc_query = request.POST.get('description')

        total_query = None
        if name_query is not None and name_query != '':
            total_query = Course.objects.filter(name=name_query)

        if semester_query is not None and semester_query != '':
            if total_query is None:
                total_query = Course.objects.filter(semester=semester_query)
            else:
                total_query = total_query.filter(semester=semester_query)
        if year_query is not None and year_query != '':
            if total_query is None:
                total_query = Course.objects.filter(year=year_query)
            else:
                total_query = total_query.filter(year=year_query)
        if credit_query is not None and credit_query != '':
            if total_query is None:
                total_query = Course.objects.filter(credits=credit_query)
            else:
                total_query = total_query.filter(credits=credit_query)
        if desc_query is not None and desc_query != '':
            if total_query is None:
                total_query = Course.objects.filter(description=credit_query)
            else:
                total_query = total_query.filter(description=credit_query)

        # GET A LIST OF ALL USERS
        course_model_list = list(total_query)
        course_list = []

        for crs_model in course_model_list:
            course_list.append(ConcreteCourse(crs_model))

        if len(course_list) == 0:
            return render(request, "CourseDelete.html", {"bad_message": "No results found. Try again.",
                                                         "page_state_title": "Query For A Course To Delete"})

        return render(request, "CourseDelete.html",
                      {"page_state_title": "Select A Course To Delete", 'query_courses': course_list})


class CourseFactoryDelete(View):
    def get(self, request):
        pass

    def post(self, request):
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type != "Admin":
            return render(request, "login.html",
                          {'message': "User has been logged out due to accessing admin content on non-admin account."})

        crs_fact: AbstractCourseFactory = ConcreteCourseFactory()
        # Can make this assumption due to narrowing conversion above.
        admin_model = Admin.objects.get(account_ID=request.session['current_user_account_id'])
        curr_user: AbstractUser = AdminUser(admin_model)
        crs_to_delete_id = request.POST.get('course_id')
        crs_model = Course.objects.get(course_ID=crs_to_delete_id)
        crs_wrapper: AbstractCourse = ConcreteCourse(crs_model)

        try:
            crs_fact.delete_course(curr_user, crs_wrapper)
        except Exception as e:
            msg = "Could not delete account due to " + str(e.__str__())
            return render(request, "CourseDelete.html", {"bad_message": msg})

        return render(request, "CourseDelete.html", {"page_state_title": "Query For A Course To Delete",
                                                     "good_message": "Course Successfully Deleted."})


class EditCourse(View):
    def get(self, request):
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type != "Admin":
            return render(request, "login.html",
                          {'message': "User has been logged out due to accessing admin content on non-admin account."})
        else:
            return render(request, "CourseEdit.html", {"page_state_title": "Query For A Course To Edit"})

    def post(self, request):
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type != "Admin":
            return render(request, "login.html",
                          {'message': "User has been logged out due to accessing admin content on non-admin account."})
        name_query = request.POST.get('name')
        semester_query = request.POST.get('semester')
        year_query = request.POST.get('year')
        credit_query = request.POST.get('credit')
        desc_query = request.POST.get('description')

        total_query = None
        if name_query is not None and name_query != '':
            total_query = Course.objects.filter(name=name_query)

        if semester_query is not None and semester_query != '':
            if total_query is None:
                total_query = Course.objects.filter(semester=semester_query)
            else:
                total_query = total_query.filter(semester=semester_query)
        if year_query is not None and year_query != '':
            if total_query is None:
                total_query = Course.objects.filter(year=year_query)
            else:
                total_query = total_query.filter(year=year_query)
        if credit_query is not None and credit_query != '':
            if total_query is None:
                total_query = Course.objects.filter(credits=credit_query)
            else:
                total_query = total_query.filter(credits=credit_query)
        if desc_query is not None and desc_query != '':
            if total_query is None:
                total_query = Course.objects.filter(description=credit_query)
            else:
                total_query = total_query.filter(description=credit_query)

        # GET A LIST OF ALL USERS
        course_model_list = list(total_query)
        course_list = []

        for crs_model in course_model_list:
            course_list.append(ConcreteCourse(crs_model))

        instructor_model_list = Instructor.objects.all()
        instructor_list = []

        for instr in instructor_model_list:
            instructor_list.append(InstructorUser(instr))

        ta_model_list = TA.objects.all()
        ta_list = []

        for ta in ta_model_list:
            ta_list.append(TAUser(ta))

        if len(course_list) == 0:
            return render(request, "CourseEdit.html", {"bad_message": "No results found. Try again.",
                                                       "page_state_title": "Query For A Course To Edit"})

        return render(request, "CourseEdit.html",
                      {"page_state_title": "Select A Course To Edit", 'total_ta_list': ta_list,
                       'total_instr_list': instructor_list,
                       'query_courses': course_list})


class CourseEditActive(View):

    def get(self):
        pass

    def post(self, request):
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type != "Admin":
            return render(request, "login.html",
                          {'message': "User has been logged out due to accessing admin content on non-admin account."})

        crs_to_edit_id = request.POST.get('course_id')
        crs_to_edit_model = Course.objects.get(course_ID=crs_to_edit_id)
        crs_to_edit_wrapper: AbstractCourse = ConcreteCourse(crs_to_edit_model)

        try:
            crs_to_edit_wrapper.set_course_name(request.POST.get('name'))
            crs_to_edit_wrapper.set_semester(request.POST.get('semester'))
            crs_to_edit_wrapper.set_year(int(request.POST.get('year')))
            crs_to_edit_wrapper.set_credits(int(request.POST.get('credits')))
            crs_to_edit_wrapper.set_description(request.POST.get('description'))
        except Exception as e:
            msg = "Could not edit account due to " + str(e.__str__())
            return render(request, "CourseEdit.html", {"bad_message": msg})

        return render(request, "CourseEdit.html", {"page_state_title": "Query For A Course To Edit",
                                                   "good_message": "Course Successfully Edited."})


class CourseAddSection(View):

    def get(self):
        pass

    def post(self, request):
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type != "Admin":
            return render(request, "login.html",
                          {'message': "User has been logged out due to accessing admin content on non-admin account."})

        crs_to_edit_id = request.POST.get('course_id')
        crs_to_edit_model = Course.objects.get(course_ID=crs_to_edit_id)
        crs_to_edit_wrapper: AbstractCourse = ConcreteCourse(crs_to_edit_model)

        ta_account_id = request.POST.get('sectionTA')
        section_num = request.POST.get('section_num')
        MeetingTimes = request.POST.get('meeting_times')

        try:
            crs_to_edit_wrapper.add_section(ta_account_id, section_num, MeetingTimes)
        except Exception as e:
            msg = "Could not add section due to " + str(e.__str__())
            return render(request, "CourseEdit.html", {"bad_message": msg})

        return render(request, "CourseEdit.html", {"page_state_title": "Query For A Course To Edit",
                                                   "good_message": "Section successfully added."})


class CourseDeleteSection(View):

    def get(self):
        pass

    def post(self, request):
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type != "Admin":
            return render(request, "login.html",
                          {
                              'message': "User has been logged out due to accessing admin content on non-admin account."})

        crs_to_edit_id = request.POST.get('course_id')
        crs_to_edit_model = Course.objects.get(course_ID=crs_to_edit_id)
        crs_to_edit_wrapper: AbstractCourse = ConcreteCourse(crs_to_edit_model)

        section_num = request.POST.get('section_num')

        # create section to pass into wrapper
        sec_to_del = Section.objects.get(course_ID=crs_to_edit_model, section_num=section_num)

        try:
            crs_to_edit_wrapper.remove_section(ConcreteSection(sec_to_del))
        except Exception as e:
            msg = "Could not delete section due to " + str(e.__str__())
            return render(request, "CourseEdit.html", {"bad_message": msg})

        return render(request, "CourseEdit.html", {"page_state_title": "Query For A Course To Edit",
                                                   "good_message": "Section Successfully Deleted."})


class CourseAddInstructor(View):

    def get(self):
        pass

    def post(self, request):
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type != "Admin":
            return render(request, "login.html",
                          {
                              'message': "User has been logged out due to accessing admin content on non-admin account."})

        crs_to_edit_id = request.POST.get('course_id')
        crs_to_edit_model = Course.objects.get(course_ID=crs_to_edit_id)
        crs_to_edit_wrapper: AbstractCourse = ConcreteCourse(crs_to_edit_model)

        selected_instr_id = request.POST.get('selected_instr')

        # create section to pass into wrapper
        instr_to_add = Instructor.objects.get(account_ID__account_ID=selected_instr_id)

        try:
            crs_to_edit_wrapper.add_instructor(InstructorUser(instr_to_add))
        except Exception as e:
            msg = "Could not assign instructor due to " + str(e.__str__())
            return render(request, "CourseEdit.html", {"bad_message": msg})

        return render(request, "CourseEdit.html", {"page_state_title": "Query For A Course Edit",
                                                   "good_message": "Instructor Successfully Assigned To Course."})


class CourseRemoveInstructor(View):
    def get(self):
        pass

    def post(self, request):
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type != "Admin":
            return render(request, "login.html",
                          {
                              'message': "User has been logged out due to accessing admin content on non-admin account."})

        crs_to_edit_id = request.POST.get('course_id')
        crs_to_edit_model = Course.objects.get(course_ID=crs_to_edit_id)
        crs_to_edit_wrapper: AbstractCourse = ConcreteCourse(crs_to_edit_model)

        selected_instr_id = request.POST.get('selected_instr')

        # create section to pass into wrapper
        instr_to_remove = Instructor.objects.get(account_ID__account_ID=selected_instr_id)

        try:
            crs_to_edit_wrapper.remove_instructor(InstructorUser(instr_to_remove))
        except Exception as e:
            msg = "Could not unassign instructor due to " + str(e.__str__())
            return render(request, "CourseEdit.html", {"bad_message": msg})

        return render(request, "CourseEdit.html", {"page_state_title": "Query For A Course To Edit",
                                                   "good_message": "Instructor Successfully Unassigned From Course."})

class SectionSummary(View):
    def get(self, request):
        courses = Course.objects.all()

        concrete_courses = [ConcreteCourse(course) for course in courses]

        return render(request, 'SectionSummary.html', {'courses': concrete_courses})

    def post(self, request):

        course_id = request.POST.get('course_id')

        try:
            course = Course.objects.get(course_ID=course_id)
        except Course.DoesNotExist:
            return render(request, 'SectionSummary.html')

        concrete_course = ConcreteCourse(course)

        sections = concrete_course.get_sections()

        sections_list = []

        for section in sections:
            sections_list.append(section)

        ta_model_list = TA.objects.all()
        ta_list = []

        for ta in ta_model_list:
            ta_list.append(TAUser(ta))

        return render(request, 'SectionSummary.html',
                      {'selected_course': concrete_course, 'sections': sections_list, 'ta_list': ta_list})



class SendNotification(View):

    def get(self, request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "Instructor":
            t = './homeStates/InstructorHome.html'
        elif user_type == "Admin":
            t = './homeStates/AdminHome.html'

        if t is None:
            return render(request, "login.html", {'message': "An unknown error has occurred."})
        else:
            return render(request, "SendNotifications.html", {'HomeState': t})

    def post(self, request):
        # If the user does not have a valid name, I.E. if they try to manually enter /home in the search bar,
        # they will fail the userAllowed test and be redirected back to the login page
        # If the user is allowed then home is rendered like normal

        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "Instructor":
            t = './homeStates/InstructorHome.html'
        elif user_type == "Admin":
            t = './homeStates/AdminHome.html'

        # if t is None:
        #   return render(request, "login.html", {'message': "An unknown error has occurred."})
        if t is not None:
            return render(request, "SendNotifications.html", {'HomeState': t})

        selected_user_email = User.objects.get(account_ID__email=request.POST.get('email')).user_type
        selected_user_course = Course.objects.get(course_ID__name=request.POST.get('name')).course_ID

        total_query = None
        total_course_query = None
        email_query = request.POST.get('email')
        # user_name = request.POST.get('acc_id')
        course_query = request.POST.get('name')
        if user_type == 'Admin':
            if selected_user_email == "Instructor":
                if email_query is not None and email_query != '':
                    total_query = Instructor.objects.filter(account_ID__user_type=selected_user_email)
        elif user_type == 'Instructor':
            if selected_user_email == "TA":
                if email_query is not None and email_query != '':
                    total_query = TA.objects.filter(account_ID__email=selected_user_email)

        if user_type == 'Admin':
            if selected_user_course is not None:
                total_course_query = None
                if course_query is not None and email_query != '':
                    total_course_query = Course.objects.filter(course_ID__name=course_query)
        elif user_type == 'Instructor':
            if selected_user_email == "TA":
                total_course_query = None
                if email_query is not None and email_query != '':
                    total_course_query = Course.objects.filter(course_ID__name=course_query)

        # GET A LIST OF ALL USERS EMAILS
        users_list = []
        if total_query == "Admin":
            users_list.append(Instructor.objects.all())
        elif total_query == "Instructor":
            users_list.append(TA.objects.all())

        # GET A LIST OF ALL USERS
        course_model_list = list(total_course_query)
        course_list = []
        instructor_course_list = []
        ta_course_list = []

        for crs_model in course_model_list:
            if total_course_query is not None:
                course_list.append(ConcreteCourse(crs_model))

        for course in course_list:
            if total_query == "Admin":
                instructor_course_list.append(course.get_instructors())
            elif total_query == "Instructors":
                ta_course_list.append(course.get_tas())

        instructor_model_list = Instructor.objects.all()
        instructor_list = []

        for instr in instructor_model_list:
            instructor_list.append(InstructorUser(instr))

        ta_model_list = TA.objects.all()
        ta_list = []

        for ta in ta_model_list:
            ta_list.append(TAUser(ta))

        # to_field = request.POST.getlist('to')
        # cc_field = request.POST.getlist('cc')
        # subject = request.POST['subject']
        # message = request.POST['message']

        try:
            if len(course_list) == 0 and len(users_list) == 0:
                return render(request, "SendNotifications.html",
                          {"Query for Course": course_list, "Select Users": users_list,
                           "Select All Users within a course": course_list})
        except Exception as e:
            msg = "Could not send email " + str(e.__str__())
            return render(request, "SendNotifications.html", {"bad_message": msg})


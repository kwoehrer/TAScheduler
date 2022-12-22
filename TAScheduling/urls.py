"""TAScheduling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.PersonalCourseViews import MyCourses
from app.search_views import SearchHome, SearchUser, SearchCourse, SearchUserResults, SearchCourseResults
from app.section_views import SingleSection
from app.user_profile_views import Profile, PersonalProfile, EditMyProfile
from app.coursesummaryviews import CourseSummary
from app.views import Login, Home, LogOut, AccountManagement, CreateAccount, AccountFactoryCreate, DeleteAccount, \
    AccountFactoryDelete, EditAccount, AccountEditActive, CourseManagement, CreateCourse, CourseFactoryCreate, \
    DeleteCourse, CourseFactoryDelete, EditCourse, CourseEditActive, CourseAddSection, CourseDeleteSection, \
    CourseAddInstructor, CourseRemoveInstructor, SectionSummary

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view()),
    path('home/', Home.as_view()),
    path('logout/', LogOut.as_view()),
    path('AccountManagement/', AccountManagement.as_view()),
    path('CreateAccount/', CreateAccount.as_view()),
    path('AccountFactoryCreate/', AccountFactoryCreate.as_view()),
    path('DeleteAccount/', DeleteAccount.as_view()),
    path('AccountFactoryDelete/', AccountFactoryDelete.as_view()),
    path('EditAccount/', EditAccount.as_view()),
    path('AccountEditActive/', AccountEditActive.as_view()),
    path('CourseManagement/', CourseManagement.as_view()),
    path('CreateCourse/', CreateCourse.as_view()),
    path('CourseFactoryCreate/', CourseFactoryCreate.as_view()),
    path('DeleteCourse/', DeleteCourse.as_view()),
    path('CourseFactoryDelete/', CourseFactoryDelete.as_view()),
    path('EditCourse/', EditCourse.as_view()),
    path('CourseEditActive/', CourseEditActive.as_view()),
    path('CourseAddSection/', CourseAddSection.as_view()),
    path('CourseDeleteSection/', CourseDeleteSection.as_view()),
    path('CourseAddInstructor/', CourseAddInstructor.as_view()),
    path('CourseRemoveInstructor/', CourseRemoveInstructor.as_view()),
    path('SectionSummary/', SectionSummary.as_view()),
    path('search/', SearchHome.as_view()),
    path('search/user/', SearchUser.as_view()),
    path('search/course/', SearchCourse.as_view()),
    path('search/user/results/', SearchUserResults.as_view()),
    path('search/course/results/', SearchCourseResults.as_view()),
    path('profile/', Profile.as_view(), name='profile'),
    path('MyProfile/', PersonalProfile.as_view()),
    path('editMyProfile/', EditMyProfile.as_view()),
    path('CourseSummary/', CourseSummary.as_view(), name="course"),
    path('SingleSectionSummary/', SingleSection.as_view(), name="section"),
    path('MyCourses/', MyCourses.as_view())

]

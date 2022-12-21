from django.contrib import admin

from app.models import User, Admin, TA, Instructor


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    pass

@admin.register(Admin)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(TA)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Instructor)
class CourseAdmin(admin.ModelAdmin):
    pass

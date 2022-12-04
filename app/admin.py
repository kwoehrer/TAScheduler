from django.contrib import admin

from app.models import User, Admin

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    pass

@admin.register(Admin)
class CourseAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin
from .models import Attendance
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

User = get_user_model()


# Register your models here.
admin.site.unregister(User)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp')
    list_filter = ('user', 'timestamp')
    search_fields = ('user', 'timestamp')
    ordering = ('-timestamp',)



@admin.register(User)
class CustomUserAdmin(DefaultUserAdmin):
    list_display = ('id', 'username', 'email', 'is_staff')  # Add 'id' to display
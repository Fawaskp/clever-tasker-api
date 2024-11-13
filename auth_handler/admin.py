from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

class MyUserAdmin(UserAdmin):
    model = MyUser
    list_display = ['email', 'name', 'is_active']
    search_fields = ['email', 'name']
    ordering = ['email']

    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

admin.site.register(MyUser, MyUserAdmin)
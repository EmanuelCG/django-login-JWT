from django.contrib import admin
from .models import User
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'last_login', 'is_verified']

admin.site.register(User, UserAdmin)
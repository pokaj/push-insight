from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'username', 'email', 'role', 'organization')

admin.site.register(User, UserAdmin)
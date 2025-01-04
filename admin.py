from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import TeamMember, Contact  # Removed Profile from imports

# Custom UserAdmin class to customize how the User model appears in the admin panel
class CustomUserAdmin(UserAdmin):
    # Add or modify fields you want to display in the user admin
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')  # Removed 'get_profile_mobile'
    search_fields = ('username', 'email')  # Fields to search by
    ordering = ('username',)  # Default ordering of user list

    # Removed custom method to display mobile from Profile

# Unregister the default User model registration
admin.site.unregister(User)

# Re-register User with the custom UserAdmin class
admin.site.register(User, CustomUserAdmin)

# Register your other models
admin.site.register(TeamMember)
admin.site.register(Contact)



from .models import Work  # Use the correct model name
admin.site.register(Work)

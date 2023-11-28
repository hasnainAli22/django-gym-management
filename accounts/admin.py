from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile, UserRole

# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email')
    # Fields to include in the user edit form in the admin interface
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        # ('Personal Info', {'fields': ('first_name', 'last_name', 'gender', 'email', 'profile_picture', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Customize the ordering of fields in the user edit form
    # You can rearrange the order as needed
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )


def approve_profiles(modeladmin, request, queryset):
    queryset.update(is_approved=True)
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_role', 'is_approved']
    list_filter = ['user_role', 'is_approved']
    actions = [approve_profiles]

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    pass

approve_profiles.short_description = "Approve selected profiles"
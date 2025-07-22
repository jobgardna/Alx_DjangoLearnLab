from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from .models import Author, Book, Library
from users.models import CustomUser

# Admin for CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (_('Additional Info'), {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_('Additional Info'), {'fields': ('date_of_birth', 'profile_photo')}),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'date_of_birth', 'is_staff']

# Register the custom user model with the custom admin
admin.site.register(CustomUser, CustomUserAdmin)

# Register other models
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)

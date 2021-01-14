from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
"""
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from snetw.models import Post

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    readonly_fields=['print_subscribed_users', 'print_subscribed_to_users']
    list_display = ('email', 'is_staff', 'is_active', 'bio', 'logo', 'usernamec', 'firstname', 'lastname', 'print_subscribed_users', 'print_subscribed_to_users')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'bio', 'logo', 'usernamec', 'firstname', 'lastname', 'print_subscribed_users', 'print_subscribed_to_users')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'usernamec', 'firstname', 'lastname')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)"""

admin.site.register(CustomUser)
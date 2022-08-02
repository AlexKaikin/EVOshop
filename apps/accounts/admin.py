from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Расширение',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'avatar',
                    'slug',
                ),
            },
        ),
    )

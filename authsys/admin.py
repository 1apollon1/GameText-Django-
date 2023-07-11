from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):

    readonly_fields = ('avatar_tag', )

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email", 'avatar', 'avatar_tag',)}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.

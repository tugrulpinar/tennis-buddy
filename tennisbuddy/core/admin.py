from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

from .forms import UserChangeForm, UserCreationForm
from .models import Address, User, UserFeedback


class AddressInline(admin.TabularInline):
    model = Address


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = [
        "email",
        "username",
        "terms_accepted_at",
        "marketing_list_accepted",
        "experience_level",
    ]
    readonly_fields = [
        "terms_accepted_at",
        "marketing_list_accepted_at",
        "date_joined",
        "last_login",
    ]
    list_display_links = ["email", "username"]
    inlines = [AddressInline]


CustomUserAdmin.fieldsets += (
    ("Experience", {"fields": ("experience_level",)}),
    (
        "Sign up details",
        {"fields": ("terms_accepted_at", "marketing_list_accepted_at")},
    ),
    ("Avatar", {"fields": ("avatar",)}),
    ("Description", {"fields": ("description",)}),
)

admin.site.register(User, CustomUserAdmin)
admin.site.register(UserFeedback)

admin_name = f"{settings.PROJECT_NAME} {_('Administration')}"
admin.site.site_title = admin_name
admin.site.site_header = admin_name

from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.gis import admin as gis_admin
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

from .forms import UserChangeForm, UserCreationForm
from .models import Profile, User, UserFeedback


@gis_admin.register(Profile)
class ProfileAdmin(gis_admin.GISModelAdmin):
    list_display = ["user", "gender", "experience_level"]
    fields = [
        "user",
        "gender",
        "experience_level",
        "description",
        "country",
        "location",
    ]


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = [
        "email",
        "username",
        "terms_accepted_at",
        "marketing_list_accepted",
    ]
    readonly_fields = [
        "terms_accepted_at",
        "marketing_list_accepted_at",
        "date_joined",
        "last_login",
    ]
    list_display_links = ["email", "username"]


CustomUserAdmin.fieldsets += (
    (
        "Sign up details",
        {"fields": ("terms_accepted_at", "marketing_list_accepted_at")},
    ),
)

admin.site.register(User, CustomUserAdmin)
admin.site.register(UserFeedback)

admin_name = f"{settings.PROJECT_NAME} {_('Administration')}"
admin.site.site_title = admin_name
admin.site.site_header = admin_name

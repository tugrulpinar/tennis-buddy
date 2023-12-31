from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.gis.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    terms_accepted_at = models.DateTimeField(blank=True, null=True)
    marketing_list_accepted_at = models.DateTimeField(blank=True, null=True)
    avatar = models.ImageField(_("avatar"), blank=True, null=True, upload_to="avatars/")

    @property
    def marketing_list_accepted(self) -> bool:
        return bool(self.marketing_list_accepted_at)

    def __str__(self):
        return self.username


class Profile(models.Model):
    EXPERIENCE_LEVEL_CHOICES = [
        (1.0, 1.0),
        (1.5, 1.5),
        (2.0, 2.0),
        (2.5, 2.5),
        (3.0, 3.0),
        (3.5, 3.5),
        (4.0, 4.0),
        (4.5, 4.5),
        (5.0, 5.0),
        (5.5, 5.5),
    ]
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True, blank=True
    )
    experience_level = models.FloatField(choices=EXPERIENCE_LEVEL_CHOICES, default=1.0)
    description = models.TextField(max_length=1500, null=True, blank=True)
    country = models.CharField(max_length=255)
    location = models.PointField(geography=True)

    def __str__(self):
        return self.user.username

    @property
    def coordinate(self) -> tuple:
        return self.location.coords


class UserFeedback(BaseModel):
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    email = models.EmailField(_("email"), blank=True)
    text = models.TextField(_("text"))

    def __str__(self):
        return self.text

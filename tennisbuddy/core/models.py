from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


LEVEL_CHOICES = [
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


class User(AbstractUser):
    terms_accepted_at = models.DateTimeField(blank=True, null=True)
    marketing_list_accepted_at = models.DateTimeField(blank=True, null=True)
    avatar = models.ImageField(_("avatar"), blank=True, null=True, upload_to="avatars/")
    experience_level = models.FloatField(choices=LEVEL_CHOICES, default=1.0)
    description = models.TextField(max_length=1500, null=True, blank=True)

    @property
    def marketing_list_accepted(self) -> bool:
        return bool(self.marketing_list_accepted_at)

    def __str__(self):
        return self.email


class UserFeedback(BaseModel):
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    email = models.EmailField(_("email"), blank=True)
    text = models.TextField(_("text"))

    def __str__(self):
        return self.text


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    @property
    def coordinate(self) -> tuple:
        return (self.latitude, self.longitude)

    def __str__(self):
        return f"{self.country} - {self.postal_code}"

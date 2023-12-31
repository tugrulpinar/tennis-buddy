# Generated by Django 4.2.4 on 2023-12-30 19:56

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_alter_user_avatar_alter_userfeedback_email_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("M", "Male"), ("F", "Female")],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "experience_level",
                    models.FloatField(
                        choices=[
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
                        ],
                        default=1.0,
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, max_length=1500, null=True),
                ),
                ("country", models.CharField(max_length=255)),
                (
                    "location",
                    django.contrib.gis.db.models.fields.PointField(
                        geography=True, srid=4326
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 4.2.4 on 2023-12-09 22:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0007_address"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="address",
            name="postal_code",
        ),
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("M", "Male"), ("F", "Female")],
                max_length=1,
                null=True,
            ),
        ),
    ]
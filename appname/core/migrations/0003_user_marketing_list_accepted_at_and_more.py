# Generated by Django 4.0 on 2022-03-20 14:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_userfeedback"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="marketing_list_accepted_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="terms_accepted_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

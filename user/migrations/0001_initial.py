# Generated by Django 4.1.7 on 2023-03-06 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("email", models.CharField(max_length=89, unique=True)),
                ("password", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
                (
                    "nickname",
                    models.CharField(blank=True, max_length=50, null=True, unique=True),
                ),
            ],
            options={
                "db_table": "user",
                "managed": False,
            },
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-15 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="prcie",
            field=models.PositiveIntegerField(default=0),
        ),
    ]

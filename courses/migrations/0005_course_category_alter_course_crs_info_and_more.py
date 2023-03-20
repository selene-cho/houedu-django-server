# Generated by Django 4.1.7 on 2023-03-20 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_alter_user_email"),
        ("categories", "0001_initial"),
        ("courses", "0004_rename_prcie_course_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="category",
            field=models.ForeignKey(
                blank=True,
                help_text="The category of the course.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="courses",
                to="categories.category",
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="crs_info",
            field=models.TextField(
                blank=True,
                help_text="Additional information about the course, if any.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="crs_name",
            field=models.CharField(help_text="The name of the course.", max_length=50),
        ),
        migrations.AlterField(
            model_name="course",
            name="price",
            field=models.PositiveIntegerField(
                default=0, help_text="The price of the course."
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="tcr",
            field=models.ForeignKey(
                blank=True,
                help_text="The teacher associated with the course, if any.",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="courses",
                to="users.teacher",
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="thumbnail",
            field=models.TextField(
                blank=True,
                help_text="The thumbnail image URL for the course, if any.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="lecture",
            name="crs",
            field=models.ForeignKey(
                blank=True,
                help_text="The course associated with the lecture.",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="lectures",
                to="courses.course",
            ),
        ),
        migrations.AlterField(
            model_name="lecture",
            name="lctr_info",
            field=models.TextField(
                blank=True,
                help_text="Additional information about the lecture, if any.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="lecture",
            name="lctr_name",
            field=models.CharField(help_text="The name of the lecture.", max_length=50),
        ),
        migrations.AlterField(
            model_name="lecture",
            name="lctr_source",
            field=models.TextField(help_text="the source code for the lecture."),
        ),
    ]

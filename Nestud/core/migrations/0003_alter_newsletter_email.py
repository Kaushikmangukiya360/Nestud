# Generated by Django 5.0 on 2024-09-04 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_course_image_alter_internshipapplication_applicant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.CharField(max_length=254),
        ),
    ]

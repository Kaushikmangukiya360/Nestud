# Generated by Django 5.0 on 2024-09-03 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default=1, upload_to='mentor/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='internshipapplication',
            name='applicant',
            field=models.CharField(max_length=254),
        ),
    ]
# Generated by Django 4.0.4 on 2022-06-27 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_coursedetail_specialization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='faculty_image',
            field=models.ImageField(default='images/faculty/faculty.png', upload_to='images/faculty/'),
        ),
    ]

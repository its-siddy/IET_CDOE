# Generated by Django 4.0.4 on 2022-06-24 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_review_course_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='useful_link',
            field=models.ManyToManyField(to='main.useful_links'),
        ),
    ]

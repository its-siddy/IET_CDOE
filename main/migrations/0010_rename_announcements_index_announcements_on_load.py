# Generated by Django 4.0.4 on 2022-06-25 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_merge_20220625_2256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='index',
            old_name='announcements',
            new_name='announcements_on_load',
        ),
    ]

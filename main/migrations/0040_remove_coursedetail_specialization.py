# Generated by Django 4.0.4 on 2022-06-27 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_alter_coursedetail_specialization'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursedetail',
            name='specialization',
        ),
    ]

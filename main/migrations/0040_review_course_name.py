# Generated by Django 4.0.4 on 2022-05-30 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_remove_review_negative'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='course_name',
            field=models.ForeignKey(default='Introduction To Data Science', on_delete=django.db.models.deletion.CASCADE, to='main.course_head'),
        ),
    ]

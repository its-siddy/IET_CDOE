# Generated by Django 4.0.4 on 2022-05-14 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_notice_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('linked_in', models.URLField()),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
            ],
        ),
    ]

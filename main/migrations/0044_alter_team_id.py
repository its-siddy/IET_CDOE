# Generated by Django 4.0.6 on 2022-07-22 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_alter_coursedetail_card_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]

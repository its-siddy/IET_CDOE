# Generated by Django 4.0.4 on 2022-06-26 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_index_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='contact_num',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='email_id',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='fb_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='insta_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='map_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='twitter_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]

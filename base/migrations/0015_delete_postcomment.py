# Generated by Django 4.0.4 on 2022-05-30 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_post_thumbnail_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostComment',
        ),
    ]

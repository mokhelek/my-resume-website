# Generated by Django 4.0.4 on 2022-07-15 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='subject',
            field=models.CharField(max_length=300),
        ),
    ]

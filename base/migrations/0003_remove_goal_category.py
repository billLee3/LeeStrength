# Generated by Django 3.2.9 on 2022-01-01 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_goal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='category',
        ),
    ]

# Generated by Django 4.0 on 2022-01-02 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_weight_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
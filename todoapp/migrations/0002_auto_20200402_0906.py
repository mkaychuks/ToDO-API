# Generated by Django 2.2.10 on 2020-04-02 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='time_created',
            field=models.TimeField(auto_now=True),
        ),
    ]

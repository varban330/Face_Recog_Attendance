# Generated by Django 2.0.6 on 2018-11-10 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_system', '0004_auto_20181109_0628'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]

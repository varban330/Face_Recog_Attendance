# Generated by Django 2.0.6 on 2018-11-09 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_system', '0003_auto_20181109_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_pic',
            field=models.FileField(default='profile-photo.jpg', upload_to='media'),
        ),
    ]

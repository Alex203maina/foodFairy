# Generated by Django 5.1.2 on 2024-11-29 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_customuser_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='dark_mode',
            field=models.BooleanField(default=False),
        ),
    ]

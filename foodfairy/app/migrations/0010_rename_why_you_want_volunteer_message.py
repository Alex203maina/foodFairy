# Generated by Django 5.1.2 on 2024-11-21 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_volunteer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteer',
            old_name='why_you_want',
            new_name='message',
        ),
    ]
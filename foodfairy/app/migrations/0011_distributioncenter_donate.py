# Generated by Django 5.1.2 on 2024-11-26 08:13

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_why_you_want_volunteer_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistributionCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('contact_person', models.CharField(max_length=255)),
                ('contact_phone', models.CharField(max_length=255)),
                ('capacity', models.PositiveIntegerField()),
                ('current_stock', models.PositiveIntegerField()),
                ('operation_hour', models.CharField(blank=True, max_length=255, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Distribution Center',
                'verbose_name_plural': 'Distribution Center',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_type', models.CharField(choices=[('food', 'Food'), ('money', 'Money'), ('clothing', 'Clothing'), ('other', 'Other')], default='food', max_length=50)),
                ('description', models.TextField(blank=True)),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('received', 'Received'), ('distributed', 'Distributed')], default='pending', max_length=20)),
                ('is_distributed', models.BooleanField(default=False)),
                ('date_donated', models.DateTimeField(default=django.utils.timezone.now)),
                ('beneficiary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_donations', to='app.beneficiary')),
                ('distribution_center', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='DistributionCenter', to='app.distributioncenter')),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_donated'],
            },
        ),
    ]
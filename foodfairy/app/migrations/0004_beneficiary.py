# Generated by Django 5.1.2 on 2024-11-21 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('family_size', models.PositiveIntegerField(blank=True, null=True)),
                ('institution_size', models.PositiveIntegerField(blank=True, null=True)),
                ('beneficiary_type', models.CharField(choices=[('individual', 'Individual'), ('family', 'Family'), ('institution', 'Institution'), ('community', 'Community')], max_length=100)),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('pending', 'Pending')], default='active', max_length=50)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Beneficiary',
                'verbose_name_plural': 'Beneficiaries',
                'ordering': ['full_name'],
            },
        ),
    ]
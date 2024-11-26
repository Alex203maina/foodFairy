# Generated by Django 5.1.2 on 2024-11-26 12:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_distributioncenter_donate'),
    ]

    operations = [
        migrations.AddField(
            model_name='donate',
            name='is_perishable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='donate',
            name='shelf_life',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='donate',
            name='distribution_center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='donations_received', to='app.distributioncenter'),
        ),
    ]

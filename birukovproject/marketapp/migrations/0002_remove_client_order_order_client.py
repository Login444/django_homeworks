# Generated by Django 5.0.3 on 2024-04-01 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='client',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='marketapp.client'),
            preserve_default=False,
        ),
    ]

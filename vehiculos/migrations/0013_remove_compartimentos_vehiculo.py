# Generated by Django 3.0 on 2020-04-03 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0012_auto_20200325_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compartimentos',
            name='vehiculo',
        ),
    ]

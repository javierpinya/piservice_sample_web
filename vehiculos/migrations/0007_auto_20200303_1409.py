# Generated by Django 3.0 on 2020-03-03 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0006_auto_20200301_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='equipos',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Indicar equipos adicionales'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='observaciones',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Observaciones'),
        ),
    ]

# Generated by Django 2.1 on 2020-03-23 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0007_auto_20200303_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='fechaadr',
            field=models.DateField(verbose_name='Fecha ADR'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='fechaitv',
            field=models.DateField(verbose_name='Fecha ITV'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='fechatablas',
            field=models.DateField(verbose_name='Fecha Tablas Calibración'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='fechatarjetatte',
            field=models.DateField(verbose_name='Fecha Tarjeta Tte'),
        ),
    ]
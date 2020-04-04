# Generated by Django 3.0 on 2020-04-03 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='driver',
            field=models.IntegerField(choices=[(1, 'ANTONIO GARCÍA'), (2, 'ISABEL GÓMEZ'), (3, 'JUAN MÉNDEZ'), (4, 'PABLO GARCÍA ')], default=1, verbose_name='Conductor'),
        ),
    ]

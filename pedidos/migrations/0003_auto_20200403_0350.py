# Generated by Django 3.0 on 2020-04-03 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_auto_20200403_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='cantidad1',
            field=models.IntegerField(default=0, verbose_name='Cantidad'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='cantidad2',
            field=models.IntegerField(default=0, verbose_name='Cantidad'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='cantidad3',
            field=models.IntegerField(default=0, verbose_name='Cantidad'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='cantidad4',
            field=models.IntegerField(default=0, verbose_name='Cantidad'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='cantidad5',
            field=models.IntegerField(default=0, verbose_name='Cantidad'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='cantidad6',
            field=models.IntegerField(default=0, verbose_name='Cantidad'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='producto1',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Producto'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='producto2',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Producto'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='producto3',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Producto'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='producto4',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Producto'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='producto5',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Producto'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='producto6',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Producto'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-14 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_producto_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(null=True),
        ),
    ]

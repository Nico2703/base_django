# Generated by Django 5.0.6 on 2024-05-14 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0003_compra_cantidad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compra',
            old_name='precio',
            new_name='precio_total',
        ),
    ]
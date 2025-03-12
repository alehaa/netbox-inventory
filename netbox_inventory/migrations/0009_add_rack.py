# Generated by Django 5.0.9 on 2024-12-11 16:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('netbox_inventory', '0008_alter_asset_device_type_alter_asset_module_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asset',
            options={
                'ordering': (
                    'device_type',
                    'module_type',
                    'inventoryitem_type',
                    'rack_type',
                    'serial',
                )
            },
        ),
        migrations.AddField(
            model_name='asset',
            name='rack',
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='assigned_asset',
                to='dcim.rack',
            ),
        ),
        migrations.AddField(
            model_name='asset',
            name='rack_type',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='assets',
                to='dcim.racktype',
            ),
        ),
        migrations.AddConstraint(
            model_name='asset',
            constraint=models.UniqueConstraint(
                fields=('rack_type', 'serial'), name='unique_rack_type_serial'
            ),
        ),
    ]

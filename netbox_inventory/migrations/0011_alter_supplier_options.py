# Generated by Django 5.1.5 on 2025-03-16 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_inventory', '0010_asset_description_inventoryitemtype_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supplier',
            options={'ordering': ('name',)},
        ),
    ]

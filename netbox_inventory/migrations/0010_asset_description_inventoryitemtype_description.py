# Generated by Django 5.1.6 on 2025-03-12 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_inventory', '0009_add_rack'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='inventoryitemtype',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

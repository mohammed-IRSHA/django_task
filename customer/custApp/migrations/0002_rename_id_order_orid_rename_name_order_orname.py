# Generated by Django 5.1.2 on 2024-10-22 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='id',
            new_name='orid',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='orname',
        ),
    ]

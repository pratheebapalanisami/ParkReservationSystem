# Generated by Django 2.2.6 on 2020-04-08 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aafieldapp', '0002_auto_20200407_1416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='Customer_Name',
            new_name='Reservation_ID',
        ),
    ]
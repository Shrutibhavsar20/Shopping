# Generated by Django 5.0.6 on 2024-07-16 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_cart_size'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order_details',
        ),
    ]

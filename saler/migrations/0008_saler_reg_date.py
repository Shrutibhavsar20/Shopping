# Generated by Django 5.0.6 on 2024-08-02 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0007_remove_saler_reg_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='saler_reg',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
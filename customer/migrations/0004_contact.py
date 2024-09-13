# Generated by Django 5.0.6 on 2024-07-04 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('contact', models.BigIntegerField()),
                ('message', models.TextField()),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'contact',
            },
        ),
    ]

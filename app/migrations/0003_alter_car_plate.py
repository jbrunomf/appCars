# Generated by Django 5.1.1 on 2024-10-11 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_car_plate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='plate',
            field=models.CharField(blank=True, max_length=7, null=True, unique=True),
        ),
    ]

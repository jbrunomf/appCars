# Generated by Django 5.1.1 on 2024-10-15 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_car_plate'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarInventory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cars_count', models.IntegerField()),
                ('cars_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]

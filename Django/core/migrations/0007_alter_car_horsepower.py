# Generated by Django 5.0.4 on 2024-05-06 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_plane_capacity_plane_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='horsepower',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Лошадиная сила'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-07 19:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shop',
            options={'ordering': ['created_at'],
                     'verbose_name': 'Товар',
                     'verbose_name_plural': 'Товары'},
        ),
        migrations.AddField(
            model_name='shop',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True,
                                       default=django.utils.timezone.now,
                                       verbose_name='Дата публикации'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='updated_at',
            field=models.DateTimeField(auto_now=True,
                                       verbose_name='Дата обновление'),
        ),
    ]

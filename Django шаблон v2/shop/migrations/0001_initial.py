# Generated by Django 5.0.6 on 2024-05-07 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('info', models.TextField(blank=True, verbose_name='Информация')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/$Y/$m/$d/', verbose_name='Фото')),
                ('in_stock', models.BooleanField(default=True, verbose_name='В наличии')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]

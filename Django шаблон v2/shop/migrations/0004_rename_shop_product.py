# Generated by Django 5.0.4 on 2024-05-18 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_category_alter_shop_photo_shop_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shop',
            new_name='Product',
        ),
    ]

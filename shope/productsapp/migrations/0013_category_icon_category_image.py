# Generated by Django 4.2 on 2023-06-05 19:15
# flake8: noqa
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0012_product_is_limited'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='categories_icons/', verbose_name='icon'),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories_images/', verbose_name='image'),
        ),
    ]

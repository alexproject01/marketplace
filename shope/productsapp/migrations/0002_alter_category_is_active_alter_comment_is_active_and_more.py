# Generated by Django 4.2 on 2023-04-22 13:39
# flake8: noqa

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='discount',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='specific',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='typespecific',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 4.2 on 2023-06-28 11:33
# flake8: noqa
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('fio', models.CharField(max_length=100, verbose_name='FIO')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='phone number')),
                ('status', models.CharField(choices=[('paid', 'Paid'), ('not paid', 'Not paid for')], default='not paid', max_length=20, verbose_name='status')),
                ('city', models.CharField(max_length=50, verbose_name='city')),
                ('address', models.CharField(max_length=100, verbose_name='address')),
                ('delivery_type', models.CharField(choices=[('Default delivery', 'Default delivery'), ('Express delivery', 'Express delivery')], default='Default delivery', max_length=20, verbose_name='delivery type')),
                ('delivery_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='delivery price')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='total price')),
                ('total_discounted_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='total discounted price')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('count', models.PositiveSmallIntegerField(verbose_name='count')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='price')),
                ('discounted_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='discounted price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='orderapp.order', verbose_name='order')),
            ],
            options={
                'verbose_name': 'order item',
                'verbose_name_plural': 'order items',
            },
        ),
    ]

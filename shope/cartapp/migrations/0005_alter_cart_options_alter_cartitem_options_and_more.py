# Generated by Django 4.2 on 2023-05-11 15:39
# flake8: noqa
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productsapp', '0006_review_remove_product_is_delivered_and_more'),
        ('cartapp', '0004_alter_cartitem_quantity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'cart', 'verbose_name_plural': 'carts'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'item in cart', 'verbose_name_plural': 'items in cart'},
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cartapp.cart', verbose_name='cart'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartitems', to='productsapp.product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='quantity'),
        ),
    ]

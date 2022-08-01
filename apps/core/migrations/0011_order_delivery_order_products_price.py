# Generated by Django 4.0.5 on 2022-07-28 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_order_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10, verbose_name='Стоимость доставки, руб'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='products_price',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10, verbose_name='Стоимость товаров, руб'),
            preserve_default=False,
        ),
    ]
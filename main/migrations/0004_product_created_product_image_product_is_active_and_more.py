# Generated by Django 4.0.5 on 2022-06-21 05:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_product_country_alter_product_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='img/product/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активация товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]

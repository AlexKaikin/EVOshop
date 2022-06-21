# Generated by Django 4.0.5 on 2022-06-21 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('tea', 'Чай'), ('coffee', 'Кофе'), ('spices', 'Специи')], default='tea', max_length=20, verbose_name='Категория'),
        ),
    ]

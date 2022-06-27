# Generated by Django 4.0.5 on 2022-06-21 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_product_created_alter_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('1', 'Чай'), ('2', 'Кофе'), ('3', 'Специи')], default='tea', max_length=20, verbose_name='Категория'),
        ),
    ]
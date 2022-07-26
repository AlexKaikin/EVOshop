# Generated by Django 4.0.5 on 2022-07-25 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_setting_delivery_setting_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='Количество'),
        ),
    ]

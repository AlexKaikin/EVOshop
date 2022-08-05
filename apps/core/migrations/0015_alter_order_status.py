# Generated by Django 4.0.5 on 2022-08-03 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('1', 'Не обработан'), ('2', 'Отменён'), ('3', 'В работе'), ('4', 'Отправлен доставкой'), ('5', 'Получен клиентом')], default='1', max_length=1, verbose_name='Статус заказа'),
        ),
    ]
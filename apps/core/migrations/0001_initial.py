# Generated by Django 4.0.5 on 2022-07-14 12:52

import apps.core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
                ('status', models.CharField(choices=[('no', 'Нет'), ('yes', 'Да')], default='yes', max_length=3, verbose_name='Опубликована')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('image', models.FileField(upload_to=apps.core.models.get_category_file_path, verbose_name='Изображение категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Отчество')),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True, verbose_name='Email')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('address', models.CharField(max_length=50, verbose_name='Адрес')),
                ('postal_code', models.CharField(max_length=20, verbose_name='Почтовый код')),
                ('comment', models.TextField(blank=True, default=None, null=True, verbose_name='Комментарий')),
                ('status', models.CharField(choices=[('1', 'Не обработан'), ('2', 'Отправлен доставкой'), ('3', 'Получен клиентом')], default='1', max_length=1, verbose_name='Статус заказа')),
                ('paid', models.CharField(choices=[('no', 'Нет'), ('yes', 'Да')], default='no', max_length=3, verbose_name='Оплачен')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, verbose_name='URL')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('country', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Страна')),
                ('town', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Город')),
                ('year', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Год')),
                ('volume', models.IntegerField(verbose_name='Вес, грамм')),
                ('price', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Цена, руб')),
                ('stock', models.PositiveIntegerField(verbose_name='Остаток на складе, штук')),
                ('tag', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Метки')),
                ('talk_forum', models.URLField(blank=True, default=None, null=True, verbose_name='Ссылка на форум')),
                ('status', models.CharField(choices=[('no', 'Нет'), ('yes', 'Да')], default='yes', max_length=3, verbose_name='Опубликован')),
                ('image', models.FileField(upload_to=apps.core.models.get_product_file_path, verbose_name='Изображение обложки')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='core.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ('-created',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Текст')),
                ('rating', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], max_length=1, verbose_name='Рейтинг')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('status', models.CharField(choices=[('1', 'На проверке'), ('2', 'Опубликован'), ('3', 'Отклонён')], default='1', max_length=1, verbose_name='Статус отзыва')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='core.product', verbose_name='Продукт')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to=apps.core.models.get_product_image_file_path, verbose_name='Фотографии')),
                ('status', models.CharField(choices=[('no', 'Нет'), ('yes', 'Да')], default='yes', max_length=3, verbose_name='Опубликована')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Стоимость')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='core.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_items', to='core.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]

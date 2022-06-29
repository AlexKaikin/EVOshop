# Generated by Django 4.0.5 on 2022-06-29 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('core', '0001_initial'), ('core', '0002_alter_product_country_alter_product_tag_and_more'), ('core', '0003_alter_product_country_alter_product_price_and_more'), ('core', '0004_product_created_product_image_product_is_active_and_more'), ('core', '0005_alter_product_created_alter_product_image_and_more'), ('core', '0006_alter_product_category'), ('core', '0007_alter_product_category'), ('core', '0008_alter_product_category_alter_product_created_and_more'), ('core', '0009_productimage'), ('core', '0010_statusorder_alter_productimage_options_and_more'), ('core', '0011_category_alter_order_status_alter_product_image_and_more'), ('core', '0012_alter_product_image_alter_productimage_image_extuser'), ('core', '0013_rename_extuser_profile'), ('core', '0014_alter_category_name_alter_product_category'), ('core', '0015_alter_product_category'), ('core', '0016_alter_product_category'), ('core', '0017_alter_product_category'), ('core', '0018_category_image'), ('core', '0019_category_url'), ('core', '0020_alter_category_url'), ('core', '0021_comment'), ('core', '0022_alter_comment_options'), ('core', '0023_rename_comment_review'), ('core', '0024_alter_review_options_rename_post_review_product'), ('core', '0025_alter_productimage_product_alter_review_product'), ('core', '0026_alter_review_product')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активация товара')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
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
                ('comment', models.TextField(blank=True, default=None, null=True, verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.statusorder', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_logged', models.BooleanField(default=True, verbose_name='Авторизован')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Категория')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активация категории')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('image', models.ImageField(default=django.utils.timezone.now, upload_to='category/', verbose_name='Изображение категории')),
                ('url', models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Ссылка на Категорию')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category', verbose_name='Категория')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('country', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Страна')),
                ('town', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Город')),
                ('year', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Год')),
                ('volume', models.IntegerField(verbose_name='Вес, грамм')),
                ('price', models.IntegerField(verbose_name='Цена, руб')),
                ('tag', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Метки')),
                ('talk_forum', models.URLField(blank=True, default=None, null=True, verbose_name='Ссылка на форум')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('image', models.ImageField(upload_to='product/', verbose_name='Изображение обложки')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активация товара')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product/', verbose_name='Фотографии')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активация изображения')),
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
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='core.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]

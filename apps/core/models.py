from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=20, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name="URL")
    is_active = models.BooleanField(default=True, verbose_name="Активация категории")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Дата изменения')
    image = models.ImageField(upload_to='category/', verbose_name='Изображение категории')
    url = models.CharField(max_length=30, blank=True, null=True, default=None, verbose_name='Ссылка на Категорию')

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name="URL")
    desc = models.TextField(verbose_name='Описание')
    country = models.CharField(max_length=50, blank=True, null=True, default=None, verbose_name='Страна')
    town = models.CharField(max_length=50, blank=True, null=True, default=None, verbose_name='Город')
    year = models.CharField(max_length=50, blank=True, null=True, default=None, verbose_name='Год')
    volume = models.IntegerField(verbose_name='Вес, грамм')
    price = models.IntegerField(verbose_name='Цена, руб')
    stock = models.PositiveIntegerField(verbose_name='Остаток на складе, штук')
    tag = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name='Метки')
    talk_forum = models.URLField(blank=True, null=True, default=None, verbose_name='Ссылка на форум')
    is_active = models.BooleanField(default=True, verbose_name="Активация товара")
    image = models.ImageField(upload_to='product/', verbose_name='Изображение обложки')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, blank=True, null=True,
                                default=None,
                                verbose_name='Товар')
    image = models.ImageField(upload_to='product/', verbose_name='Фотографии')
    is_active = models.BooleanField(default=True, verbose_name="Активация изображения")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return str(self.product)


class Review(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    description = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', blank=True, null=True,
                                verbose_name='Продукт')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Автор')
    status = models.BooleanField(default=False, verbose_name='Видимость отзыва')

    # def __str__(self):
    #     return self.description
    #
    # def get_absolute_url(self):
    #     return reverse('main')


class StatusOrder(models.Model):
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    name = models.CharField(max_length=50, verbose_name='Название')
    is_active = models.BooleanField(default=True, verbose_name="Активация товара")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.name


class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    email = models.EmailField(blank=True, null=True, default=None, verbose_name='Email')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    address = models.CharField(max_length=50, verbose_name='Адрес')
    comment = models.TextField(blank=True, null=True, default=None, verbose_name='Комментарий')
    status = models.ForeignKey(StatusOrder, on_delete=models.SET_NULL, null=True, verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return str(self.id)


class Profile(models.Model):  # расширяет модель User, таблица для связи 1 с 1

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Имя')
    is_logged = models.BooleanField(default=True, verbose_name='Авторизован')

    def __str__(self):
        return self.user.username

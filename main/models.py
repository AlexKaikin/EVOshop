from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=50, verbose_name='Название')
    is_active = models.BooleanField(default=True, verbose_name="Активация категории")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    TYPES = (
        ('1', 'Чай'),
        ('2', 'Кофе'),
        ('3', 'Специи')
    )

    category = models.CharField(max_length=20, verbose_name='Категория', choices=TYPES, default='1')
    name = models.CharField(max_length=50, verbose_name='Название')
    desc = models.TextField(verbose_name='Описание')
    country = models.CharField(max_length=50, blank=True, null=True, default=None, verbose_name='Страна')
    town = models.CharField(max_length=50, blank=True, null=True, default=None, verbose_name='Город')
    year = models.CharField(max_length=50, blank=True, null=True, default=None, verbose_name='Год')
    volume = models.IntegerField(verbose_name='Вес, грамм')
    price = models.IntegerField(verbose_name='Цена, руб')
    tag = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name='Метки')
    talk_forum = models.URLField(blank=True, null=True, default=None, verbose_name='Ссылка на форум')
    is_active = models.BooleanField(default=True, verbose_name="Активация товара")
    image = models.ImageField(upload_to='static/media/product/', verbose_name='Изображение обложки')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Дата изменения')
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None,
                                verbose_name='Товар')
    image = models.ImageField(upload_to='static/media/product/', verbose_name='Фотографии')
    is_active = models.BooleanField(default=True, verbose_name="Активация изображения")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return str(self.product)


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

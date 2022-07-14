from django.db import models


def get_category_file_path(instance, filename):
    # return os.path.join("%s" % instance.slug, filename)
    return '{0}/{1}/{2}'.format('category', instance.slug, filename)


def get_product_file_path(instance, filename):
    return '{0}/{1}/{2}'.format('product', instance.slug, filename)


def get_product_image_file_path(instance, filename):
    return '{0}/{1}/{2}'.format('product', instance.product.slug, filename)


class Category(models.Model):
    """ Категории """

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    STATUS = (
        ('no', 'Нет'),
        ('yes', 'Да')
    )

    name = models.CharField(max_length=20, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name="URL")
    status = models.CharField(choices=STATUS, default='yes', max_length=3, verbose_name="Опубликована")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Дата изменения')
    image = models.FileField(upload_to=get_category_file_path, verbose_name='Изображение категории')

    def __str__(self):
        return self.name


class Product(models.Model):
    """ Товары """

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)
        ordering = ('-created',)

    STATUS = (
        ('no', 'Нет'),
        ('yes', 'Да')
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name="URL")
    desc = models.TextField(verbose_name='Описание')
    country = models.CharField(max_length=50, blank=True, null=True, default=None, verbose_name='Страна')
    town = models.CharField(max_length=50, blank=True, null=True, default=None, verbose_name='Город')
    year = models.CharField(max_length=50, blank=True, null=True, default=None, verbose_name='Год')
    volume = models.IntegerField(verbose_name='Вес, грамм')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Цена, руб')
    stock = models.PositiveIntegerField(verbose_name='Остаток на складе, штук')
    tag = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name='Метки')
    talk_forum = models.URLField(blank=True, null=True, default=None, verbose_name='Ссылка на форум')
    status = models.CharField(choices=STATUS, default='yes', max_length=3, verbose_name="Опубликован")
    image = models.FileField(upload_to=get_product_file_path, verbose_name='Изображение обложки')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    """ Фотографии к товару """

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    STATUS = (
        ('no', 'Нет'),
        ('yes', 'Да')
    )

    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, blank=True, null=True,
                                default=None,
                                verbose_name='Товар')
    image = models.FileField(upload_to=get_product_image_file_path, verbose_name='Фотографии')
    status = models.CharField(choices=STATUS, default='yes', max_length=3, verbose_name="Опубликована")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return str(self.product)


class Review(models.Model):
    """ Отзывы и рейтинги """

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-created',)

    RATING = (
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5)
    )

    STATUS = (
        ('1', 'На проверке'),
        ('2', 'Опубликован'),
        ('3', 'Отклонён')
    )

    description = models.TextField(verbose_name='Текст')
    rating = models.CharField(choices=RATING, max_length=1, verbose_name='Рейтинг')
    created = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', blank=True, null=True,
                                verbose_name='Продукт')
    profile = models.ForeignKey('authentication.Profile', on_delete=models.CASCADE, related_name='reviews',
                                blank=True, null=True,
                                verbose_name='Автор')
    status = models.CharField(choices=STATUS, default='1', max_length=1, verbose_name='Статус отзыва')

    # def __str__(self):
    #     return self.description
    #
    # def get_absolute_url(self):
    #     return reverse('main')


class Order(models.Model):
    """ Заказы """

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-created',)

    STATUS = (
        ('1', 'Не обработан'),
        ('2', 'Отправлен доставкой'),
        ('3', 'Получен клиентом')
    )

    PAID = (
        ('no', 'Нет'),
        ('yes', 'Да')
    )

    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    email = models.EmailField(blank=True, null=True, default=None, verbose_name='Email')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    address = models.CharField(max_length=50, verbose_name='Адрес')
    postal_code = models.CharField(max_length=20, verbose_name='Почтовый код')
    comment = models.TextField(blank=True, null=True, default=None, verbose_name='Комментарий')
    status = models.CharField(choices=STATUS, default='1', max_length=1, verbose_name='Статус заказа')
    paid = models.CharField(choices=PAID, default='no', max_length=3, verbose_name='Оплачен')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    profile = models.ForeignKey('authentication.Profile', on_delete=models.CASCADE, related_name='orders',
                                blank=True, null=True,
                                verbose_name='Пользователь')

    def __str__(self):
        return 'Заказ №{}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """ Товары в заказе """

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items', verbose_name='Товар')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Стоимость')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

from django.db import models
from django.urls import reverse
from pytils import translit


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
        ordering = ('-updated', '-created',)

    PUBLISHED = (
        ('no', 'Нет'),
        ('yes', 'Да')
    )

    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True, blank=True, unique=True, verbose_name="URL")
    published = models.CharField(choices=PUBLISHED, default='yes', max_length=3, verbose_name="Опубликована")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    image = models.FileField(upload_to=get_category_file_path, verbose_name='Изображение категории')

    def save(self, *args, **kwargs):
        name = self.name
        self.slug = translit.slugify(name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})


class Product(models.Model):
    """ Товары """

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)
        ordering = ('-updated', '-created',)

    PUBLISHED = (
        ('no', 'Нет'),
        ('yes', 'Да')
    )

    name = models.CharField(max_length=50, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True, blank=True, unique=True, verbose_name="URL")
    desc = models.TextField(verbose_name='Описание')
    country = models.CharField(max_length=50, blank=True, null=True, default=None, verbose_name='Страна')
    town = models.CharField(max_length=50, blank=True, null=True, default=None, verbose_name='Город')
    year = models.CharField(max_length=50, blank=True, null=True, default=None, verbose_name='Год')
    volume = models.IntegerField(verbose_name='Вес, грамм')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Цена, руб')
    stock = models.PositiveIntegerField(verbose_name='Остаток на складе, штук')
    talk_forum = models.URLField(blank=True, null=True, default=None, verbose_name='Ссылка на форум')
    published = models.CharField(choices=PUBLISHED, default='yes', max_length=3, verbose_name="Опубликован")
    image = models.FileField(upload_to=get_product_file_path, verbose_name='Изображение обложки')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    tag = models.ManyToManyField('Tag', related_name='tags', blank=True, verbose_name='Метки')

    def save(self, *args, **kwargs):
        name = self.name
        self.slug = translit.slugify(name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})

    # def get_review(self):
    #     return self.reviews.filter(parent__isnull=True, published='yes').select_related('profile')


class Tag(models.Model):
    """ Метки к товару """

    class Meta:
        verbose_name = 'Метки'
        verbose_name_plural = 'Метки'

    name = models.CharField(max_length=50, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=50, db_index=True, blank=True, unique=True, verbose_name="URL")

    def save(self, *args, **kwargs):
        name = self.name
        self.slug = translit.slugify(name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    """ Фотографии к товару """

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    PUBLISHED = (
        ('no', 'Нет'),
        ('yes', 'Да')
    )

    image = models.FileField(upload_to=get_product_image_file_path, verbose_name='Фотография', blank=True)
    published = models.CharField(choices=PUBLISHED, default='yes', max_length=3, verbose_name="Опубликована")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, blank=True, null=True,
                                default=None, verbose_name='Товар')

    def __str__(self):
        return str(self.product)


class Review(models.Model):
    """ Отзывы и рейтинги """

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-created',)

    class Rating(models.IntegerChoices):
        NO = 0, 'Без рейтинга'
        FIVE = 5, '★★★★★'
        FOUR = 4, '★★★★☆'
        THREE = 3, '★★★☆☆'
        TWO = 2, '★★☆☆☆'
        ONE = 1, '★☆☆☆☆'

    PUBLISHED = (
        ('checking', 'На проверке'),
        ('yes', 'Опубликован'),
        ('no', 'Отклонён')
    )

    description = models.TextField(verbose_name='Отзыв')
    rating = models.IntegerField(choices=Rating.choices, verbose_name='Рейтинг')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    published = models.CharField(choices=PUBLISHED, default='checking', max_length=8, verbose_name='Статус отзыва')

    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, related_name='children', blank=True, null=True, verbose_name='Родитель'
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', blank=True, null=True,
                                verbose_name='Продукт')
    profile = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, related_name='reviews',
                                blank=True, null=True, verbose_name='Автор')

    def __str__(self):
        return 'Отзыв №{}'.format(self.id)


class Order(models.Model):
    """ Заказы """

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-created',)

    STATUS = (
        ('1', 'Не обработан'),
        ('2', 'Отменён'),
        ('3', 'В работе'),
        ('4', 'Отправлен доставкой'),
        ('5', 'Получен клиентом')
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
    products_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                         verbose_name='Стоимость товаров, руб')
    delivery = models.DecimalField(max_digits=10, decimal_places=0, blank=True, verbose_name='Стоимость доставки, руб')
    total_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, verbose_name='Стоимость заказа, руб')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    profile = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, related_name='orders',
                                blank=True, null=True, verbose_name='Пользователь')

    def __str__(self):
        return 'Заказ №{}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_absolute_url(self):
        return reverse('profile_order_detail', kwargs={'pk': self.pk})


class OrderItem(models.Model):
    """ Товары в заказе """

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items', verbose_name='Товар')

    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Стоимость')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


class Setting(models.Model):
    """
    Настройки сайта:
    - бесплатная доставка
    """
    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'

    name = models.CharField(max_length=50, verbose_name='Настройки')
    delivery = models.PositiveIntegerField(default=0, verbose_name='Доставка, руб.')
    delivery_free = models.PositiveIntegerField(default=0, verbose_name='Бесплатная доставка от, руб.')

    def __str__(self):
        return self.name


class Message(models.Model):
    """
    Сообщения со страницы контактов
    """
    class Meta:
        verbose_name = 'Сообщения'
        verbose_name_plural = 'Сообщения'

    name = models.CharField(max_length=50, verbose_name='Ваше имя')
    email = models.EmailField(blank=True, null=True, default=None, verbose_name='Ваш e-mail')
    message = models.TextField(blank=True, null=True, default=None, verbose_name='Сообщение')

    def __str__(self):
        return 'Сообщение №{}'.format(self.id)


class Subscribe(models.Model):
    """ Подписка на рассылку новостей на email """
    class Meta:
        verbose_name = 'E-mail рассылка'
        verbose_name_plural = 'E-mail рассылка'

    email = models.EmailField(unique=True,)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата подписки')

    def __str__(self):
        return self.email

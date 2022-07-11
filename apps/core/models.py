from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    """ Категории """

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=20, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name="URL")
    is_active = models.BooleanField(default=True, verbose_name="Активация категории")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Дата изменения')
    image = models.FileField(upload_to='category/', verbose_name='Изображение категории')
    url = models.CharField(max_length=30, blank=True, null=True, default=None, verbose_name='Ссылка на Категорию')

    def __str__(self):
        return self.name


class Product(models.Model):
    """ Товары """

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)
        ordering = ('-created',)

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
    is_active = models.BooleanField(default=True, verbose_name="Активация товара")
    image = models.FileField(upload_to='product/', verbose_name='Изображение обложки')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    """ Фотографии к товару """

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, blank=True, null=True,
                                default=None,
                                verbose_name='Товар')
    image = models.FileField(upload_to='product/', verbose_name='Фотографии')
    is_active = models.BooleanField(default=True, verbose_name="Активация изображения")
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

    description = models.TextField(verbose_name='Текст')
    rating = models.CharField(choices=RATING, max_length=1, verbose_name='Рейтинг')
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


class Profile(models.Model):  # расширяет модель User, таблица для связи 1 с 1
    """ Профиль пользователя """

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Имя')
    is_logged = models.BooleanField(default=True, verbose_name='Авторизован')

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """ Создание профиля пользователя при регистрации """
        if created:
            Profile.objects.create(user=instance)  # id=instance.id

    @receiver
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


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
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='orders', blank=True, null=True,
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

from django.conf import settings

from apps.core.models import Product


class Compare(object):

    def __init__(self, request):
        """ Инициализируем хранилище для сравнения """
        self.session = request.session
        compare = self.session.get(settings.COMPARE_SESSION_ID)
        if not compare:
            compare = self.session[settings.COMPARE_SESSION_ID] = {}
        self.compare = compare

    def add(self, product):
        """ Добавить товар в хранилище для сравнения """
        product_id = str(product.id)
        if product_id not in self.compare:
            self.compare[product_id] = {'item': 1}
        # else:
        #     del self.compare[product_id]
        self.save()

    def save(self):
        # Обновление сессии compare
        self.session[settings.COMPARE_SESSION_ID] = self.compare
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, product):
        """ Удаление товара из сравнения """
        product_id = str(product.id)
        if product_id in self.compare:
            del self.compare[product_id]
            self.save()

    def __iter__(self):
        """ Перебор элементов и получение товаров из базы данных """
        product_ids = self.compare.keys()
        # получение объектов product и добавление их в хранилище
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.compare[str(product.id)]['product'] = product

        for item in self.compare.values():
            # item['price'] = item['price']
            # item['total_price'] = item['price'] * item['item']
            yield item

    def __len__(self):
        """ Подсчет всех товаров в хранилище """
        return sum(item['item'] for item in self.compare.values())

    def clear(self):
        # удаление хранилища из сессии
        del self.session[settings.COMPARE_SESSION_ID]
        self.session.modified = True

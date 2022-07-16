from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Category, Product, OrderItem
from .forms import ReviewForm, OrderCreateForm
from apps.cart.forms import CartAddProductForm
from apps.cart.cart import Cart
from .services.index_service import get_category_list
from .services.catalog_service import get_product_list
from .services.search_service import get_search_list


class IndexView(ListView):
    """ Главная страница, вывод категорий """
    model = Category
    template_name = 'core/index.html'

    def get_queryset(self):
        return get_category_list()


class CatalogView(ListView):
    """ Вывод товаров из категории """
    model = Product
    paginate_by = 9
    template_name = 'core/catalog.html'

    def get_queryset(self):
        return get_product_list(self)


class ProductView(SuccessMessageMixin, FormMixin, DetailView):
    """ Детализация товара """
    model = Product
    template_name = 'core/product.html'
    form_class = ReviewForm
    success_message = 'Отзыв добавлен и ожидает модерации'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context

    def get_initial(self):
        return {
            'profile': self.request.user,
            'product': self.get_object()
        }

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('product', kwargs={'slug': self.get_object().slug})


def order_create(request):
    """ Страница оформления заказа """
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.profile = request.user
            instance.save()
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'cart/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'cart/create.html',
                  {'cart': cart, 'form': form})


class SearchView(ListView):
    """ Вывод товаров по совпадению слова в заголовке товара """
    paginate_by = 9
    template_name = 'core/catalog.html'

    def get_queryset(self):
        return get_search_list(self)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context


def about(request):
    """ Страница о компании """
    return render(request, 'core/about.html')


def contacts(request):
    """ Страница контактов """
    return render(request, 'core/contacts.html')


def page_not_found(request, exception):
    """ Страница 404 """
    return render(request, 'core/404-page.html', status=404)

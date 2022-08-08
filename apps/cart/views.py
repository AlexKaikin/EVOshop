from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from apps.core.models import Product, OrderItem

from .cart import Cart
from .forms import CartAddProductForm, OrderCreateForm
from .services.cart_detail_service import get_setting_delivery


@require_POST
def cart_add(request, product_id):
    """ Добавление товара в корзину """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])

    return redirect('cart_detail')


def cart_remove(request, product_id):
    """ Удаление товара из корзины """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)

    return redirect('cart_detail')


def cart_detail(request):
    """ Страница корзины """
    cart = Cart(request)
    setting_delivery = get_setting_delivery()
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    context = {'cart': cart, 'delivery': setting_delivery.delivery, 'delivery_free': setting_delivery.delivery_free}

    return render(request, 'cart/cart.html', context)


def order_create(request):
    """ Страница оформления заказа """
    cart = Cart(request)
    setting_delivery = get_setting_delivery()
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.profile = request.user
            if cart.get_products_price() < setting_delivery.delivery_free:
                instance.delivery = setting_delivery.delivery
            else:
                instance.delivery = 0
            instance.products_price = cart.get_products_price()
            instance.total_price = cart.get_total_price()
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
    context = {'cart': cart, 'form': form, 'delivery': setting_delivery.delivery,
               'delivery_free': setting_delivery.delivery_free}

    return render(request, 'cart/create.html', context)

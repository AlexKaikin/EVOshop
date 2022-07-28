from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from apps.core.models import Product, OrderItem, Setting

from .cart import Cart
from .forms import CartAddProductForm, OrderCreateForm
from .services.cart_detail import get_delivery, get_delivery_free


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
    delivery = get_delivery()
    delivery_free = get_delivery_free()
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/cart.html', {'cart': cart, 'delivery': delivery, 'delivery_free': delivery_free})


def order_create(request):
    """ Страница оформления заказа """
    cart = Cart(request)
    delivery = get_delivery()
    delivery_free = get_delivery_free()
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.profile = request.user
            if cart.get_products_price() < delivery_free:
                instance.delivery = delivery
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
    return render(request, 'cart/create.html',
                  {'cart': cart, 'form': form, 'delivery': delivery, 'delivery_free': delivery_free})

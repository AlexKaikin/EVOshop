from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from apps.core.models import Product, OrderItem

from .cart import Cart
from .forms import CartAddProductForm, OrderCreateForm


@require_POST
def cart_add(request, product_id):
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
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})


def order_create(request):
    """ Страница оформления заказа """
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        q = Product.objects.get()
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

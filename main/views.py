from django.shortcuts import render
from main.models import Product


def index(request):
    return render(request, 'index.html')


def tea(request):
    tea_all = {'prods': Product.objects.filter(category=1)}
    return render(request, 'catalog.html', tea_all)


def coffee(request):
    coffee_all = {'prods': Product.objects.filter(category=2)}
    return render(request, 'catalog.html', coffee_all)


def spices(request):
    spices_all = {'prods': Product.objects.filter(category=3)}
    return render(request, 'catalog.html', spices_all)


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')


def product(request, id):  # страница товара, получает id товара
    prod = Product.objects.get(id=id)  # находим товар по id
    prod_photos = prod.productimage_set.all()  # находим все фотографии
    prod_dic = {'prod': prod, 'prod_photos': prod_photos}
    return render(request, 'product.html', prod_dic)

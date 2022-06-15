from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def tea(request):
    return render(request, 'catalog.html')


def coffee(request):
    return render(request, 'catalog.html')


def spices(request):
    return render(request, 'catalog.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')

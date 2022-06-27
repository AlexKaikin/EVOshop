from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from main.models import Product, Category, Review
from django.views.generic import DetailView, CreateView
from .forms import ReviewForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    category_all = {'categories': Category.objects.all()}
    return render(request, 'index.html', category_all)


class RegisterForm(CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


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


# def product(request, id):  # страница товара, получает id товара
#     prod = Product.objects.get(id=id)  # находим товар по id
#     prod_photos = prod.productimage_set.all()  # находим все фотографии
#     prod_dic = {'prod': prod, 'prod_photos': prod_photos}
#     return render(request, 'product.html', prod_dic)
class ProductView(DetailView):
    model = Product
    template_name = 'product.html'


class AddReviewView(CreateView):
    model = Review
    template_name = 'product.html'
    form_class = ReviewForm

    def form_valid(self, form):
        form.instance.product_id = self.kwargs['pk']
        return super().form_valid(form)

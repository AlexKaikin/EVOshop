from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View

from .models import Product, Category, Review
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from .forms import ProductForm, ReviewForm, UserRegisterForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages


def index(request):
    context = {'categories': Category.objects.all()}
    return render(request, 'core/index.html', context)


class SuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)


class RegisterForm(CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')


class LoginForm(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'
    form_class = UserLoginForm
    success_msg = 'вы вошли'
    success_url = reverse_lazy('main')


class LogOutForm(LogoutView):
    template_name = 'accounts/logout.html'
    success_url = reverse_lazy('logout')


# def catalog(request, pk):
#     prod_cat = Category.objects.get(id=pk)
#     prod_all = Product.objects.filter(category=1)
#     context = {'prod_cat': prod_cat, 'prods': prod_all}
#     return render(request, 'core/catalog.html', context)


def tea(request):
    context = {'prods': Product.objects.filter(category=1)}
    return render(request, 'core/catalog.html', context)


def coffee(request):
    context = {'prods': Product.objects.filter(category=2)}
    return render(request, 'core/catalog.html', context)


def spices(request):
    context = {'prods': Product.objects.filter(category=3)}
    return render(request, 'core/catalog.html', context)


def about(request):
    return render(request, 'core/about.html')


def contacts(request):
    return render(request, 'core/contacts.html')


class ProductView(SuccessMessageMixin, FormMixin, DetailView):
    model = Product
    template_name = 'core/product.html'
    form_class = ReviewForm
    success_msg = 'Отзыв добавлен и ожидает модерации'

    def get_success_url(self, **kwargs):
        return reverse_lazy('product', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.product = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


# def product(request, pk):
#     prod = Product.objects.get(id=pk)
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#     context = {
#         'product': prod,
#         'form': ReviewForm()
#     }
#     return render(request, 'core/product.html', context)


class EditProductView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'core/edit_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('edit_product')
    success_msg = 'Товар обновлён'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse("edit_product", kwargs={'pk': pk})


class AddProductView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'core/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('add_product')
    success_msg = 'Товар добавлен'


# class DeleteProductView(LoginRequiredMixin, DeleteView):
#     model = Product
#     template_name = 'delete_product'
#     success_url = reverse_lazy('main')


def delete_product(request, pk):
    prod = Product.objects.get(id=pk)
    prod.delete()
    return redirect(reverse('main'))

# class AddReviewView(CreateView):
#     model = Review
#     template_name = 'core/product.html'
#     form_class = ReviewForm
#
#     def form_valid(self, form):
#         form.instance.product_id = self.kwargs['pk']
#         return super().form_valid(form)

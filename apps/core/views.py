from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Category, Product, Profile
from .forms import ProductForm, ReviewForm, UserRegisterForm, UserLoginForm
from apps.cart.forms import CartAddProductForm


class IndexView(ListView):
    model = Category
    template_name = 'core/index.html'

    def get_queryset(self):
        object_list = Category.objects.filter(is_active=True)
        return object_list


class CatalogView(ListView):
    model = Product
    template_name = 'core/catalog.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        object_list = Category.objects.get(slug=slug)
        object_list = object_list.products.filter(is_active=True)
        return object_list


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'core/product.html', {'product': product, 'cart_product_form': cart_product_form})


# class ProductView(SuccessMessageMixin, FormMixin, DetailView):
#     model = Product
#     template_name = 'core/product.html'
#     form_class = ReviewForm
#     success_message = 'Отзыв добавлен и ожидает модерации'
#
#     def get_success_url(self, **kwargs):
#         return reverse_lazy('product', kwargs={'slug': self.get_object().slug})
#
#     def post(self, request, *args, **kwargs):
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.product = self.get_object()
#         self.object.author = self.request.user
#         self.object.save()
#         return super().form_valid(form)


class EditProductView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'core/edit_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('edit_product')
    success_message = 'Товар обновлён'

    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse("edit_product", kwargs={'slug': slug})


class AddProductView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'core/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('add_product')
    success_message = 'Товар добавлен'


# class DeleteProductView(LoginRequiredMixin, DeleteView):
#     model = Product
#     template_name = 'delete_product'
#     success_url = reverse_lazy('main')


def delete_product(request, slug):
    product = Product.objects.get(slug=slug)
    product.delete()
    return redirect(reverse('main'))


class RegisterForm(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')
    success_message = 'Регистрация прошла успешно, можете войти'


class LoginForm(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'
    form_class = UserLoginForm
    success_message = '%(username)s, добро пожаловать!'
    success_url = reverse_lazy('main')


class LogOutForm(LogoutView):
    template_name = 'accounts/logout.html'
    success_url = reverse_lazy('logout')


class ProfileView(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'


def about(request):
    return render(request, 'core/about.html')


def contacts(request):
    return render(request, 'core/contacts.html')




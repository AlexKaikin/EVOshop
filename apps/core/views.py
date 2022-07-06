from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Category, Product, Profile, OrderItem
from .forms import ProductForm, ReviewForm, OrderCreateForm
from apps.cart.forms import CartAddProductForm
from apps.cart.cart import Cart


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


class ProductView(SuccessMessageMixin, FormMixin, DetailView):
    model = Product
    template_name = 'core/product.html'
    form_class = ReviewForm
    success_message = 'Отзыв добавлен и ожидает модерации'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('product', kwargs={'slug': self.get_object().slug})

    # def get_initial(self):
    #     return {
    #         'author': self.request.user,
    #         'product': self.get_object()
    #     }

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.product = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
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


class ProfileView(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'


def about(request):
    return render(request, 'core/about.html')


def contacts(request):
    return render(request, 'core/contacts.html')


def no_page(request):
    return render(request, 'core/404-page.html')

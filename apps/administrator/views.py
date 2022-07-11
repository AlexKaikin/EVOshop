from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, CreateView

from apps.core.forms import ProductForm
from apps.core.models import Product


class EditProductView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """ Обновление товара """
    model = Product
    template_name = 'administrator/edit_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('edit_product')
    success_message = 'Товар обновлён'

    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse("edit_product", kwargs={'slug': slug})


class AddProductView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """ Добавление товара """
    model = Product
    template_name = 'administrator/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('add_product')
    success_message = 'Товар добавлен'


# class DeleteProductView(LoginRequiredMixin, DeleteView):
#     model = Product
#     template_name = 'delete_product'
#     success_url = reverse_lazy('main')


def delete_product(request, slug):
    """ Удаление товара """
    product = Product.objects.get(slug=slug)
    product.delete()
    return redirect(reverse('main'))

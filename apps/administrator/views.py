from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, CreateView, ListView

from apps.core.models import Category, Product, Review, Order

from .forms import CategoryForm, ProductForm, ReviewForm, OrderForm
from .services.admin_product_view import get_product_list
from .services.admin_review_view import get_review_list
from .services.administrator_servece import get_count_review, get_count_order


def administrator(request):
    """ Панель администратора """
    count_review = get_count_review
    count_order = get_count_order
    context = {'count_review': count_review, 'count_order': count_order}
    return render(request, 'administrator/administrator.html', context)


class AdminCategoryView(ListView):
    """ Список категорий для панели администратора """
    model = Category
    paginate_by = 10
    template_name = 'administrator/admin_category.html'


class AddCategoryView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """ Добавление категории """
    model = Category
    template_name = 'administrator/add_category.html'
    form_class = CategoryForm
    success_url = reverse_lazy('admin_category')
    success_message = 'Категория добавлена'


class UpdateCategoryView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """ Обновление товара """
    model = Category
    template_name = 'administrator/update_category.html'
    form_class = CategoryForm
    success_url = reverse_lazy('update_category')
    success_message = 'Категория обновлена'

    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse("update_category", kwargs={'slug': slug})


def delete_category(request, slug):
    """ Удаление категории """
    category = Category.objects.get(slug=slug)
    category.delete()
    return redirect(reverse('admin_category'))


class AdminProductView(ListView):
    """ Список товаров для панели администратора """
    model = Product
    paginate_by = 10
    template_name = 'administrator/admin_product.html'

    def get_queryset(self):
        return get_product_list(self)


class AddProductView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """ Добавление товара """
    model = Product
    template_name = 'administrator/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('admin_product')
    success_message = 'Товар добавлен'


class UpdateProductView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """ Обновление товара """
    model = Product
    template_name = 'administrator/update_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('update_product')
    success_message = 'Товар обновлён'

    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse("update_product", kwargs={'slug': slug})


def delete_product(request, slug):
    """ Удаление товара """
    product = Product.objects.get(slug=slug)
    product.delete()
    return redirect(reverse('admin_product'))


class AdminReviewView(ListView):
    """ Список отзывов для панели администратора """
    model = Review
    paginate_by = 10
    template_name = 'administrator/admin_review.html'

    def get_queryset(self):
        return get_review_list(self)


class UpdateReviewView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """ Обновление отзыва """
    model = Review
    template_name = 'administrator/update_review.html'
    form_class = ReviewForm
    success_url = reverse_lazy('update_review')
    success_message = 'Отзыв обновлён'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse("update_review", kwargs={'pk': pk})


def delete_review(request, pk):
    """ Удаление отзыва """
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect(reverse('admin_review'))


class AdminOrderView(ListView):
    """ Список заказов для панели администратора """
    model = Order
    paginate_by = 10
    template_name = 'administrator/admin_order.html'


class UpdateOrderView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """ Обновление заказа """
    model = Order
    template_name = 'administrator/update_order.html'
    form_class = OrderForm
    success_url = reverse_lazy('update_order')
    success_message = 'Заказ обновлён'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse("update_order", kwargs={'pk': pk})


def delete_order(request, pk):
    """ Удаление отзыва """
    order = Order.objects.get(pk=pk)
    order.delete()
    return redirect(reverse('admin_order'))

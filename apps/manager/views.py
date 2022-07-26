from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from django.db.models.functions import TruncDay, TruncMonth
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, CreateView, ListView

from apps.core.models import Category, Product, Review, Order, OrderItem

from .forms import CategoryForm, ProductForm, ReviewForm, OrderForm
from .services.manager_category_view import get_category_list
from .services.manager_order_view import get_order_list
from .services.manager_product_view import get_product_list
from .services.manager_review_view import get_review_list
from .services.manager_servece import get_count_review, get_count_order


def manager(request):
    """ Панель управления """
    count_review = get_count_review
    count_order = get_count_order

    orders_day = (Order.objects.all()
                  .annotate(day=TruncDay('created'))
                  .values('day')
                  .annotate(count_order=Count('created'))
                  .values('day', 'count_order')
                  .order_by('day')
                  )

    orders_month = (Order.objects.all()
                    .annotate(month=TruncMonth('created'))
                    .values('month')
                    .annotate(count_order=Count('created'))
                    .values('month', 'count_order')
                    .order_by('month')
                    )

    context = {'count_review': count_review, 'count_order': count_order, 'orders_day': orders_day,
               'orders_month': orders_month}
    return render(request, 'manager/manager.html', context)


class ManagerCategoryView(ListView):
    """ Список категорий для панели управления """
    model = Category
    template_name = 'manager/category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = get_category_list()
        paginator = Paginator(context['object_list'], 10)
        page = self.request.GET.get('page')
        try:
            context['object_list'] = paginator.page(page)
        except PageNotAnInteger:
            context['object_list'] = paginator.page(1)
        except EmptyPage:
            context['object_list'] = paginator.page(paginator.num_pages)
        return context


class AddCategoryView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """ Добавление категории """
    model = Category
    template_name = 'manager/add_category.html'
    form_class = CategoryForm
    success_url = reverse_lazy('manager_category')
    success_message = 'Категория добавлена'


class UpdateCategoryView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """ Обновление товара """
    model = Category
    template_name = 'manager/update_category.html'
    form_class = CategoryForm
    success_url = reverse_lazy('manager_category')
    success_message = 'Категория обновлена'


def delete_category(request, slug):
    """ Удаление категории """
    category = Category.objects.get(slug=slug)
    category.delete()
    return redirect(reverse('manager_category'))


class ManagerProductView(ListView):
    """ Список товаров для панели управления """
    model = Product
    template_name = 'manager/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = get_product_list(self)
        paginator = Paginator(context['object_list'], 10)
        page = self.request.GET.get('page')
        try:
            context['object_list'] = paginator.page(page)
        except PageNotAnInteger:
            context['object_list'] = paginator.page(1)
        except EmptyPage:
            context['object_list'] = paginator.page(paginator.num_pages)
        return context


class AddProductView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """ Добавление товара """
    model = Product
    template_name = 'manager/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('manager_product')
    success_message = 'Товар добавлен'


class UpdateProductView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """ Обновление товара """
    model = Product
    template_name = 'manager/update_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('manager_product')
    success_message = 'Товар обновлён'


def delete_product(request, slug):
    """ Удаление товара """
    product = Product.objects.get(slug=slug)
    product.delete()
    return redirect(reverse('manager_product'))


class ManagerReviewView(ListView):
    """ Список отзывов для панели управления """
    model = Review
    template_name = 'manager/review.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = get_review_list(self)
        paginator = Paginator(context['object_list'], 10)
        page = self.request.GET.get('page')
        try:
            context['object_list'] = paginator.page(page)
        except PageNotAnInteger:
            context['object_list'] = paginator.page(1)
        except EmptyPage:
            context['object_list'] = paginator.page(paginator.num_pages)
        return context


class UpdateReviewView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """ Обновление отзыва """
    model = Review
    template_name = 'manager/update_review.html'
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
    return redirect(reverse('manager_review'))


class ManagerOrderView(ListView):
    """ Список заказов для панели управления """
    model = Order
    template_name = 'manager/order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = get_order_list()
        paginator = Paginator(context['object_list'], 10)
        page = self.request.GET.get('page')
        try:
            context['object_list'] = paginator.page(page)
        except PageNotAnInteger:
            context['object_list'] = paginator.page(1)
        except EmptyPage:
            context['object_list'] = paginator.page(paginator.num_pages)
        return context


class UpdateOrderView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """ Обновление заказа """
    model = Order
    template_name = 'manager/update_order.html'
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
    return redirect(reverse('manager_order'))

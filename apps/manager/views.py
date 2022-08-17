from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, CreateView, ListView

from apps.core.models import Category, Product, Review, Order, Setting
from apps.core.utils import ajax_paginator

from .forms import CategoryForm, ProductForm, ReviewForm, OrderForm, SettingForm, ProductFormSet
from .services.manager_category_view_service import get_category_list
from .services.manager_order_view_service import get_order_list
from .services.manager_product_view_service import get_product_list
from .services.manager_review_view_service import get_review_list
from .services.manager_servece import get_count_review, get_count_order, get_orders_day, get_orders_month, \
    get_profit_day, get_profit_month


def manager(request):
    """ Дашборд панели управления """
    count_review = get_count_review
    count_order = get_count_order
    orders_day = get_orders_day
    orders_month = get_orders_month
    profit_day = get_profit_day
    profit_month = get_profit_month

    context = {'count_review': count_review, 'count_order': count_order, 'orders_day': orders_day,
               'orders_month': orders_month, 'profit_day': profit_day, 'profit_month': profit_month,
               'page_manager': True}
    return render(request, 'manager/manager.html', context)


class ManagerCategoryView(ListView):
    """ Список категорий для панели управления """
    model = Category
    template_name = 'manager/category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = get_category_list()
        context['page_manager_category'] = True
        ajax_paginator(self, context)
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
        context['page_manager_product'] = True
        ajax_paginator(self, context)
        return context


class AddProductView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """ Добавление товара """
    model = Product
    template_name = 'manager/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('manager_product')
    success_message = 'Товар добавлен'

    def form_valid(self, form):
        context = self.get_context_data()
        product_form = context['product_form']
        if product_form.is_valid():
            self.object = form.save()
            product_form.instance = self.object
            product_form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(AddProductView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['product_form'] = ProductFormSet(self.request.POST, self.request.FILES)
        else:
            context['product_form'] = ProductFormSet()

        return context


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
        context['page_manager_review'] = True
        ajax_paginator(self, context)
        return context


class UpdateReviewView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """ Обновление отзыва """
    model = Review
    template_name = 'manager/update_review.html'
    form_class = ReviewForm
    success_url = reverse_lazy('update_review')
    success_message = 'Отзыв обновлён'

    def form_valid(self, form):
        form.save()
        response = {'status': 'ok'}
        return JsonResponse(response, status=200)


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
        context['page_manager_order'] = True
        ajax_paginator(self, context)
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


class ManagerSettingView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """ Настройки магазина """
    model = Setting
    template_name = 'manager/setting.html'
    form_class = SettingForm
    success_url = reverse_lazy('manager_setting')
    success_message = 'Настройки обновлены'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse("manager_setting", kwargs={'pk': pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_manager_setting'] = True
        return context

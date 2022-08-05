from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, CreateView
from django.contrib.messages.views import SuccessMessageMixin

from apps.core.models import Category, Product, Tag
from apps.cart.forms import CartAddProductForm

from .forms import ReviewForm, ContactForm
from .services.index_service import get_category_list, get_popular_list
from .services.category_service import get_product_list
from .services.product_service import get_product, get_review_list, get_images_list, get_reply_list
from .services.search_service import get_search_list


class Filter:
    """ Фильтр товаров """

    def get_category(self):
        return Category.objects.filter(published='yes')

    def get_tag(self):
        return Tag.objects.filter()


class IndexView(Filter, ListView):
    """ Главная страница, вывод категорий """
    model = Category
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['popular'] = get_popular_list()
        return context

    def get_queryset(self):
        return get_category_list()


class CategoryView(ListView):
    """ Вывод товаров из категории """
    model = Product
    template_name = 'core/category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = get_product_list(self)
        paginator = Paginator(context['object_list'], 9)
        page = self.request.GET.get('page')
        try:
            context['object_list'] = paginator.page(page)
        except PageNotAnInteger:
            context['object_list'] = paginator.page(1)
        except EmptyPage:
            context['object_list'] = paginator.page(paginator.num_pages)

        context['cart_product_form'] = CartAddProductForm()
        return context


class ProductView(FormMixin, DetailView):
    """ Детализация товара """
    model = Product
    template_name = 'core/product.html'
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        context['images'] = get_images_list(self)
        context['reply_list'] = get_reply_list(self)
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

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.profile = request.user
            form.product = self.get_object()
            form.save()
            return JsonResponse({'status': 'ok'}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    def get_queryset(self):
        return get_product(self)


class SearchView(ListView):
    """ Вывод товаров по совпадению слова в заголовке товара """
    template_name = 'core/category.html'

    def get_queryset(self):
        return get_search_list(self)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = ''.join([f"q={x}&" for x in self.request.GET.get("q")])
        context['object_list'] = self.get_queryset()
        paginator = Paginator(context['object_list'], 9)
        page = self.request.GET.get('page')
        try:
            context['object_list'] = paginator.page(page)
        except PageNotAnInteger:
            context['object_list'] = paginator.page(1)
        except EmptyPage:
            context['object_list'] = paginator.page(paginator.num_pages)

        context['cart_product_form'] = CartAddProductForm()
        return context


class ContactView(SuccessMessageMixin, CreateView):
    """ Страница Контакты """
    form_class = ContactForm
    template_name = 'core/contacts.html'
    success_url = reverse_lazy('contacts')
    success_message = 'Сообщение отправлено'

    def form_valid(self, form):
        """ Если форма валидна, вернем код 200 """
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        form.save()
        return JsonResponse({"name": name, "email": email, "message": message, 'messages': 'Сообщение отправлено'},
                            status=200)

    def form_invalid(self, form):
        """ Если форма невалидна, возвращаем код 400 с ошибками. """
        errors = form.errors.as_json()
        return JsonResponse({"errors": errors}, status=400)


class FilterProductView(Filter, ListView):
    """ Фильтр товаров """
    template_name = 'core/category.html'

    def get_queryset(self):
        queryset = Product.objects.filter(
            Q(category__name__in=self.request.GET.getlist("category")) |
            Q(tag__name__in=self.request.GET.getlist("tag")), published='yes'
        ).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["category"] = ''.join([f"category={x}&" for x in self.request.GET.getlist("category")])
        context["tag"] = ''.join([f"tag={x}&" for x in self.request.GET.getlist("tag")])
        context['object_list'] = self.get_queryset()
        paginator = Paginator(context['object_list'], 9)
        page = self.request.GET.get('page')
        try:
            context['object_list'] = paginator.page(page)
        except PageNotAnInteger:
            context['object_list'] = paginator.page(1)
        except EmptyPage:
            context['object_list'] = paginator.page(paginator.num_pages)

        context['cart_product_form'] = CartAddProductForm()
        return context


def about(request):
    """ Страница о компании """
    return render(request, 'core/about.html')


def page_not_found(request, exception):
    """ Страница 404 """
    return render(request, 'core/404-page.html', status=404)

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, CreateView
from django.contrib.messages.views import SuccessMessageMixin

from apps.core.models import Category, Product
from apps.cart.forms import CartAddProductForm

from .forms import ReviewForm, ContactForm
from .services.index_service import get_category_list, get_popular_list
from .services.category_service import get_product_list
from .services.product_service import get_product, get_review_list, get_images_list
from .services.search_service import get_search_list


class IndexView(ListView):
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


class ProductView(SuccessMessageMixin, FormMixin, DetailView):
    """ Детализация товара """
    model = Product
    template_name = 'core/product.html'
    form_class = ReviewForm
    context_object_name = 'product'
    success_message = 'Отзыв добавлен и ожидает модерации'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        context['images'] = get_images_list(self)
        context['object_list'] = get_review_list(self)  # отзывы
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
            instance = form.save(commit=False)
            instance.profile = request.user
            instance.product = self.get_object()
            instance.save()
            form.save()
            return JsonResponse({'status': 'ok'}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    def get_queryset(self):
        return get_product(self)

    def get_success_url(self, **kwargs):
        return reverse_lazy('product', kwargs={'slug': self.get_object().slug})


class SearchView(ListView):
    """ Вывод товаров по совпадению слова в заголовке товара """
    paginate_by = 9
    template_name = 'core/category.html'

    def get_queryset(self):
        return get_search_list(self)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
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


def about(request):
    """ Страница о компании """
    return render(request, 'core/about.html')


def page_not_found(request, exception):
    """ Страница 404 """
    return render(request, 'core/404-page.html', status=404)

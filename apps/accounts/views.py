from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse

from apps.core.models import Order, Review

from .forms import UserRegisterForm, UserLoginForm, ProfileForm
from .models import Profile
from .services.profile_order_detail_view import get_delivery_free, get_order, get_product_list
from .services.profile_order_view import get_order_list
from .services.profile_review_view import get_review_list


class RegisterForm(SuccessMessageMixin, CreateView):
    """ Страница регистрации """
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')
    success_message = '%(username)s, добро пожаловать!'

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


def validate_username(request):
    """ Проверка доступности логина """
    username = request.GET.get('username', None)
    response = {
        'username_taken': Profile.objects.filter(username__iexact=username).exists(),
    }
    return JsonResponse(response)


def validate_email(request):
    """ Проверка доступности e-mail """
    email = request.GET.get('email', None)
    response = {
        'email_taken': Profile.objects.filter(email__iexact=email).exists(),
    }
    return JsonResponse(response)


class LoginForm(SuccessMessageMixin, LoginView):
    """ Страница авторизации """
    template_name = 'accounts/login.html'
    form_class = UserLoginForm
    success_message = '%(username)s, добро пожаловать!'
    success_url = reverse_lazy('index')


class LogOutForm(LogoutView):
    """ Выход  """
    template_name = 'accounts/logout.html'
    success_url = reverse_lazy('logout')


class ProfileView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """ Страница профиль пользователя """
    model = Profile
    template_name = 'accounts/profile/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    success_message = 'Профиль обновлён'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse("profile", kwargs={'pk': pk})


class ProfileOrderView(ListView):
    """ Страница заказов пользователя """
    model = Order
    template_name = 'accounts/profile/order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = get_order_list(self)
        paginator = Paginator(context['object_list'], 10)
        page = self.request.GET.get('page')
        try:
            context['object_list'] = paginator.page(page)
        except PageNotAnInteger:
            context['object_list'] = paginator.page(1)
        except EmptyPage:
            context['object_list'] = paginator.page(paginator.num_pages)
        return context


class ProfileOrderDetailView(DetailView):
    """ Детализация заказа """
    model = Order
    template_name = 'accounts/profile/order_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = get_product_list(self)
        context['delivery_free'] = get_delivery_free()
        return context


class ProfileReviewView(ListView):
    """ Страница отзывов пользователя """
    model = Review
    template_name = 'accounts/profile/review.html'

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

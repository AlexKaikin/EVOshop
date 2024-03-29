from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse

from apps.core.models import Order, Review
from apps.core.utils import ajax_paginator

from .forms import UserRegisterForm, UserLoginForm, ProfileForm
from .models import Profile
from .services.profile_order_detail_view_service import get_delivery_free, get_product_list
from .services.profile_order_view_service import get_order_list
from .services.profile_review_view_service import get_review_list


class RegisterForm(SuccessMessageMixin, CreateView):
    """ Страница регистрации """
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')
    success_message = '%(username)s, добро пожаловать!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_profile'] = True
        return context

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


class LoginForm(SuccessMessageMixin, LoginView):
    """ Страница авторизации """
    template_name = 'accounts/login.html'
    form_class = UserLoginForm
    success_message = '%(username)s, добро пожаловать!'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_profile'] = True
        return context


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_profile'] = True
        return context

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse("profile", kwargs={'pk': pk})

    def form_valid(self, form):
        form.save()
        response = {'status': 'ok'}
        return JsonResponse(response, status=200)

    def form_invalid(self, form):
        response = {'status': 'error'}
        return JsonResponse(response, status=400)


class ProfileOrderView(ListView):
    """ Страница заказов пользователя """
    model = Order
    template_name = 'accounts/profile/order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = get_order_list(self)
        ajax_paginator(self, context)
        context['page_profile_order'] = True
        return context


class ProfileOrderDetailView(DetailView):
    """ Детализация заказа """
    model = Order
    template_name = 'accounts/profile/order_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = get_product_list(self)
        context['delivery_free'] = get_delivery_free()
        context['page_profile_order'] = True
        return context


class ProfileReviewView(ListView):
    """ Страница отзывов пользователя """
    model = Review
    template_name = 'accounts/profile/review.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = get_review_list(self)
        ajax_paginator(self, context)
        context['page_profile_review'] = True
        return context

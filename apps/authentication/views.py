from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView


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

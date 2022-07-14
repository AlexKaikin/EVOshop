from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from .forms import UserRegisterForm, UserLoginForm, ProfileForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, UpdateView


class RegisterForm(SuccessMessageMixin, CreateView):
    """ Страница регистрации """
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')
    success_message = 'Регистрация прошла успешно, можете войти'


class LoginForm(SuccessMessageMixin, LoginView):
    """ Страница авторизации """
    template_name = 'accounts/login.html'
    form_class = UserLoginForm
    success_message = '%(username)s, добро пожаловать!'
    success_url = reverse_lazy('main')


class LogOutForm(LogoutView):
    """ Выход  """
    template_name = 'accounts/logout.html'
    success_url = reverse_lazy('logout')


class ProfileView(DetailView):
    """ Страница профиль пользователя """
    model = Profile
    template_name = 'accounts/profile.html'


class UpdateProfileView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """ Обновление профиля """
    model = Profile
    template_name = 'accounts/update_profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('update_product')
    success_message = 'Профиль обновлён'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse("update_profile", kwargs={'pk': pk})

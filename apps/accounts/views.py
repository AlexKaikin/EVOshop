from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse

from .forms import UserRegisterForm, UserLoginForm, ProfileForm
from .models import Profile

from apps.core.models import Order, Review
from .services.profile_order_view import get_order_list
from .services.profile_review_view import get_review_list


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
    paginate_by = 10
    template_name = 'accounts/profile/order.html'

    def get_queryset(self):
        return get_order_list(self)


class ProfileReviewView(ListView):
    """ Страница отзывов пользователя """
    model = Review
    paginate_by = 10
    template_name = 'accounts/profile/review.html'

    def get_queryset(self):
        return get_review_list(self)

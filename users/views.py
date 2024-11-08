from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
import logging
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from .models import UserProfile
# from orders.models import Order
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = "users/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["orders"] = Order.objects.filter(
        #     user=self.request.user)  # аолучаем заказы
        # logger.debug(
        #     f"Загружены заказы для пользователя {self.request.user.username}")
        return context


class RegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users:profile")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()

        UserProfile.objects.create(user=user)

        login(self.request, user)
        logger.info(f"Новый пользователь зарегистрирован: {user.username}")
        return super().form_valid(form)

    def form_invalid(self, form):
        logger.warning(f"Неудачная попытка регистрации. Ошибки: {form.errors}")
        return super().form_invalid(form)


class UserLoginView(LoginView):
    template_name = "users/login.html"
    authentication_form = UserLoginForm

    def form_valid(self, form):
        logger.info(
            f"Пользователь {form.get_user().username} вошел в систему.")
        return super().form_valid(form)

    def form_invalid(self, form):
        logger.warning(f"Неудачная попытка входа. Данные: {form.cleaned_data}")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("users:profile")


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("users:login")

    def dispatch(self, request, *args, **kwargs):
        logger.info(f"Пользователь {request.user.username} вышел из системы.")
        return super().dispatch(request, *args, **kwargs)


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/password_change.html"
    success_url = reverse_lazy("users:profile")

    def form_valid(self, form):
        logger.info(
            f"Пользователь {self.request.user.username} изменил пароль.")
        return super().form_valid(form)

    def form_invalid(self, form):
        logger.warning(
            f"Неудачная попытка смены пароля пользователем {self.request.user.username}. Ошибки: {form.errors}")
        return super().form_invalid(form)


def profile_admin(request):
    return render(request, 'admin/users/profile.html')


@login_required
def dashboard(request):
    logger.debug("Доступ к личному кабинету.")
    return render(request, 'users/dashboard.html')


@login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if 'remove_avatar' in request.POST and request.POST['remove_avatar'] == '1':
            user_profile.avatar.delete(save=False)  #удалить файл автавра
            user_profile.avatar = None  #обнуляю
        elif form.is_valid():
            user = request.user
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email')
            user.save()  
            form.save()
            logger.info(f"Пользователь {request.user.username} обновил профиль.")
            return redirect('users:profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'users/edit_profile.html', {'form': form})


@login_required
def clear_avatar(request):
    if request.method == 'POST':
        user_profile = request.user.userprofile
        user_profile.avatar.delete()  #удалила файл с сервера
        user_profile.avatar = None  #сбросила
        user_profile.save()
        return redirect('users:profile')  

    return redirect('users:profile')  # если не post то просто переходим на профиль

class HomePageView(TemplateView):
    template_name = "home.html"
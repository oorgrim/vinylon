from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
# from captcha.fields import CaptchaField

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label=_('Пароль'), widget=forms.PasswordInput)
    password_confirm = forms.CharField(label=_('Подтвердите пароль'), widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        labels = {
            'username': _('Имя пользователя'),
            'first_name': _('Имя'),
            'last_name': _('Фамилия'),
            'email': _('Электронная почта'),
        }

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError(_('Пароли не совпадают'))
        return password_confirm

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label=_('Имя пользователя'))
    password = forms.CharField(label=_('Пароль'), widget=forms.PasswordInput)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # fields = ['nickname', 'image']
        # labels = {
        #     'nickname': _('Никнейм'),
        #     'image': _('Фото профиля'),
        # }
        fields = ['first_name', 'last_name', 'phone', 'email', 'avatar']
        widgets = {
            'first_name': forms.TextInput(attrs={'required': 'true'}),
            'last_name': forms.TextInput(attrs={'required': 'true'}),
            'email': forms.EmailInput(attrs={'required': 'true'}),
            'phone': forms.TextInput(attrs={'required': 'true'}),
        }


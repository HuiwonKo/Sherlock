from django import forms
from django.core.validators import EmailValidator
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Profile, GENDER_CHOICES

class SignupForm(UserCreationForm):
    login_id = forms.CharField(label='아이디')
    login_password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    name = forms.CharField(label='이름')
    nickname = forms.CharField(label='닉네임')
    gender = forms.ChoiceField(label='성별', choices=GENDER_CHOICES)


    def save(self):
        user = super().save()
        phone = self.cleaned_data['phone']
        address = self.cleaned_data['address']
        Profile.objects.create(user=user, phone=phone, address=address)
        return user


class LoginForm(AuthenticationForm):
    login_id = forms.CharField(label='아이디')
    login_password = forms.CharField(label='비밀번호', widget=forms.PasswordInput())

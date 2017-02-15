from django import forms
from django.core.validators import EmailValidator
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Profile, GENDER_CHOICES
'''
    login_id = forms.CharField(required=True, label='아이디', help_text="*필수*")
    login_password = forms.CharField(required=True, label='비밀번호', widget=forms.PasswordInput(attrs={'class':'form-control',}), help_text="*필수*"
        )
    name = forms.CharField(label='이름')
'''
class SignupForm(UserCreationForm):

    nickname = forms.CharField(required=False, label='Nickname')
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES)
    phone = forms.IntegerField(required=False, label='Phone number')

'''
    def save(self):
        user = super().save()
        phone = self.cleaned_data['phone']
        Profile.objects.create(user=user, phone=phone,)
        return user
'''

class LoginForm(AuthenticationForm):
    login_id = forms.CharField(label='아이디')
    login_password = forms.CharField(label='비밀번호', widget=forms.PasswordInput())

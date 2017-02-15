from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from .forms import SignupForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Profile
from cafe.models import Room, Review, Like
from django.contrib.auth.models import User
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == "POST":
        userform = SignupForm(request.POST) #사용자가 입력한 값은 사전객체형태로 request.POST 안에 있다!
        if userform.is_valid():
            userform.save()
            return HttpResponseRedirect(
                reverse("cafe:index")
            )
    elif request.method == "GET": #겟방식의 경우 사용자 입력값이 없기때문에 아무것도 입력하지 않은 객체를 만들어준다.
        userform = SignupForm()
    return render(request, 'accounts/signup.html', {'userform':userform,},
     )


def profile(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    return render(request, 'accounts/profile.html',
        {'user':user,
    })

def passprofile(request):
    return  HttpResponseRedirect(
                reverse("cafe:index")
            )
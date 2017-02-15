from django.views.generic import TemplateView
from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views
from accounts.forms import LoginForm
urlpatterns = [
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^signup_ok/$', TemplateView.as_view(template_name = 'accounts/signup_ok.html'), name='signup_ok'),
    url(r'^login/$', login, name='login', kwargs={'template_name': 'accounts/login.html',}
        ),
    url(r'^logout/$', logout, {'next_page':'/login/',}, name='logout'),
    url(r'^profile/(?P<user_pk>\d+)/$', views.profile, name='profile'),
]
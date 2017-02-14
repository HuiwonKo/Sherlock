from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<pk>\d+)/$', views.room_detail, name='room_detail'),
    url(r'^(?P<room_pk>\d+)/comments/new$', views.review_new, name='review_new'),
    url(r'^(?P<room_pk>\d+)/comments/(?P<review_pk>\d+)/edit$', views.review_edit, name='review_edit'),
    url(r'^(?P<room_pk>\d+)/comments/(?P<review_pk>\d+)/delete$', views.review_delete, name='review_delete'),
]

from django.db import models
from .choices import *
from django.core.urlresolvers import reverse
from django.conf import settings
# Create your models here.

class Cafe(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성 일시")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="업데이트 일시")
    name = models.CharField(max_length=20, verbose_name="카페 이름")
    lnglat = models.CharField(max_length=50, verbose_name="카페 위치")
    station = models.IntegerField(choices=STATION_CHOICES, default=0, verbose_name="카페 주변 지하철역")
    url = models.CharField(max_length=50, verbose_name="카페 url")
    phone = models.CharField(max_length=30, verbose_name="카페 번호")
    address = models.CharField(max_length=50, verbose_name="카페 주소")

    def __str__(self):
        return self.name


class Room(models.Model):
    cafe = models.ForeignKey(Cafe, related_name="cafe_room_set") # cafe : room = 1 : N
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성 일시")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="업데이트 일시")
    name = models.CharField(max_length=20, verbose_name="방 이름")
    number = models.IntegerField(default=1, verbose_name="방 번호")
    level = models.IntegerField(choices=LEVEL_CHOICES, default=0, verbose_name="방 레벨")
    image = models.ImageField(blank=True, null=True, verbose_name="방 이미지")
    story = models.TextField(blank = True, verbose_name="방 설명")
    click = models.IntegerField(default=0, verbose_name="방 조회수")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cafe:room_detail', args=[self.pk])

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="review_user")
    room = models.ForeignKey(Room, related_name="cafe_review_set")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성 일시")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="업데이트 일시")
    content = models.CharField(max_length=150, verbose_name="댓글 내용")

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-id']


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="like_user_set")
    room = models.ForeignKey(Room, related_name="room_like_set")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-id']


"""
class Post_authentication(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성 일시")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="업데이트 일시")
    cafe = models.CharField(verbose_name='카페 이름')
    room = models.CharField(verbose_name='방 이름')
    image = models.ImageField(blank=True, null=True, verbose_name="인증 사진")
    time = models.TimeField(verbose_name="탈출 시간")
"""
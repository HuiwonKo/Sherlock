from django.db import models
from .choices import *

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
    score_star = models.IntegerField(default=0, verbose_name="방 별점")
    #score_hard = models.IntegerField(default=0, verbose_name="방 난이도 점수")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성 일시")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="업데이트 일시")
    name = models.CharField(max_length=20, verbose_name="방 이름")
    number = models.IntegerField(default=1, verbose_name="방 번호")
    level = models.IntegerField(choices=LEVEL_CHOICES, default=0, verbose_name="방 레벨")
    #theme = models.CharField(max_length=50, verbose_name="방 테마")
    image = models.ImageField(blank=True, null=True, verbose_name="방 이미지")
    story = models.TextField(blank = True, verbose_name="방 설명")

    def __str__(self):
        return self.name

class Review(models.Model):
    room = models.ForeignKey(Room, related_name="cafe_review_set")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성 일시")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="업데이트 일시")
    score_hard = models.IntegerField(default=0, null=True, verbose_name="방 난이도 점수")
    score_star = models.IntegerField(default=0, null=True, verbose_name="방 별점")
    author = models.CharField(max_length=20, verbose_name="댓글 작성자")
    content = models.CharField(max_length=150, verbose_name="댓글 내용")

    def __str__(self):
        return self.author


"""
class Post_authentication(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성 일시")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="업데이트 일시")
    cafe = models.CharField(verbose_name='카페 이름')
    room = models.CharField(verbose_name='방 이름')
    image = models.ImageField(blank=True, null=True, verbose_name="인증 사진")
    time = models.TimeField(verbose_name="탈출 시간")
"""
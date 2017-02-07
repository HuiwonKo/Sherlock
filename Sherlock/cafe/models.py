from django.db import models

# Create your models here.

class Cafe(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성 일시")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="업데이트 일시")
    name = models.CharField(max_length=20, verbose_name="카페 이름")
    lnglat = models.CharField(max_length=50, verbose_name="카페 위치")
    image = models.ImageField(blank=True, null=True, verbose_name="카페 이미지")
    url = models.CharField(max_length=50, verbose_name="카페 url 주소")
    price = models.IntegerField(default=0, verbose_name="카페 가격")


class Room(models.Model):
    cafe = models.ForeignKey(Cafe, related_name="cafe_room_set") # cafe : room = 1 : N
    score_star = models.IntegerField(default=0, verbose_name="방 별점")
    score_hard = models.IntegerField(default=0, verbose_name="방 난이도 점수")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성 일시")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="업데이트 일시")
    name = models.CharField(max_length=20, verbose_name="방 이름")
    number = models.IntegerField(default=1, verbose_name="방 번호")
    level = models.IntegerField(default=1, verbose_name="방 레벨")
    theme = models.CharField(max_length=50, verbose_name="방 테마")
    min_time = models.TimeField(verbose_name="방 탈출 최소 시간")


class Hard(models.Model):
    room = models.ForeignKey(Room, related_name="room_hard_set")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성 일시")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="업데이트 일시")
    score = models.IntegerField(default=0, null=True, verbose_name="방 난이도 점수")


class Star(models.Model):
    room = models.ForeignKey(Room, related_name="room_star_set")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성 일시")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="업데이트 일시")
    score = models.IntegerField(default=0, null=True, verbose_name="방 별점")

class Comment(models.Model):
    cafe = models.ForeignKey(Cafe, related_name="cafe_comment_set") # cafe : comment = 1 : N
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성 일시")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="업데이트 일시")
    author = models.CharField(max_length=20, verbose_name="댓글 작성자")
    content = models.CharField(max_length=150, verbose_name="댓글 내용")


"""
class Post_authentication(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성 일시")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="업데이트 일시")
    cafe = models.CharField(verbose_name='카페 이름')
    room = models.CharField(verbose_name='방 이름')
    image = models.ImageField(blank=True, null=True, verbose_name="인증 사진")
    time = models.TimeField(verbose_name="탈출 시간")
"""
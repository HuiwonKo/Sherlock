from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile")
    #group = models.ForeignKey(Group, related_name='Profile_Group_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    login_id = models.CharField(max_length=20, verbose_name='아이디')
    login_pw = models.CharField(max_length=20, verbose_name='비밀번호')
    name = models.CharField(max_length=20, verbose_name='이름')
    gender = models.BooleanField(default=True)
    nickname = models.CharField(max_length=20, verbose_name='닉네임')
    #level = models.CharField(max_length=20, verbose_name='레벨')
    #score = models.IntegerField(default=0, verbose_name='점수')


GENDER_CHOICES = (
    ('남','남'),
    ('여','여'),
)

"""
class Group(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=20, verbose_name='만든 사람')
    name = models.CharField(max_length=20, verbose_name='그룹 이름')
    level = models.CharField(max_length=20, verbose_name='레벨')
    score = models.IntegerField(default=0, verbose_name='점수')
"""

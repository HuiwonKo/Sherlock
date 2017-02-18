# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 11:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cafe', '0003_auto_20170207_0825'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-id']},
        ),
        migrations.RemoveField(
            model_name='cafe',
            name='image',
        ),
        migrations.RemoveField(
            model_name='cafe',
            name='price',
        ),
        migrations.RemoveField(
            model_name='review',
            name='author',
        ),
        migrations.RemoveField(
            model_name='room',
            name='min_time',
        ),
        migrations.RemoveField(
            model_name='room',
            name='score_hard',
        ),
        migrations.RemoveField(
            model_name='room',
            name='theme',
        ),
        migrations.AddField(
            model_name='cafe',
            name='address',
            field=models.CharField(default=1, max_length=50, verbose_name='카페 주소'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cafe',
            name='phone',
            field=models.CharField(default=1, max_length=30, verbose_name='카페 번호'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cafe',
            name='station',
            field=models.IntegerField(choices=[(0, '-------'), (1, '강남역'), (2, '건대입구역'), (3, '구로디지털단지역'), (4, '노원역'), (5, '명동역'), (6, '목동역'), (7, '상수역'), (8, '성신여대입구역'), (9, '신논현역'), (10, '신림역'), (11, '신사역'), (12, '신촌역'), (13, '압구정로데오역'), (14, '어린이대공원역'), (15, '영등포역'), (16, '이태원역'), (17, '잠실새내역'), (18, '종각역'), (19, '합정역'), (20, '혜화역'), (21, '홍대입구역')], default=0, verbose_name='카페 주변 지하철역'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='review_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='story',
            field=models.TextField(blank=True, verbose_name='방 설명'),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='url',
            field=models.CharField(max_length=50, verbose_name='카페 url'),
        ),
        migrations.AlterField(
            model_name='review',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cafe_review_set', to='cafe.Room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='level',
            field=models.IntegerField(choices=[(0, '-------'), (1, '10%미만'), (2, '10%~20%'), (3, '20%~30%'), (4, '30%~40%'), (5, '40%~50%'), (6, '50%이상')], default=0, verbose_name='방 레벨'),
        ),
    ]
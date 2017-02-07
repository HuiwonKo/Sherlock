# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 06:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='업데이트 일시')),
                ('name', models.CharField(max_length=20, verbose_name='카페 이름')),
                ('lnglat', models.CharField(max_length=50, verbose_name='카페 위치')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='카페 이미지')),
                ('url', models.CharField(max_length=50, verbose_name='카페 url 주소')),
                ('price', models.IntegerField(default=0, verbose_name='카페 가격')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='업데이트 일시')),
                ('author', models.CharField(max_length=20, verbose_name='댓글 작성자')),
                ('content', models.CharField(max_length=150, verbose_name='댓글 내용')),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cafe_comment_set', to='cafe.Cafe')),
            ],
        ),
        migrations.CreateModel(
            name='Hard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='업데이트 일시')),
                ('score', models.IntegerField(default=0, null=True, verbose_name='방 난이도 점수')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_star', models.IntegerField(default=0, verbose_name='방 별점')),
                ('score_hard', models.IntegerField(default=0, verbose_name='방 난이도 점수')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='업데이트 일시')),
                ('name', models.CharField(max_length=20, verbose_name='방 이름')),
                ('number', models.IntegerField(default=1, verbose_name='방 번호')),
                ('level', models.IntegerField(default=1, verbose_name='방 레벨')),
                ('theme', models.CharField(max_length=50, verbose_name='방 테마')),
                ('min_time', models.TimeField(verbose_name='방 탈출 최소 시간')),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cafe_room_set', to='cafe.Cafe')),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='업데이트 일시')),
                ('score', models.IntegerField(default=0, null=True, verbose_name='방 별점')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_star_set', to='cafe.Room')),
            ],
        ),
        migrations.AddField(
            model_name='hard',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_hard_set', to='cafe.Room'),
        ),
    ]
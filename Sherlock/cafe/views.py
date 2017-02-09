from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Cafe, Room, Review
from .forms import ReviewForm


def index(request):
    return render(request, "cafe/index.html")

# room_list filter 부분 디버깅 필요
def room_list(request, pk, room_cafe_station, room_score_hard):
    cafe = get_object_or_404(Cafe, pk=pk)
    room_list = Room.objects.filter(station = room_cafe_station, score_hard = room_score_hard)
    return render(request, "cafe/room_list.html",{'room_list':room_list})


def room_detail(request,pk):
    room = get_object_or_404(Room, pk=pk)
    review = get_object_or_404(Review, pk= room.pk)
    msn = {"room":room, "review":review,}
    return render(request, "cafe/room_detail.html", msn)


@login_required
def review_new(request,pk):

    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        reviewForm = ReviewForm(request.POST)
        if reviewForm.is_valid():
            review = reviewForm.save(commit=False)
            review.author = request.user
            review.created_at = timezone.now()
            review.save()
            messages.success(request,"리뷰가 성공적으로 등록되었습니다.")
            return redirect(room_detail, pk=pk)
    else:
        reviewForm = ReviewForm()
    return render(request, 'room_detail.html',{'reviewForm':reviewForm , 'review':review})

@login_required
def review_edit(request,pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        reviewForm = ReviewForm(request.POST, instance=review)
        if reviewForm.is_valid():
            review = reviewForm.save(commit=False)
            review.author = request.user
            review.save()
            return redirect(room_detail, pk=pk)

@login_required
def review_delete(request,pk):
    review = get_object_or_404(Review, pk=pk)
    if request.user != review.author:
        messages.ERROR(request,"자신이 작성한 리뷰만 삭제할 수 있습니다.")
        return redirect(room_detail, pk=pk)
    review.delete()
    messages.error(request,"리뷰가 삭제되었습니다.")
    return redirect(room_detail)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Cafe, Room, Review
from .forms import ReviewForm


def index(request):
    station_key = request.POST.getlist("station")
    level_key = request.POST.getlist("level")
    room_list = Room.objects.none()
    if station_key and level_key:
        room_list = Room.objects.filter(cafe__station__in = station_key, level__in = level_key)
    elif station_key:
        room_list = Room.objects.filter(cafe__station__in = station_key)
    elif level_key:
        room_list = Room.objects.filter(level__in = level_key)
    paginator = Paginator(room_list, 5)
    page_request_var = 'page'
    page = request.POST.get(page_request_var)
    try:
        room_list_paginate = paginator.page(page)
    except PageNotAnInteger:
        room_list_paginate = paginator.page(1)
    except EmptyPage:
        room_list_paginate = paginator.page(paginator.num_pages)
    return render(request, "cafe/index.html", {
        'room_list':room_list_paginate,
        'page_request_var':page_request_var,
        'stations':station_key,
        'levels':level_key,
        })
#def room_list(request):

def room_detail(request,pk):
    room = get_object_or_404(Room, pk=pk)
    review_form = ReviewForm()
    #review = get_object_or_404(Review, pk= room.pk)

    return render(request, 'cafe/room_detail.html', {
        'room':room, 'review_form':review_form,
        })

@login_required
def review_new(request,room_pk):
    room = get_object_or_404(Room, pk=room_pk)
    if request.method == "POST":
        reviewForm = ReviewForm(request.POST)
        if reviewForm.is_valid():
            review = reviewForm.save(commit=False)
            review.user = request.user
            review.created_at = timezone.now()
            review.room = room
            review.save()
            print("###### save finished #######")
            messages.success(request, "리뷰가 성공적으로 등록되었습니다.")
            return redirect(review.room)
    else:
        reviewForm = ReviewForm()
    return render(request, 'cafe/room_detail.html', {'reviewForm':reviewForm , })

@login_required
def review_edit(request, room_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.user != request.user:
        messages.warning(request, '댓글 작성자만 수정가능합니다')
        return redirect(review.room)
    if request.method == "POST":
        reviewForm = ReviewForm(request.POST, instance=review)
        if reviewForm.is_valid():
            review = reviewForm.save()
            messages.success(request, "리뷰가 성공적으로 수정되었습니다.")
            return redirect(review.room)
    else:
        reviewForm = ReviewForm(instance=review)
    return render(request, 'cafe/review_edit.html', {'reviewForm':reviewForm,})

@login_required
def review_delete(request, room_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user != review.user:
        messages.warning(request, "자신이 작성한 리뷰만 삭제할 수 있습니다.")
        return redirect(review.room)
    if request.method == "POST":
        review.delete()
        messages.success(request,"리뷰가 삭제되었습니다.")
        return redirect(review.room)
    else:
        return render(request, 'cafe/review_confirm_delete.html', {'review':review})

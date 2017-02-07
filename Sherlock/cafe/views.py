from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Cafe, Room, Review
from .forms import ReviewForm


def index(request):
    return render(request,'index.html')

def room_list(request):
    room_list = Room.objects.filter(hard = , location = , )
    return render(request, "room_list.html",{'room_list':room_list})


def room_detail(request,pk):
    room = get_object_or_404(Room, pk=pk)
    review = get_object_or_404(Review, pk= room.pk)
    msn = {"room":room, "review":review,}
    return render(request, "room_detail.html", msn)

"""
@login_required
def review_new(request):
    if request.method == "POST":
        reviewForm = ReviewForm(request.POST)
        if reviewForm.is_valid():
            review = reviewForm.save(commit=False)



@login_required
def review_edit(request):
    pass

@login_required
def review_delete(request):
    pass
"""
from django.contrib import admin
from .models import Cafe, Room, Review
# Register your models here.

admin.site.register(Room)
admin.site.register(Cafe)
admin.site.register(Review)
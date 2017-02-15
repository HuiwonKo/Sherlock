from django.contrib import admin
from .models import Cafe, Room, Review, Like
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CafeResource(resources.ModelResource):
    class Meta:
        model = Cafe
        fields = (
        'id', 'name', 'lnglat', 'station', 'url', 'phone', 'address'
        )

class CafeAdmin(ImportExportModelAdmin):
    resource_class = CafeResource

class RoomResource(resources.ModelResource):
    class Meta:
        model = Room
        fields = (
        'id', 'cafe', 'name', 'number', 'level', 'image', 'story',
        )

class RoomAdmin(ImportExportModelAdmin):
    resource_class = RoomResource

admin.site.register(Room, RoomAdmin)
admin.site.register(Cafe, CafeAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['room','user','content']

admin.site.register(Review, ReviewAdmin)
admin.site.register(Like)
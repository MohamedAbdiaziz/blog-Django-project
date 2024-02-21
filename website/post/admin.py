from django.contrib import admin
from .models import Post
# Register your models here.

from django.contrib.admin import ListFilter
from django.contrib import admin

class postmodeladmin(admin.ModelAdmin):
    list_display = ["title","update", "regDate"]
    list_display_links = ["update"]
    list_editable = ["title"]
    search_fields = ["title"]
    

admin.site.register(Post, postmodeladmin)
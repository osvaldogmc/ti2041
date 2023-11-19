from django.contrib import admin
from .models import Entry, Category, Hashtag, Post, Posteo
# Register your models here.
admin.site.register(Entry)
admin.site.register(Category)
admin.site.register(Hashtag)
admin.site.register(Post)
admin.site.register(Posteo)
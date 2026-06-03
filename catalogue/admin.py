from django.contrib import admin
from .models import Publisher, Category, Game

admin.site.register(Publisher)
admin.site.register(Category)
admin.site.register(Game)
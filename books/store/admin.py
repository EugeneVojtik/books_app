from django.contrib import admin
from django.contrib.admin import ModelAdmin

from store.models import Book, UserBookRelations

admin.site.register(Book)

@admin.register(UserBookRelations)
class UserBookRelationAdmin(ModelAdmin):
    pass
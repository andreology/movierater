from django.contrib import admin
from .models import Book

#customizing admin page
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['published']
    search_fields = ['title', 'description']

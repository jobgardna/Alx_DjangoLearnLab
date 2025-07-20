from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display these fields in the list
    list_filter = ('publication_year', 'author')            # Add filter sidebar
    search_fields = ('title', 'author')                     # Enable search bar
# Django Admin Configuration for Book Model

## Book Registration

The `Book` model was registered with the Django admin interface in `bookshelf/admin.py` using the `@admin.register` decorator.

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year', 'author')
    search_fields = ('title', 'author')
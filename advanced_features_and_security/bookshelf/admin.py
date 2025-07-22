from django.contrib import admin
from .models import Author, Book, Library, Librarian, UserProfile

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')                # Display these fields in the list
    list_filter = ('author',)  # This is a tuple with one element.
    search_fields = ('title', 'author')               # Enable search bar

# Register the rest with default admin
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(UserProfile)
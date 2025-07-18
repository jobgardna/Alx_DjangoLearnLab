# query_samples.py

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --- Sample Queries ---

# 1. List all books in a library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library.name}:")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print("Library not found.")


# 2. Query all books by a specific author
def books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    if books.exists():
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    else:
        print(f"No books found by {author_name}.")


# 3. Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        if hasattr(library, 'librarian'):
            print(f"Librarian for {library.name}: {library.librarian.name}")
        else:
            print("No librarian assigned to this library.")
    except Library.DoesNotExist:
        print("Library not found.")
        

# --- Sample Calls ---

# Replace these with names that exist in your DB when testing
list_books_in_library("Central Library")
books_by_author("George Orwell")
librarian_for_library("Central Library")

print("\nAvailable Libraries:")
for lib in Library.objects.all():
    print(f"- {lib.name}")

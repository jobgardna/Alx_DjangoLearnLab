# CRUD Operations for Book Model

## Create
```python
>>> from bookshelf.models import Book
>>> book = Book(title="1984", author="George Orwell", publication_year=1949)
>>> book.save()
# Output: Book instance saved successfully.

>>> from bookshelf.models import Book
>>> Book.objects.all()
<QuerySet [<Book: 1984>]>

>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
# Book title updated to 'Nineteen Eighty-Four'

>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>
# Book successfully deleted.

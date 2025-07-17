```python
from bookshelf.models import Book

# Create a book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
# <Book: 1984>
```
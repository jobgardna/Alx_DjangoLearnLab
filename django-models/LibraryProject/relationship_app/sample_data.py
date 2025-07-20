from relationship_app.models import Author, Book, Library, Librarian

orwell = Author.objects.create(name="George Orwell")

book1 = Book.objects.create(title="1984", author=orwell)
book2 = Book.objects.create(title="Animal Farm", author=orwell)

lib = Library.objects.create(name="Central Library")
lib.books.set([book1, book2])

librarian = Librarian.objects.create(name="Mr. Smith", library=lib)

print("Sample data added successfully.")

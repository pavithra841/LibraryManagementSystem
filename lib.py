# Library Management System - Basic Version

library = []

def add_book(book_name):
    library.append(book_name)
    print(f"Book added: {book_name}")

def view_books():
    if not library:
        print("No books available")
    else:
        print("Books in Library:")
        for book in library:
            print("-", book)

# Sample usage
add_book("Python Programming")
add_book("Data Structures")

view_books()

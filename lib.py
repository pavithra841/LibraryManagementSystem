

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


def issue_book(book_name):
    if book_name in library:
        print("Book issued:", book_name)
    else:
        print("Book not available")
def login(username, password):
    if username == "admin" and password == "1234":
        print("Login Successful")
    else:
        print("Invalid Credentials")        

add_book("Python Programming")
add_book("Data Structures")

view_books()


class Book:
    def __init__(self, id, title, total_pages, percent_finished_prev, percent_finished_now):
        self.id = id
        self.title = title
        self.total_pages = total_pages
        self.percent_finished_prev = percent_finished_prev
        self.percent_finished_now = percent_finished_now

book1 = Book(1,"The Magic of Reality", 270, 35, 35)
book2 = Book(2,"Fundamentals of Software Architecture", 419, 18, 28)

currently_reading = [book1, book2]

def get_book(id):
    """Return information about a specific book."""
    id = int(id)
    for book in currently_reading:
        if book.id == id:
            return book
    print("Book not found.")

def list_books():
    return currently_reading

def create_book(title, total_pages, percent_finished_prev, percent_finished_now):
    """Create a new book and add it to the list."""
    book = Book(title, total_pages, percent_finished_prev, percent_finished_now)
    currently_reading.append(book)
    return book

def update_book(title, new_total_pages, new_percent_finished_now):
    """Update information about a specific book."""
    book = get_book(title)
    if book:
        book.total_pages = new_total_pages
        book.percent_finished_now = new_percent_finished_now
        print("Book updated successfully.")
        return book
    print("Book not found.")

def delete_book(title):
    """Delete a specific book from the list."""
    book = get_book(title)
    if book:
        currently_reading.remove(book)
        print("Book deleted successfully.")
        return
    print("Book not found.")
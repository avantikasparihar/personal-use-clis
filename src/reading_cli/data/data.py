import os
import yaml

class Book:
    def __init__(self, id, title, total_pages, percent_finished_prev, percent_finished_now):
        self.id = id
        self.title = title
        self.total_pages = total_pages
        self.percent_finished_prev = percent_finished_prev
        self.percent_finished_now = percent_finished_now

# Get the directory of the current script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Join the directory path and the filename to get the full path
file_path = os.path.join(dir_path, 'books.yaml')

with open(file_path, 'r') as file:
    books_data = yaml.safe_load(file)

currently_reading = [Book(**book) for book in books_data]

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
import os
import yaml
from .data import BooksManager, Book

# Get the directory of the current script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Join the directory path and the filename to get the full path
file_path = os.path.join(dir_path, 'books.yaml')

with open(file_path, 'r') as file:
    books_data = yaml.safe_load(file)

currently_reading = [Book(**book) for book in books_data]

class DefaultBooksManager(BooksManager):
    def get_book(self, id):
        """Return information about a specific book."""
        id = int(id)
        for book in currently_reading:
            if book.id == id:
                return book
        print("Book not found.")
        pass

    def list_books(self):
        return currently_reading
        pass

    def create_book(self, new_book):
        """Create a new book and add it to the list."""
        new_book.id = len(currently_reading) + 1
        currently_reading.append(new_book)
        update_yaml()
        return new_book
        pass

    def update_book(self, updated_book):
        """Update information about a specific book."""
        for i, book in enumerate(currently_reading):
            if book.id == updated_book.id:
                currently_reading[i] = updated_book
                update_yaml()
                return updated_book
        print("Book not found.")
        pass

    def delete_book(self, id):
        """Delete a specific book from the list."""
        book = self.get_book(id)
        if book:
            currently_reading.remove(book)
            print("Book deleted successfully.")
            return
        print("Book not found.")
        pass

def update_yaml():
    # Convert the currently_reading list to a list of dictionaries
    books_data = [vars(b) for b in currently_reading]

    # Write the updated list back to the YAML file
    with open(file_path, 'w') as file:
        yaml.safe_dump(books_data, file)
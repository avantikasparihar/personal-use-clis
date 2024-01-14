# cli.py
import datetime
import os
import click

from data.default import DefaultBooksManager

books_manager = DefaultBooksManager()

@click.group("reading-cli")
def reading_cli():
    pass

@reading_cli.command("greet")
@click.option('--name', required=True, help='The person to greet.')
def hello(name):
    current_user = os.getlogin()
    click.echo(f"Hello {name}! \nusername: {current_user} \nToday is {datetime.date.today()}\n")

@reading_cli.command("currently-reading")
@click.option('--id', required=False, help='ID of the book to show.')
def currently_reading(id):
    if id != None:
        book = books_manager.get_book(id)
        click.echo(f"{book.id}. {book.title} - {book.total_pages} pages, {book.percent_finished_now}% complete")
        return

    books = books_manager.list_books()

    click.echo("You're currently reading: ")
    for i, book in enumerate(books):
        click.echo(f"{i+1}. {book.title} - {book.total_pages} pages, {book.percent_finished_now}% complete")

@reading_cli.command("total-pages-read")
@click.option('--id', required=False, help='ID of the book to show.')
def total_pages(id):
    if id != None:
        book = books_manager.get_book(id)
        pages_read = book.total_pages * (book.percent_finished_now - book.percent_finished_prev) / 100
        click.echo(f"You've read {pages_read} pages of {book.title} today")
        return

    books = books_manager.list_books()
    total_pages_read = 0

    for i, book in enumerate(books):
        pages_read = book.total_pages * (book.percent_finished_now - book.percent_finished_prev) / 100
        total_pages_read += pages_read
        click.echo(f"Pages read for {book.title}: {pages_read}")

    click.echo(f"\nYou've read {total_pages_read} pages in total today")

@reading_cli.command("update-progress")
@click.option('--id', type=click.INT, required=True, help='ID of the book to update.')
@click.option('--percent', type=click.INT, required=True, help='New percent complete.')
def update_progress(id, percent):
    book = books_manager.get_book(id)
    book.percent_finished_now = int(percent)
    books_manager.update_book(book)

    click.echo(f"Progress updated for {book.title}")

@reading_cli.command("reset-day")
def reset_day():
    books = books_manager.list_books()

    for i, book in enumerate(books):
        book.percent_finished_prev = book.percent_finished_now
        books_manager.update_book(book)

    click.echo("Progress reset for all books")

def main():
    reading_cli()

if __name__ == '__main__':
    main()

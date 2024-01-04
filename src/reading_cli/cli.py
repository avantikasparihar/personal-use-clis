# cli.py
import datetime
import os
import click

from . import data

@click.group("reading-cli")
def reading_cli():
    pass

@reading_cli.command("greet")
@click.option('--name', required=True, help='The person to greet.')
def hello(name):
    current_user = os.getlogin()
    click.echo(f"Hello {name}! \nusername: {current_user} \nToday is {datetime.date.today()}\n")

@reading_cli.command("show-current")
@click.option('--id', required=False, help='ID of the book to show.')
def currently_reading(id):
    if id != None:
        book = data.get_book(id)
        click.echo(f"{book.id}. {book.title} - {book.total_pages} pages, {book.percent_finished_now}% complete")
        return

    books = data.list_books()

    click.echo("You're currently reading: ")
    for i, book in enumerate(books):
        click.echo(f"{i+1}. {book.title} - {book.total_pages} pages, {book.percent_finished_now}% complete")

@reading_cli.command("show-total-pages")
@click.option('--id', required=False, help='ID of the book to show.')
def total_pages(id):
    if id != None:
        book = data.get_book(id)
        pages_read = book.total_pages * (book.percent_finished_now - book.percent_finished_prev) / 100
        click.echo(f"You've read {pages_read} pages of {book.title} today")
        return

    books = data.list_books()
    total_pages_read = 0

    for i, book in enumerate(books):
        pages_read = book.total_pages * (book.percent_finished_now - book.percent_finished_prev) / 100
        total_pages_read += pages_read
        click.echo(f"Pages read for {book.title}: {pages_read}")

    click.echo(f"\nYou've read {total_pages_read} pages in total today")

def main():
    reading_cli()

if __name__ == '__main__':
    main()

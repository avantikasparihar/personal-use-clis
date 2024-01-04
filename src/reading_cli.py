# cli.py
import datetime
import os
import click

import data

@click.group("reading-cli")
def reading_cli():
    pass

@reading_cli.command("greet")
@click.option('--name', required=True, help='The person to greet.')
def hello(name):
    current_user = os.getlogin()
    click.echo(f"Hello {name}! \nusername: {current_user} \nToday is {datetime.date.today()}\n")

@reading_cli.command("show-current")
def currently_reading():
    books = data.list_books()

    click.echo("You're currently reading: ")
    for i, book in enumerate(books):
        click.echo(f"{i+1}. {book.title} - {book.total_pages} pages, {book.percent_finished_now}% complete")

    click.echo("\n")
    total_pages_read = 0

    # for i in range(len(total_pages)):
    #     pages_read = total_pages[i] * (percent_finished_now[i] - percent_finished_prev[i]) / 100
    #     total_pages_read += pages_read
    #     click.echo(f"Pages read for {currently_reading_books[i]}: {pages_read}")

    click.echo(f"\nYou've read {total_pages_read} pages today")

def main():
    reading_cli()

if __name__ == '__main__':
    main()

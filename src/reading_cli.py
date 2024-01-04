# cli.py
import click
import datetime

@click.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(name):
    click.echo(f"Hello {name}! Today is {datetime.date.today()}\n")

@click.command()
def currently_reading():
    currently_reading_books = ["the magic of reality", "fundamentals of software architecture"]
    total_pages = [270, 419]
    percent_finished_prev = [35, 18]
    percent_finished_now = [35, 28]

    click.echo("You're currently reading: ")
    for i, book in enumerate(currently_reading_books):
        click.echo(f"{i+1}. {book} - {total_pages[i]} pages, {percent_finished_now[i]}% complete")

    click.echo("\n")
    total_pages_read = 0

    for i in range(len(total_pages)):
        pages_read = total_pages[i] * (percent_finished_now[i] - percent_finished_prev[i]) / 100
        total_pages_read += pages_read
        click.echo(f"Pages read for {currently_reading_books[i]}: {pages_read}")

    click.echo(f"\nYou've read {total_pages_read} pages today")

if __name__ == '__main__':
    hello()
    currently_reading()

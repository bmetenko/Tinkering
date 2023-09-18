import click

"""
usage: python -m click_hello --count=2
>>> prompt name:
"""


@click.command()
@click.option(
    '--count',
    default=1,
    help='Number of hellos.'
)
@click.option(
    '--name',
    prompt='name',
    help='Who to greet.'
)
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""

    start_of_program()

    for x in range(count):
        click.echo(f"Hello {name}!")

    end_of_program()

def start_of_program():
    click.echo(click.style("- start of program -", blink=True, fg="red", bold=True))

def end_of_program():
    click.echo(click.style("- end of program -", blink=True, fg="cyan", bold=True))

if __name__ == '__main__':
    hello()
    
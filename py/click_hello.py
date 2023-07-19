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
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()
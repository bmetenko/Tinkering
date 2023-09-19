import click

"""
usage: python3 -m click_hello hello --name=Dan --count=2
"""

@click.group()
def main_group():
    pass

@main_group.command()
@click.option(
    '--count',
    default=1,
    help='Number of hellos.'
)
@click.option(
    '--name',
    # prompt='name',
    help='Who to greet.'
)
def hello(name, count):
    """Simple program that greets NAME for a total of COUNT times."""

    # start_of_program()

    for x in range(count):
        click.echo(f"Hello {name}!")

    # end_of_program()

@main_group.command()
def start_of_program():
    click.echo(click.style("- start of program -", blink=True, fg="red", bold=True))

@main_group.command()
def end_of_program():
    click.echo(
        click.style("- end of", blink=True, fg="cyan", bold=True) + 
        " " + 
        click.style("program -", blink=True, fg="yellow", bold=True)
        )

main_group.add_command(start_of_program)
main_group.add_command(hello)
main_group.add_command(end_of_program)


if __name__ == '__main__':
    main_group()
    
import click

"""
usage: python3 -m click_hello hello --name=Dan --count=2
chained call: python3 -m click_hello start hello --name=Dan --count=2 end
python3 -m click_hello hello // also works

"""


@click.group(chain=True)
@click.option('--debug/--no-debug', default=False)
@click.option(
    '--count',
    default=1,
    help='number of hellos.'
)
@click.option(
    '--name',
    # prompt='name',
    help='who to greet.'
)
@click.pass_context
def main_group(ctx, debug, count, name):
    ctx.ensure_object(dict)
    ctx.obj['DEBUG'] = debug
    ctx.obj['name'] = name
    ctx.obj['count'] = count

@main_group.command()
@click.option(
    '--count',
    default=1,
    help='number of hellos.'
)
@click.option(
    '--name',
    # prompt='name',
    help='who to greet.'
)
@click.pass_context
def hello(ctx, name, count):
    """Simple program that greets NAME for a total of COUNT times."""

    # start_of_program()
    if not name or not count:
        name = ctx.obj['name']
        count = ctx.obj['count']

    for x in range(count):
        click.echo(f"Hello {name}!")

    # end_of_program()


@main_group.command('start')
@click.pass_context
def start_of_program(ctx):
    click.echo(ctx)
    click.echo(click.style("- start of program -", blink=True, fg="red", bold=True))


@main_group.command('end')
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
    main_group(default_map={"name": "user", "count": 1, "debug": True})

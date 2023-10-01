import os
import logging

import click
import rich

"""
usage: python3 -m click_hello hello --name=Dan --count=2
chained call: python3 -m click_hello start hello --name=Dan --count=2 end
python3 -m click_hello hello // also works

if installed using: pip install --editable .
- click_utils --name=reese --name=glen hello
"""


@click.group(chain=True)
@click.option(
    '--debug/--no-debug',
    is_flag=True,
    default=False
)
@click.option(
    '--count',
    default=1,
    help='number of hellos.',
    type=click.IntRange(0, 5, clamp=True)
)
@click.option(
    '--name',
    default=lambda: [os.environ.get("USER", "")],
    help='who to greet.',
    show_default="current user",
    multiple=True
)
@click.option('--upper', 'transform', flag_value='upper',
              default=True)
@click.option('--lower', 'transform', flag_value='lower')
@click.option(
    '-s',
    count=True,
    help='iterable count of s for unit time.'
)
@click.option(
    '--full_seconds',
    help='number of seconds to wait.'
)
@click.option(
    '--time_unit_override',
    type=click.Choice(['minute(s)', 'second(s)', 'hour(s)'], case_sensitive=False),
    default='second(s)'
)
@click.pass_context
def main_group(ctx, debug, count, name, transform, s, full_seconds, time_unit_override):
    ctx.ensure_object(dict)
    ctx.obj['DEBUG'] = debug
    ctx.obj['name'] = name
    ctx.obj['count'] = count
    ctx.obj['seconds'] = s
    ctx.obj['full_seconds'] = full_seconds
    ctx.obj['time_unit_override'] = time_unit_override
    ctx.obj['transformation'] = transform


@main_group.command()
@click.pass_context
def hello(ctx):
    """Simple program that greets NAME for a total of COUNT times."""

    name = ctx.obj['name']
    count = ctx.obj['count']
    # click.echo(int(count))

    if int(count) == 5:
        click.secho('Count is clamped to 5.', fg='red')

    if int(count) == 0:
        click.secho('Count cannot be negative.', fg='red')

    transform_text = ctx.obj['transformation']

    if transform_text == 'lower':
        name = [str(i).lower() for i in name]

    if transform_text == 'upper':
        name = [str(i).upper() for i in name]

    for x in range(count):
        for _name in name:
            click.echo(f"Hello {_name}!")

    # end_of_program()


@main_group.command('start')
@click.pass_context
def start_of_program(ctx):
    """Start of Program Message"""
    click.echo(rich.inspect(ctx))

    click.echo(click.style("- start of program -", blink=True, fg="red", bold=True))


@main_group.command('end')
def end_of_program():
    """End of Program Message"""
    click.echo(
        click.style("- end of", blink=True, fg="cyan", bold=True) +
        " " +
        click.style("program -", blink=True, fg="yellow", bold=True)
    )


main_group.add_command(start_of_program)
main_group.add_command(hello)
main_group.add_command(end_of_program)


@main_group.command('text')
def long_text_example():
    """Scrollable Text Example"""
    click.echo_via_pager("\n".join(f"Line {idx}" for idx in range(20)))


@main_group.command('time')
@click.pass_context
def wait_for(ctx):
    """ Wait For (x) (unit time) """
    import time
    seconds = ctx.obj['seconds']
    full_seconds = ctx.obj['full_seconds']
    time_unit = ctx.obj['time_unit_override']

    multiply = 1
    if time_unit == 'minute(s)':
        multiply = 60

    if time_unit == 'hour(s)':
        multiply = 360

    # python3 -m click_hello -ssss time
    with click.progressbar([i for i in range(0, int(seconds))]) as bar:
        for x in bar:
            print(f" counted sleep({x} / {seconds} {time_unit})...")
            time.sleep(multiply)

    with click.progressbar([i for i in range(0, int(full_seconds))]) as bar:
        for x in bar:
            print(f" counted sleep({x} / {seconds} {time_unit})...")
            time.sleep(multiply)


@main_group.command('path_copy')
def path_copy():
    """ Copy path to clipboard """

    import platform
    import os
    import subprocess

    current_dir = os.getcwd()

    if platform.system() == 'Darwin':
        cmd = 'echo ' + str(current_dir).strip() + '|pbcopy'
        subprocess.check_call(cmd, shell=True)

    if platform.system() == 'Windows':
        cmd = 'echo ' + str(current_dir).strip() + '|clip'
        return subprocess.check_call(cmd, shell=True)




if __name__ == '__main__':
    main_group(default_map={"count": 1, "debug": True, 'full_seconds': '0', 's': 0, 'transformation': 'lower'})

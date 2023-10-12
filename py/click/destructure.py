import dis, io
from itertools import cycle

from rich.tree import Tree
from rich.text import Text
from rich.panel import Panel
from rich import print

import click_hello


def test_hello():
    if True:
        a = [i for i in ['a', 'b', 'c']]
        print(a)
    else:
        print((1,2))
    print("Hello")


test_dis = dis.Bytecode(test_hello)

first_tree = Tree(
    f"{test_hello.__name__}",
    guide_style="bold black",
)


color1 = cycle(['red', 'green', 'blue'])


def next_tree(diss, init_tree):
    for instr in diss:
        color = next(color1)
        branch = init_tree.add(
            f"[bold {color}]{instr.opname}",
            guide_style=color
        )

        branch_text =f"Value: `{instr.argval}`"

        if instr.is_jump_target:
            branch_text += f" : [jump target] offset: {instr.offset}"

        val_branch = branch.add(Panel(Text(branch_text, style='yellow'), style=color))
        if type(instr.argval).__name__ == 'code':
            next_diss = dis.Bytecode(instr.argval)

            next_tree(next_diss, val_branch)


next_tree(test_dis, first_tree)
print(first_tree)
import dis, io

from rich.tree import Tree
from rich.text import Text
from rich import print

import click_hello


def test_hello():
    [i for i in ['a', 'b', 'c']]
    print("Hello")


test_dis = dis.Bytecode(test_hello)

first_tree = Tree(
    f"{test_hello.__name__}",
    guide_style="bold black",
)


def next_tree(diss, init_tree):
    for instr in diss:
        # print(instr)
        branch = init_tree.add(
            f"[bold yellow]{instr.opname}",
        )

        branch.add(Text(f"Value: {instr.argval}", style='blue'))

        if type(instr.argval).__name__ == 'code':
            # print(dir(instr.argval))
            next_diss = dis.Bytecode(instr.argval)

            next_tree(next_diss, branch)


next_tree(test_dis, first_tree)
print(first_tree)
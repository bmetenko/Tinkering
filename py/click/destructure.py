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

for instr in test_dis:
    print(instr)
    branch = first_tree.add(
            f"[bold yellow]{instr.opname}",
        )

    branch.add(Text(f"Value: {instr.argval}", style='blue'))

    if type(instr.argval).__name__ == 'code':
        print(dir(instr.argval))
        next_dis = dis.Bytecode(instr.argval)

        for inst in next_dis:
            branch2 = branch.add(
                f"[bold yellow]{inst.opname}",
            )
            branch2.add(Text(f"Value: {inst.argval}", style='green'))

print(first_tree)
# import types
#
# source_py = "click_hello.py"
#
# with open(source_py) as f_source:
#     source_code = f_source.read()
#
# byte_code = compile(source_code, source_py, "exec")
# dis.dis(byte_code)
#
# for x in byte_code.co_consts:
#     if isinstance(x, types.CodeType):
#         sub_byte_code = x
#         func_name = sub_byte_code.co_name
#         print('\nDisassembly of %s:' % func_name)
#         dis.dis(sub_byte_code)
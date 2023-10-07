import dis, io

from rich.tree import Tree
from rich import print

import click_hello


def test_hello():
    print("Hello")


test_dis = dis.Bytecode(test_hello)

first_tree = Tree(
    f"{test_hello.__name__}",
    guide_style="bold black",
)

for instr in test_dis:
    branch = first_tree.add(
            f"[bold yellow]{instr}",
        )

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
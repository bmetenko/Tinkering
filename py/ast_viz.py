import ast
from pprint import pprint

def main():
    parsed = ast.parse("""print('hello world')""")
    print(ast.dump(parsed))

    with open("py/paths.py", "r") as python_file:
        ast_tree = ast.parse(python_file.read())

    dump = ast.dump(ast_tree, indent=2)
    print(dump)


class NewVisitor(ast.NodeVisitor):
    
    def __init__(self):
        self.all_nodes = []
    
    def node_visit(self, node):
        for alias in node.names:
            self.all_nodes.append(alias.name)
        
        self.generic_visit(node)

    def visit_Call(self, node):
        self.all_nodes.append(node._fields)
        fields = {}
        for field in node._fields:
            fields.update({
                field: node.__dict__[field]
            })

        self.all_nodes.append(fields)
        self.generic_visit(node)

    def visit_Name(self, node):
        self.all_nodes.append(node._fields)
        self.generic_visit(node)

    def print_all(self):
        pprint(self.all_nodes)

if __name__ == "__main__":
    main()

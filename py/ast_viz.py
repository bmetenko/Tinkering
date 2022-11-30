import ast
from pprint import pprint

def main():
    parsed = ast.parse("""print('hello world')""")
    print(ast.dump(parsed))

    with open("paths.py", "r") as python_file:
        ast_tree = ast.parse(python_file.read())

    visitor = NewVisitor()
    visitor.visit(ast_tree)
    visitor.print_all()


class NewVisitor(ast.NodeVisitor):
    
    def __init__(self):
        self.all_nodes = []
    
    def node_visit(self, node):
        for alias in node.names:
            self.append(alias.name)
        
        self.generic_visit(node)

    def print_all(self):
        pprint(self.all_nodes)

if __name__ == "__main__":
    main()
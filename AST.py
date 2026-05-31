from rule_engine import parser, Context
import inspect

def print_ast(node, indent=0):
    pad = "  " * indent
    print(f"{pad}{node.__class__.__name__}")

    for name, value in inspect.getmembers(node):
        if name.startswith("_") or inspect.ismethod(value) or inspect.isfunction(value):
            continue

        # element AST
        if hasattr(value, "__class__") and value.__class__.__module__.startswith("rule_engine"):
            print(f"{pad}  -> {name}:")
            print_ast(value, indent + 2)

        # lista elementów AST
        elif isinstance(value, list):
            print(f"{pad}  -> {name}: [")
            for item in value:
                print_ast(item, indent + 2)
            print(f"{pad}  ]")

        # prymitywy
        else:
            print(f"{pad}  -> {name}: {value}")


ctx = Context()
p = parser.Parser()

ast = p.parse("wiek >= 18 and kraj =~ '^PL'", ctx)

print_ast(ast)

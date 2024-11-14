import ast
# Example: Parse a simple expression into an AST
expr = "(5 + 4) * 6 + 3"
parsed_ast = ast.parse(expr, mode='eval')
# Visualizing the AST
result = ast.dump(parsed_ast, indent=4)

print(result)
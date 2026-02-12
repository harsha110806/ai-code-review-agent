import ast

class CodeParser:
    """
    Parses Python source code and extracts structural information
    for context-aware code review.
    """

    def __init__(self, code: str):
        self.code = code
        self.tree = ast.parse(code)

    def get_functions(self):
        """
        Extract all function definitions from the code.
        """
        functions = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                functions.append({
                    "name": node.name,
                    "args": [arg.arg for arg in node.args.args],
                    "line_count": node.end_lineno - node.lineno + 1 if hasattr(node, "end_lineno") else None
                })
        return functions

    def get_control_structures(self):
        """
        Count loops and conditional statements.
        """
        loops = 0
        conditionals = 0

        for node in ast.walk(self.tree):
            if isinstance(node, (ast.For, ast.While)):
                loops += 1
            if isinstance(node, ast.If):
                conditionals += 1

        return {
            "loops": loops,
            "conditionals": conditionals
        }

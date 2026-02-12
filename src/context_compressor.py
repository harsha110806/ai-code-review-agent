class ContextCompressor:
    """
    Compresses extracted code context into a concise summary
    suitable for AI-based code review.
    """

    def __init__(self, functions, control_structures):
        self.functions = functions
        self.control_structures = control_structures

    def compress(self):
        summary = {
            "total_functions": len(self.functions),
            "functions": [],
            "loops": self.control_structures.get("loops", 0),
            "conditionals": self.control_structures.get("conditionals", 0)
        }

        for func in self.functions:
            summary["functions"].append({
                "name": func["name"],
                "args_count": len(func["args"]),
                "line_count": func["line_count"]
            })

        return summary

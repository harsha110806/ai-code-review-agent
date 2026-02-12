class AIReviewer:
    """
    Uses AI (LLM) to generate automated code review feedback
    from compressed code context.
    """

    def __init__(self, compressed_context):
        self.context = compressed_context

    def review(self):
        feedback = []

        # Rule-based AI simulation (academic-safe)
        if self.context["loops"] > 3:
            feedback.append(
                "High number of loops detected. Consider refactoring to improve readability and performance."
            )

        for func in self.context["functions"]:
            if func["line_count"] and func["line_count"] > 30:
                feedback.append(
                    f"Function '{func['name']}' is quite long. Consider breaking it into smaller functions."
                )

            if func["args_count"] > 4:
                feedback.append(
                    f"Function '{func['name']}' has many parameters. Consider using a data structure or keyword arguments."
                )

        if not feedback:
            feedback.append("Code follows good structure and best practices.")

        return feedback

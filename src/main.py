from parser import CodeParser
from context_compressor import ContextCompressor
from ai_reviewer import AIReviewer


def run_code_review(code: str):
    parser = CodeParser(code)
    functions = parser.get_functions()
    control_structures = parser.get_control_structures()

    compressor = ContextCompressor(functions, control_structures)
    compressed_context = compressor.compress()

    reviewer = AIReviewer(compressed_context)
    feedback = reviewer.review()

    return feedback


if __name__ == "__main__":
    sample_code = """
def example(a, b, c, d, e):
    for i in range(5):
        for j in range(3):
            if i % 2 == 0:
                print(i, j)
    return a + b + c + d + e
"""

    results = run_code_review(sample_code)

    print("AI Code Review Feedback:")
    for item in results:
        print("-", item)

from parser import CodeParser
from context_compressor import ContextCompressor
from ai_reviewer import AIReviewer
from refiner import CodeRefiner


def run_code_review(code: str):
    parser = CodeParser(code)
    functions = parser.get_functions()
    control_structures = parser.get_control_structures()

    compressor = ContextCompressor(functions, control_structures)
    compressed_context = compressor.compress()

    reviewer = AIReviewer(compressed_context)
    feedback = reviewer.review()

    refiner = CodeRefiner(code, feedback)
    refined_code = refiner.refine()

    return feedback, refined_code


if __name__ == "__main__":
    sample_code = """
def process_orders(orders, tax_rate, discount, shipping_fee, service_charge, region):
    total_revenue = 0

    for order in orders:
        order_total = 0

        for item in order["items"]:
            if item["quantity"] > 0:
                item_price = item["price"] * item["quantity"]
                order_total += item_price

                if region == "international":
                    order_total += item_price * 0.1

        if discount > 0:
            order_total -= discount

        order_total += shipping_fee + service_charge
        total_revenue += order_total

    return total_revenue
"""

    feedback, refined = run_code_review(sample_code)

    print("AI Code Review Feedback:")
    for f in feedback:
        print("-", f)

    print("\nRefined Code Output:")
    print(refined)

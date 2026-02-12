def process_orders(orders, tax_rate, discount, shipping_fee, service_charge, region):
    total_revenue = 0

    for order in orders:
        order_total = 0

        for item in order["items"]:
            if item["quantity"] > 0:
                item_price = item["price"] * item["quantity"]
                order_total += item_price

                if region == "international":
                    order_total += item_price * 0.1  # extra tax

        if discount > 0:
            order_total -= discount

        order_total += shipping_fee + service_charge
        total_revenue += order_total

    return total_revenue

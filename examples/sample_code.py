def calculate_total(price, tax, discount, shipping, service_fee):
    total = price + tax + shipping + service_fee
    if discount > 0:
        total -= discount

    for i in range(3):
        print("Processing step", i)

    return total

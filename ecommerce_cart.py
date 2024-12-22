def calc_total(items):
    if not items:
        return "Cart is empty."
    total_price = sum(items.values())
    if len(items) > 5:
        total_price *= 0.9 
    return f"Total Price: {total_price}"


cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
print(calc_total(cart_items))

#Task 1:


def unpack_tuple(manifest):
    for order in manifest:
        name, item, quantity = order
        print(f"{name} placed an order for {quantity} {item}")


orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Cameras", 2),
    ("Joe", "Desktop", 1),
    ("Andreas", "Keyboard", 1)
]

unpack_tuple(orders)
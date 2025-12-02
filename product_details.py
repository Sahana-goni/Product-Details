def get_product_info(product_id, name, quantity, price):
    formatted_info = (
        f"Product Information:\n"
        f"---------------------\n"
        f"Product ID : {product_id}\n"
        f"Name       : {name}\n"
        f"Quantity   : {quantity}\n"
        f"Price      : ${price:.2f}"
    )
    return formatted_info


# Example usage:
print(get_product_info("P1001", "Wireless Mouse", 25, 19.99))


# This script follows PEP 8 conventions:
#   4 spaces per indentation level
#   snake_case naming for variables and functions
#   lines kept to 79 characters or fewer
#   clear, single purpose comments


def calculate_total_price(unit_price, quantity, tax_rate=0.16):
    """
    Calculate the total price of an order, including tax.

    Parameters:
        unit_price (float): price of a single unit
        quantity (int): number of units bought
        tax_rate (float): tax rate as a decimal (default 16%)

    Returns:
        float: the final total price, tax included
    """
    subtotal = unit_price * quantity
    tax_amount = subtotal * tax_rate
    total_price = subtotal + tax_amount
    return total_price


# Demonstrating at least three different variable assignments
student_name = "Peter Kamau"          # string assignment
number_of_items = 3                   # integer assignment
price_per_item = 250.0                # float assignment
is_discount_applied = False           # boolean assignment

# Using the function defined above
final_price = calculate_total_price(price_per_item, number_of_items)

print("Student:", student_name)
print("Items bought:", number_of_items)
print("Price per item:", price_per_item)
print("Discount applied?", is_discount_applied)
print("Final price (with tax):", round(final_price, 2))
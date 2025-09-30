"""
Title: Total Stock Value from Product String

Problem Statement:
You are given a string S that contains various product names, their prices,
and quantities in the following format:

    Product1:Price1:Quantity1;Product2:Price2:Quantity2;...

Your task is to calculate the total value of the stock.
The total value is calculated by multiplying the price of each product by
its quantity and summing these values.

Input Specification:
- input1: A string S in the specified format.

Output Specification:
- Return an integer value representing the total value of the stock.

Example:
Input:
S = "Apple:250:10;Banana:120:15;Orange:300:5"
Output:
5800

Explanation:
Apple → 250 * 10 = 2500
Banana → 120 * 15 = 1800
Orange → 300 * 5  = 1500
Total  = 5800
"""

def total_stock_value(S: str) -> int:
    total = 0
    # Split by ';' to get each product record
    products = S.split(';')
    for item in products:
        if not item.strip():
            continue
        # Split each product by ':' to get name, price, quantity
        parts = item.split(':')
        if len(parts) != 3:
            raise ValueError("Invalid format. Expected Product:Price:Quantity.")
        _, price, quantity = parts
        total += int(price) * int(quantity)
    return total


# -------- User Input --------
S = input("Enter products in the format Product:Price:Quantity;... : ").strip()

try:
    print("Total stock value:", total_stock_value(S))
except ValueError as e:
    print("Error:", e)

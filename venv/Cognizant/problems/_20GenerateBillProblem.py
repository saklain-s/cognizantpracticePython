"""
Vohra went to a movie with his friends in a Wave theatre and duri
break time he bought pizzas, puffs and cool drinks. Consider the
following prices :
· Rs.100/pizza
. Rs.20/puffs
· Rs.10/cooldrink
. Generate a bill for What Vohra has bought.
"""

x = int(input()) * 100
y = int(input()) * 20
z = int(input()) * 10
print(x+y+z)

pizza_price = 100
puff_price = 20
cooldrink_price = 10

pizza_qty = int(input("Enter number of pizzas: "))
puff_qty = int(input("Enter number of puffs: "))
cooldrink_qty = int(input("Enter number of cool drinks: "))

total = pizza_qty*pizza_price + puff_qty*puff_price + cooldrink_qty*cooldrink_price

print("Total Bill: Rs.", total)

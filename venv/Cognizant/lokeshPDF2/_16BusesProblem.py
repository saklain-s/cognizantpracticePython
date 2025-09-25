# Problem Statement:
# Sunland operates two types of transport services for its annual Summer Festival: Buses and Shuttles.
# A bus can carry up to 80 people and a shuttle can carry up to 8 people.
# There are N people who need to be transported to the festival grounds.
# Each bus requires P litres of fuel and each shuttle requires Q litres of fuel to complete the trip.
# The fuel price in Sunland is 75 coins per litre.
# Task: Find the minimum fuel cost (in coins) required to transport all N people.


people = int(input())
bus_fuel = int(input())
shuttle_fuel = int(input())
fuel_price = 75
min_cost = float('inf')
max_buses = (people + 79) // 80

for bus in range(max_buses+1):
    remaining = max(0,people - bus*80)
    shuttles = (remaining + 7) // 8
    cost = (bus * bus_fuel + shuttles * shuttle_fuel) * fuel_price
    min_cost = min(min_cost,cost)
print(min_cost)


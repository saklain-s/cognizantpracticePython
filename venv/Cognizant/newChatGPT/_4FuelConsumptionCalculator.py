# Problem: Fuel Consumption Calculator
#
# Calculate the fuel consumption of a truck in both European units (liters per 100 km)
# and U.S. units (miles per gallon). Handle invalid inputs gracefully.
#
# Input:
#   - distance_traveled (in km)
#   - fuel_consumed (in liters)
#
# Output:
#   - Fuel consumption in liters/100 km (European)
#   - Fuel consumption in miles/gallon (U.S.)
#
# Edge Cases:
#   - If distance or fuel is <= 0, print "Invalid Input"
#
# Constants:
#   - 1 mile = 1.609 km
#   - 1 gallon = 3.785 liters
#
# Example:
# Input: distance_traveled = 100, fuel_consumed = 5
# Output:
#   European: 5.0 L/100km
#   US: 47.043 mpg

# Input from user
distance = float(input("Enter distance traveled in km: "))
fuel = float(input("Enter fuel consumed in liters: "))

# Check for invalid input
if distance <= 0 or fuel <= 0:
    print("Invalid Input")
else:
    # European consumption (liters per 100 km)
    european = (fuel * 100) / distance

    # US consumption (miles per gallon)
    miles = distance / 1.609
    gallons = fuel / 3.785
    us = miles / gallons

    # Output results
    print("European: {:.2f} L/100km".format(european))
    print("US: {:.2f} mpg".format(us))

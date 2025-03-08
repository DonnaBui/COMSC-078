# Functions Part 3: Phone Plan - Donna Bui - 2/14/2023 - Professor Henry Estrada's COMSC 078

def get_units():
    units = int(input("Enter number of units used: " ))
    if units < 0:
        print("You cannot have negative units.")
        return get_units() # ask the user to input units again if they put a negative number
    else:
        return units

def calculate_cost(units, baseCost, freeUnits, costPastLimit, planName):
    cost = baseCost
    if freeUnits-units < 0:
        extraUnits = units-freeUnits
        fee = (extraUnits*costPastLimit)*0.01
        cost += fee
    print("Cost for", planName,"is $", "%.2f" % cost)
    return cost
        
    
units = get_units()
plan1 = calculate_cost(units, 9.38, 65, 4.5, "Plan 1") # Calculate cost for first plan based on instructions in canvas
plan2 = calculate_cost(units, 8.57, 50, 5.2, "Plan 2") # Same for Plan 2

if plan1 < plan2:
    print("Plan 1 is cheaper.")
elif plan2 < plan1:
    print("Plan 2 is cheaper.")
else: # just in case
    print("Both plans are equal.")
    
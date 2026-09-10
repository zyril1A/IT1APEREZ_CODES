# Code Challenge 3
# Global Freight Calculator

# INPUTS

sender_name = input("Enter name: ")
item_type = input("Type of Item: ")
is_fragile = bool(input("Fragile(True/False)? "))
weight = float(input("Weight(kg): "))
distance = float(input("Distance(km): "))
is_express = bool(input("Express(True/False)? "))
is_international = bool(input("International(True/False)? "))

# TOTAL

base_cost = (weight * 2.50) + (distance * 0.15)
i_total = (base_cost * 1.40) + 50
eh_total = (base_cost * 1.20) + 25
ov_total = base_cost + 30

# PRINT

if (weight <= 2 and distance <= 100) and (is_express == False and is_international == False):
	print("Total = 0")
elif is_express == True and is_international == True:
	print("\nTotal =", i_total)
elif (is_express == True and is_international == True) and weight > 20:
	print("Total =", eh_total)
elif weight > 30 or distance > 1000:
	print("Total =", ov_total)
else:
	print("Total =", base_cost)

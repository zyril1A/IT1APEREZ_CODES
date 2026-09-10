# Write a python program that accepts an integer number as age
# and determines the age group label base of that input

name = input("Enter Name: ")
age = int(input("Enter Age: "))

print("Hi,", name, "\b! That age is considered as:")

if age >= 1 and age <= 5:
	print ("INFANT")
elif age >= 6 and age <= 12:
	print ("KID")
elif age >= 13 and age <= 19:
	print ("TEENAGER")
elif age >= 20 and age <= 29:
	print ("EARLY ADULTHOOD")
elif age >= 30 and age <= 48:
	print ("ADULT")
elif age >= 49 and age <= 59:
	print ("ADVANCE ADULT")
elif age >= 60 and age <= 150:
	print ("SENIOR")
else:
	print ("INVALID.")



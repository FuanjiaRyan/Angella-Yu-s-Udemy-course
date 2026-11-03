# print("Welcome to the tip calculator!")

# total = float(input("What was the total bill? $"))

# how_much = int(input("How much tip will you like to give? 10%, 12%, or 15%? "))

# tip = 0
# each_person = 0

# if how_much == 10:
#     tip = total * 0.10
# elif how_much == 12:
#     tip = total * 0.12
# elif how_much == 15:
#     tip = total * 0.15
# else:
#     print("Price percentage out of range")

# people = int(input("How many people to split the bill? "))
# each_person = tip * people

# print(f"Each person should pay: ${each_person:.2f}")

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip will you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = tip / 100 * bill + bill

bill_per_person = bill_with_tip / people

print(f"Each person should pay ${bill_per_person:.2f}")
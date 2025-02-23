# Pizza Order Program   

print("Welcome to Python's Pizza Deliveries")

# Getting user inputs
size = input("What size of pizza do you want? S(Small), M(Medium), L(Large): ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

# Initialize bill to 0
bill = 0

# Checking the size of the pizza
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong pizza size.")
    bill = None  # Invalid size, no bill
    print("Please start again with a valid size.")
    exit()

# Checking for pepperoni
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Checking for extra cheese
if extra_cheese == "Y":
    bill += 1

# Only print the bill if the size was valid
if bill is not None:
    print(f'Your Pizza Total is ${bill}')

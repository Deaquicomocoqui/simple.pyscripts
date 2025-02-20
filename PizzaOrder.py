# Pizza Order Program   

print("Welcome to Python's Pizza Deliveries")
size = input("What size of pizza do you want? S(Small), M(Medium), L(Large): ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0 
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong pizza size.")
    
if pepperoni == "Y":
    if size == "S":
        bill = bill + 2
    else:
        bill = bill + 3

if extra_cheese == "Y":
    bill = bill + 1

print(f'Your Pizza Total is ${bill}')
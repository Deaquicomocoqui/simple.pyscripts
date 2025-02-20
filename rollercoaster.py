
print("""
      ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----
       """)

print("\nWelcome to the rollercoaster!")
height = int(input("What is your height in Centimeters (cm)? \n"))
if height >= 120:
    print("\nYou can ride the rollercoaster safely!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
    elif age <= 18:
        bill = 7
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
    want_photo = input("Do you want to have a photo taken? Type y for Yes and n for No.\n")
    if want_photo == "y":
        bill = bill + 3
    print(f'Your final bill is {bill}')
else:
    print("\nSorry your height is not currently allowed in this ride, its for your own safety")

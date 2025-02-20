import time

print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill? \n$"))
tip = int(input("How much percentage of tip would you like to give? 5%, 10%, or 12%?\n"))
people = int(input("How many people to split the bill? \n"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print("\nCALCULATING!\nPLEASE WAIT!\n")
time.sleep(1)
print((f'Each person should pay: \n ${final_amount} \n'))

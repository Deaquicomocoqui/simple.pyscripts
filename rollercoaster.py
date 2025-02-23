art = r''' 
Welcome                                       __
                                       _  |  |
                   Yye                |_| |--|
                .---.  e           AA | | |  |
               /.--./\  e        A
              // || \/\  e      A
             //|/|| |\/\   aa a    |\o/ o/--
            ///|\|| | \/\ .       ~o \.'\.o'
           //|\|/|| | |\/\ .      /.` \o'
          //\|/|\|| | | \/\ ( (  . \o'
  __ __ _//|/|\|/|| | | |\/`--' '
 __/__/__//|\|/|\|| | | | `--'
 |\|/|\|/|\|/|\|/|| | | | |
RG'''

print(art)
print("\nWelcome to the rollercoaster!")

# Get height input from the user
height = int(input("What is your height in Centimeters (cm)? \n"))

if height >= 120:
    print("\nYou can ride the rollercoaster safely!")
    
    # Get age input from the user
    age = int(input("What is your age? "))
    
    # Determine the base price based on age
    if age <= 12:
        bill = 5
    elif age <= 18:
        bill = 7
    elif 45 <= age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
        bill = 0  # Free ride for 45-55 age group
    else:
        bill = 12

    # Ask if the user wants a photo
    want_photo = input("Do you want to have a photo taken? Type y for Yes and n for No.\n").lower()
    
    if want_photo == "y":
        bill += 3
    
    # Print the final bill
    print(f'Your final bill is ${bill}')
else:
    print("\nSorry, your height is not currently allowed on this ride, it's for your own safety.")

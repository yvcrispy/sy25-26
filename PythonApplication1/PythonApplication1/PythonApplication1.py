lineup = [
    ("Code Play", "Indie", 30),
    ("The Pythonistas", "Rock", 45),
    ("Syntax Error", "Metal", 60)
]
selection = 0
time = 0

print("Welcome to the PyFest 2026 Manager!")
while selection != "6":
    print(" ")
    print("1. View Lineup and Total Time Allotted")
    print("2. Add a New Band")
    print("3. Move First Band to End")
    print("4. Remove Band")
    print("5. Move Band to Specific Position")
    print("6. Exit")
    selection = int(input("Please select an option from 1-6: "))
    print(" ")
    if selection == 1:
        for item in lineup:
            time = time + item[2]
            print("Name of Band:",item[0],)
            print("Genre:",item[1])
            print("Time Allotted:", item[2])
        print("The festival should last", time, "minutes.")
    elif selection == 2:
        new_name = input("What is the name of the incoming band?: ")
        new_genre = input("What genre does " + new_name + " play?: ")
        new_time = int(input("How much long are they going to be playing? (in minutes): "))
        full_new = (new_name, new_genre, new_time)
        lineup.append(full_new)
        print(new_name + " has been added to the roster.")
    elif selection == 3:
        first_band = lineup.pop(0)
        lineup.append(first_band)
        print((first_band[0]) + " has been moved to the end.")
    elif selection == 4:
        x_check = input("Which band would you like to remove from the roster?: ")
        for item in lineup:
            if item[0] == x_check:
                lineup.remove(item)
                print("Removed successfully.")
    elif selection == 5:
        numofband = 0
        for item in lineup:
            numofband = numofband + 1
        move_band = input("Which band would you like to move? ")
        location = int(input("Where would you like to move " + move_band + "? " + "(1 - " + str(numofband) + "): "))
        #finish up this part and we're go to go i think
        lineup.add(move_band)
    elif selection > 6 or selection < 1:
        print("Please select a number between 1 and 6.")
    else:
        print("Thank you for using the PyFest 2026 manager! Enjoy the show!")
        break


lineup.pop(0)
print(lineup)

for item in lineup:
    time = time + item[0]
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
    if selection == 1:
        for item in lineup:
            #the following line don't wor????
            time = time + item[0]
            print(time)
    elif selection == 2:
        print("2")
    elif selection == 3:
        first_band = lineup.pop(0)
        lineup.append(first_band)
        print((first_band[0]) + " has been moved to the end.")
    elif selection == 4:
        print("4")
    elif selection == 5:
        print("5")
    elif selection > 6 or selection < 1:
        print("Please select a number between 1 and 6.")
    else:
        print("Thank you for using the PyFest 2026 manager! Enjoy the show!")
        break


lineup.pop(0)
print(lineup)

for item in lineup:
    time = time + item[0]
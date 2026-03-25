"""
the idea is simple:
-the checklist!!! to see if he is correct!!!
-who is he?? the apple
-start with an empty file
-the file might look something as follows:
(date + time)
apple 1:
apple color: (green/yellow/red)
is apple rotton?: (yes/no)
apple size: (small = <150, medium = 150><200, large = >200)
apple 2:
apple color: (green/yellow/red)
is apple rotton?: (yes/no)
apple size: (small = <150, medium = 150><200, large = >200)
-save the file at that date and time
-intake all the apple varieties on the file
-count the number of apples of each color
-count number of apples in specidic size
-count number of rotton apples
return individual apple list if user asks
return final counts of everything if user asks
"""
file = open("apple.txt", "r")
filecontent = file.read()
file.close()
file = open("apple.txt", 'a')
#print (filecontent)
count = 0
print("The apple catalog")
print("~~~~~~~~~~~~~~~~~")
choice = 0
while choice != 4:
    print("What would you like to do?")
    choice = input("1). add apple   2). view apples   3). count apples   4). exit")
    if choice == "1":
        count = count + 1
        color = input("Is the apple yellow, green, or red?: ")
        while color != "red" and color != "yellow" and color != "green":
            print("Invalid apple color. Try again.")
            color = input("Is the apple yellow, green, or red?: ")
        print("The apple is "+ color + ".")
        size = -1
        tag = "none"
        while tag != "large" or tag != "medium" or tag != "small":
            size = int(input("In grams, how much does the apple weigh?: "))
            if size > 200:
                tag = "large"
                print("The apple is large.")
                break
            elif size <= 200 and size >= 150:
                tag = "medium"
                print("The apple is medium.")
                break
            elif size <= 150 and size > 0:
                tag = "small"
                print("The apple is small.")
                break
            else:
                print("Please insert a vaild number for the apple's size.")
        status = input("Is the apple currently rotton? (Yes/No): ")
        status = status.upper()
        if status == "YES":
            rotton = True
        elif status == "NO":
            rotton = False
        else:
            while status != "YES" and status != "NO":
                print("That is not a valid answer. Try again.")
                status = "Is the apple currently rotton? (Yes/No): "
                statues = status.upper()
                if status == "YES":
                    rotton = True
                elif status == "NO":
                    rotton = False
        if rotton:
            rr = "rotton"
        else:
            rr = "not rotton"
        print("Apple", str(count) + " has been documented. It is " + color + ", " + tag + ", and is " + rr + ".")

rotton = False
applecount= 0
rottoncount= 0
green = 0
red = 0
yellow = 0
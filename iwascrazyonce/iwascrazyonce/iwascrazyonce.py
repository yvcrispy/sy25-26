import datetime
diary = "diary.txt"
diarite = open(diary, 'a')
datentime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M;%S")
print(datentime)
inputted = 0
while inputted != 4:
    print("Diary Program")
    print("Options:")
    print("1.) Write     2.) Read     3.) Clear    4.) Exit")
    inputted = int(input("How would you like to proceed?(1-4): "))
    if inputted == 1:
        newentrynom = input("What is the name of this new entry?: ")
        newentrycont = input("Please write the contents of "+ newentrynom + ": ")
        newentry = diarite.write("------------"+ "\n"+ newentrynom+ "\n"+ datentime+ "\n"+ newentrycont+ "\n")
        print("Entry logged.")
    if inputted == 2:
        print(diarite.read())
    if inputted == 3:
        ask = input("Are you sure? This action will erase all existing entries (Y/N): ")
        while ask.upper() != "Y" or ask.upper != "N":
            if ask.upper() == "Y":
                diarite.close()
                diarite = open(diary, 'w')
                diarite.close()
                diarite = open(diary, 'a')
                print("Entries cleared.")
            elif ask.upper() == "N":
                inputted = 0
            else:
                ask = input("Please type one of the give options(Y/N): ")
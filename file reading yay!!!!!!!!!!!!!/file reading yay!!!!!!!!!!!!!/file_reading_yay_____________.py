filename = input("What file would you like to open?: ")
file = open(filename, 'r')
line = file.readline()
while line:
    print(line)
    line = file.readline()
file.close()
filename = input("File Name:")
pattern = input("Enter pattern:")

file = open(filename, 'r')
lines = file.readlines()

for f in files:


for i,line in enumerate(lines):
    if pattern in line:
        print(filename, (i+1), line)
filename = "output.txt"
file = open(filename, 'a')
for i in range(10):
    file.write(f"This is line {i}. \n")
file.close()
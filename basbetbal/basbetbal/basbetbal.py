seeds = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7 ,10, 2, 15]
winners = ["Purdue", "FDU", "FAU", "Memphis", "Duke", "Oral Roberts", "UVA", "Furman", "Kentucky", "Pitt", "Kansas", "Howard","Texas", "Penn St", "UCLA", "UNC Asheville"]
count = 0
current = 0

for seed in seeds:
    if seed >= 10:
        count = count + 1
        print("Cinderella Alert! " + str(winners[current]) + " pulls the upset!")
    current = current + 1
print("There were " + str(count) + " upsets.")
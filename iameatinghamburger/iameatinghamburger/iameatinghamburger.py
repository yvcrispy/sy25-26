# 1. potato grader
weight = int(input("How much does the potato weigh?"))
if weight < 100:
    print("This is a small grade potato.")
elif weight <= 200:
    print("This is a medium grade potato.")
else:
    print("This is a large grade potato.")
# 2. blemish counter
blem = 0
count = []
total = 0
potato = 1
for i in range(5):
    blem = int(input("How many blemishes are on potato " + str(potato) + "?"))
    count.append(blem)
    potato = potato + 1
total = sum(count)
print("There were " + str(total) + " blemishes across all potatoes.")
print("There was an average of " + str(total/5) + " blemishes per potato.")
# 3. quality control
firstcrate = [0,2,5,1,0,8,3,0]
perfect = []
for item in firstcrate:
    if item == 0:
        perfect.append(item)
percent = (len(perfect) / len(firstcrate))
print("In this crate, " + str(len(perfect)) + " potatoes, or " + str(percent*100) + "% of potatoes were perfect.")
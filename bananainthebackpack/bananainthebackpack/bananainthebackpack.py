import glob
files = glob.glob("server_dump/*.txt") 
OKcount = 0
WARNcount = 0
ERRORcount = 0
OKlist = []
WARNlist = []
ERRORlist = []
for file in files:
    current = open(file, "r")
    status = current.read()
    if "OK" in status:
        OKcount = OKcount + 1
        OKlist.append(file)
    elif "WARN" in status:
        WARNcount = WARNcount + 1
        WARNlist.append(file)
    elif "ERROR" in status:
        ERRORcount = ERRORcount + 1
        ERRORlist.append(file)
    current.close()
print("Files with 'OK' status: "+str(OKcount))
print("Files with 'WARN' status: "+str(WARNcount))
print("Files with 'ERROR' status: "+str(ERRORcount))
ask = ""
while ask != "OK" or ask != "WARN" or ask != "ERROR":
    ask = input("Would which file statues would you like to view? (OK/WARN/ERROR): ")
    if ask == "OK":
        for file in OKlist:
            print(file)
        break
    elif ask == "WARN":
        for file in WARNlist:
            print(file)
        break
    elif ask == "ERROR":
        for file in ERRORlist:
            print(file)
        break
    else:
        print("Please enter one of the given statuses.")
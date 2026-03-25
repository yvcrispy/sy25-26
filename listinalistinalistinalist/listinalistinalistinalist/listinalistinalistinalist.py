
D3 = ["D3", "Seat Toledo Marathon", 220, (195,330), 8400, 5.2, 2100, 5]
F1 = ["F1", "VW Off-Road-Bug", 185, (104,142), 6000, 9.0, 1880, 4]
A4 = ["A4", "Suzuki Ignis", 180, (153,206), 7250, 8.0, 1597, 4]
C1 = ["C1", "Subaru Impreza WRC", 220, (221,300), 5500, 5.4, 1994, 4]
F4 = ["F4", "PRD Racing Team", 200, (125,170), 6500, 7.1, 2700, 6]
G2 = ["G2", "Seat Ibiza GTi", 220, (205,280), 8400, 6.5, 1984, 4]
A2 = ["A2", "Ford Focus WRC", 224, (221,300), 5400, 5.5, 1995, 4]
F3 = ["F3", "Renault Megane", 218, (198,270), 8400, 5.9, 1995, 4]
D4 = ["D4", "Peugeot 206 WRC", 225, (221,300), 5600, 5.4, 1996, 4]
G1 = ["G1", "Citroen Visa 4x4", 190, (74,100), 7680, 9.0, 1566, 4]
H2 = ["H2", "Mitsubishi Lancer", 198, (213,290), 5500, 7.2, 1997, 4]
F2 = ["F2", "Mitsubishi Galant", 180, (216,294), 5800, 6.3, 3395, 4]
E4 = ["E4", "Austin Metro 6", 240, (265,360), 9800, 3.4, 3600, 6]

cars = [D3, F1, A4, C1, F4, G2, A2, F3, D4, G1, H2, F2, E4]

def print_car(c):
    print(c[0] + "  Car Model: " + c[1])
    print("Top Speed: " + str(c[2]) + "km/h" + "     RPM: " + str(c[4]))
    print("HP: " + str(c[3]) + "     0-60: " + str(c[5]))
    print("CCs: " + str(c[6]) + "     Cylinders: " + str(c[7]))

i = 1
for c in cars:
    print(i, c[1])
    i = i + 1
    print(" ")
choice = int(input("Which car would you like to display?"))
choice = choice - 1
print_car(cars[choice])
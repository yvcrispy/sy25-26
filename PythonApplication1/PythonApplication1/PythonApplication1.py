# The initial lineup
lineup = [
    ("Code Play", "Indie", 30),
    ("The Pythonistas", "Rock", 45),
    ("Syntax Error", "Metal", 60)
]

# 1. Add the headliner
headliner = ("The Byte Beats", "Synthwave", 90)
lineup.append(headliner)

removed_band = lineup.pop(0)
lineup.append(removed_band)

gone = lineup.pop(0)
print(lineup)

for i in range(lineup):
    print("tehe")
# Continue the logic below...
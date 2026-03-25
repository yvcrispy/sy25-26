import random
random = random.randint(1,10)
if random == 1:
    secret = "heebeejeebies"
if random == 2:
    secret = "amongus"
if random == 3:
    secret = "creature"
if random == 4:
    secret = "crispy"
if random == 5:
    secret = "obamacare"
if random == 6:
    secret = "showbiz"
if random == 7:
    secret = "omelet"
if random == 8:
    secret = "zhequirioth"
if random == 9:
    secret = "scrimble"
if random == 10:
    secret = "spy"
dashes = ["-"]
guesses = 10
for i in range(len(secret)-1):
    dashes.append("-")
def get_guess():
    answer = input("Guess: ")
    while len(answer) != 1 or not answer.islower():
        if len(answer) != 1:
            print("Your answer must have one letter!")
            answer = input("Guess: ")
        elif not answer.islower():
            print("Your answer must be a lowercase letter!")
            answer = input("Guess: ")
    return answer
def do_word(answer):
    if str(answer) in secret:
        print("That letter is in the word!")
        for i in range (len(secret)):
            if str(answer) == secret[i]:
                dashes[i] = answer
        print(("").join(dashes))
    else:
        print("That letter isn't in the word.")
        print(("").join(dashes))
for i in range(10):
    do_word(get_guess())
    if ("").join(dashes) == secret:
        print("You win! Good Job!")
        break
if ("").join(dashes) != secret:
    print("")
    print("You failed to guess the secret word. The word was " + secret + ".")
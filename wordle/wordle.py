import random

class Colour:
    red = '\033[41m'
    green = '\033[42m'
    orange = '\033[43m'
    reset = '\033[0m'

valids = []
wordles = []
with open("valids.csv", "r") as file:
    valids = file.readline().split(",")
with open("wordles.csv", "r") as file:
    wordles = file.readline().split(",")
valids  = set(valids)
try:
    valids.remove("")
except:
    pass

wordle = random.choice(wordles).upper()
count = 0
wordle_letter_count = {}

for letter in wordle:
    if letter in wordle_letter_count:
        wordle_letter_count[letter] += 1
    else:
        wordle_letter_count[letter] = 1

print("GUESS A WORD:")
for i in range(6):
    matches = 0
    result, guess = [], ""
    temp_wlc = wordle_letter_count.copy()

    while guess.lower() not in valids:
        guess = input().upper()
        if guess.lower() not in valids:
            print("Invalid guess! Try again!")

    for j in range(len(guess)):#each letter in each guess
        current_letter = guess[j]
        if current_letter in wordle:
            if current_letter == wordle[j]: #if perfect match
                result.append(Colour.green + current_letter)
                temp_wlc[current_letter] -= 1
                matches +=1
            else:#do else later
                result.append("*")
        else: #wrong
            result.append(Colour.red + current_letter)

    for s in range(len(result)):
        if result[s] == "*":#letter exists
            if temp_wlc[guess[s]] > 0:
                result[s] = Colour.orange + guess[s]
                temp_wlc[guess[s]] -= 1
            else:
                result[s] = Colour.red + guess[s]
    result[len(guess)-1] += Colour.reset
    print("".join(result))

    count += 1
    if matches == 5:
        print("You took " + str(count) + " guesses!")
        count = -1
        break
if count >=0:
    print("You didn't find the wordle! - " + wordle)


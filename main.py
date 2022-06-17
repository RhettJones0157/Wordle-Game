import random
wordlelist = ['world', 'femur', 'crazy', 'quail', 'snake', 'churn', 'forge', 'lower', 'pause', 'trail', 'under', 'grant', 'store', 'feral', 'dunes', 'tuple', 'scrap', 'match', 'angry', 'gloss', 'chump', 'drunk', 'viral', 'frack', 'prime', 'milky', 'after', 'shell']
randomword = random.randint(0, 14)
word = wordlelist[randomword]
wordle = list(word)
f = '\033[37m'
def guess(place, w, x, y, z):
    if theirs[place] == wordle[w] or theirs[place] == wordle[x] or theirs[place] == wordle[y] or theirs[place] == wordle[z]:
        color = '\033[33m'
    elif theirs[place] == wordle[place]:
        color = '\033[32m'
    else:
        color = '\033[37m'
    return color
for i in range(6):
  guessword = input("Enter word: ")
  theirs = list(guessword)
  if len(theirs) < 5:
    print("Word not long enough.")
  else:
    a = guess(0, 1, 2, 3, 4)
    b = guess(1, 0, 2, 3, 4)    
    c = guess(2, 0, 1, 3, 4)
    d = guess(3, 0, 1, 2, 4)
    e = guess(4, 0, 1, 2, 3)
    print(a + theirs[0] + b + theirs[1] + c + theirs[2] + d + theirs[3] + e + theirs[4] + f)
    if theirs == wordle:
        print("You won!")
        break
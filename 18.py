import string
words = ["hallo", "klempner", "das", "ist", "fantastisch", "fluggegecheimen"]
chances = {}
countInWords = {}
for letter in string.ascii_lowercase:
    chances[letter] = countInWords[letter] = 0

ovLen = 0
for word in words:
    ovLen += len(word)
    for char in word:
        countInWords[char] += 1

for char in countInWords:
    chances[char] = countInWords[char] / ovLen

word = input()

pronChance = chances[word[0]]
if pronChance == 0:
    exit()

prev_chance = pronChance

for i in range(1, len(word)):

    if chances[word[i]] == 0.0:

        if prev_chance == 0.0:
            exit()

        else:
            pronChance *= prev_chance
    
    else:
        pronChance *= chances[word[i]]
        prev_chance = pronChance

print(pronChance)

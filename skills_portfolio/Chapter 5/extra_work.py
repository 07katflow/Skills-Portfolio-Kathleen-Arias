word = "pneumonoultramicroscopicsilicovolcanoconiosis"
letter_count = {}
for letter in word:
    if letter not in letter_count:
        letter_count[letter] = 0
    letter_count[letter] += 1
print(letter_count)
vowels = ['a', 'e', 'i', 'o', 'u']
word = "Milliways"
result = []
for letter in word:
    if letter in vowels:
        if letter not in result:
            result.append(letter)
            print(letter)



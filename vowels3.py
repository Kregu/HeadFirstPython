vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
result = []
for letter in word:
    if letter in vowels:
        if letter not in result:
            result.append(letter)
            print(letter)
            


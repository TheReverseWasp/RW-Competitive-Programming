word = input()
if word == word[0].lower() + word[1:].upper():
    print(word[0].upper() + word[1:].lower())
elif word == word.upper():
    print(word.lower())
else:
    print(word)
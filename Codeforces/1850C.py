words = int(input())
word_list = list()
for __ in range(words):
    cache = ""
    for ___ in range(8):
        temp = input()
        for letter in temp:
            if letter != '.':
                cache += letter
                break
    word_list.append(cache+"")

print("\n".join(word_list))
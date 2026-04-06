tc=int(input())
for _ in range(tc):
    n=int(input())
    bigrams = list(input().split())
    word = bigrams[0]
    i = 1
    while i < len(bigrams):
        if bigrams[i][0] != word[-1]:
            word+=bigrams[i]
        else:
            word+=bigrams[i][1]
        i+=1
    if len(word) < n:
        word += word[-1]
    print(word)
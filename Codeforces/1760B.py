dic = "abcdefghijklmnopqrstuvwxyz"
db = {dic[it]:it + 1 for it in range(len(dic))}
tc = int(input())
for __ in range(tc):
    input()
    word = input()
    answer = 1
    for letter in word:
        answer = max(answer, db[letter])
    print(answer)
tc = int(input())
for __ in range(tc):
    s = input()
    starto = -1
    endo = -1
    answer = 0
    for i in range(len(s)):
        if s[i] == "1":
            if starto == -1:
                starto = i + 0
            endo = i + 0
    for i in range(starto, endo):
        if s[i] == "0":
            answer += 1
    print(answer)

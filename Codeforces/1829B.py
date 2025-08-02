tc = int(input())
for __ in range(tc):
    n = int(input())
    l = list(map(int,input().split()))
    acum, answer = 0, 0
    for i in range(n):
        if l[i] == 1:
            acum = 0
        else:
            acum += 1
            answer = max(answer,acum)

    print(answer)

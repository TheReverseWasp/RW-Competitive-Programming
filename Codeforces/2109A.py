tc = int(input())
for _ in range(tc):
    n = int(input())
    duels = list(map(int,input().split()))
    flag = True
    for i in range(1,n):
        if duels[i] == duels[i-1] and duels[i] == 0:
            flag = False
            break
    if duels.count(0) == 0:
        flag = False
    if flag:
        print("NO")
    else:
        print("YES")
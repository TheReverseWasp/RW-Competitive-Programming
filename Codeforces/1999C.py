tc = int(input())
for __ in range(tc):
    n,s,m = map(int,input().split())
    r = 0
    flag = False
    for i in range(n):
        new_l, new_r = map(int,input().split())
        if new_l - r >= s:
            flag = True
        r = new_r + 0
    if m - r >= s:
        flag = True
    if flag:
        print("YES")
    else:
        print("NO")
tc = int(input())
for _ in range(tc):
    ini, fin = map(int,input().split())
    ans = 0
    while ini <= fin - 2:
        if ini % 2 == 1:
            ans+=1
            ini+=3
        else:
            ini+=1
    print(ans)
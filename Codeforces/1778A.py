tc=int(input())
for _ in range(tc):
    n = int(input())
    a=list(map(int,input().split()))
    ans = sum(a)
    temp = ans + 0
    performed = False
    for i in range(n-1):
        if a[i] == a[i+1] and a[i] == -1:
            temp = ans + 4
            performed = True
            break
        elif a[i] != a[i+1]:
            performed = True
    if not performed:
        print(ans-4)
    else:
        print(temp)
import math
tc=int(input())
for _ in range(tc):
    n=int(input())
    a=list(map(int,input().split()))
    flag = False
    for i in range(n):
        for j in range(n):
            if i <= j:
                if math.gcd(a[i],a[j]) <= 2:
                    flag = True
                    break
        if flag:
            break
    if flag:
        print("yes")
    else:
        print("no")
import math
tc = int(input())
for __ in range(tc):
    n,k,p = map(int,input().split())
    temp = math.ceil(abs(k) / p)
    if temp > n:
        print(-1)
    else:
        print(temp)
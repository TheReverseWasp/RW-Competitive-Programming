tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    ans = a[-1]
    maxo = 0
    for i in range(len(a)-1):
        maxo = max(a[i],maxo)
    print(ans+maxo)
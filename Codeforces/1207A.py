tc=int(input())
for _ in range(tc):
    b,p,f=map(int,input().split())
    h,c=map(int,input().split())
    profit = 0
    if h >= c:
        profit += min(b//2, p) * h
        b -= min(b//2, p) * 2
        profit += min(b//2, f) * c
    else:
        profit += min(b//2, f) * c
        b -= min(b//2, f) * 2
        profit += min(b//2, p) * h
    print(profit)
    
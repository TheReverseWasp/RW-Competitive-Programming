tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(0,n,2):
        temp = abs(a[i] - a[i+1])
        ans = max(temp,ans)
    print(ans)
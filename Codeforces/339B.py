n,m = map(int,input().split())
tasks = list(map(int,input().split()))
imin = 1
ans = 0
for i in range(m):
    if imin > tasks[i]:
        ans += n - imin + 1
        imin = 1
    ans += tasks[i] - imin
    imin = tasks[i] - 0
print(ans)
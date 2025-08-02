n,m = map(int,input().split())
tvs = list(map(int,input().split()))
tvs.sort()
ans = 0
for i in range(m):
    if tvs[i] < 0:
        ans += - tvs[i]
    else:
        break
print(ans)

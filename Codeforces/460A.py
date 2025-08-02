n, m = map(int,input().split())
ans = n + 0
trash = n + 0
while trash >= m:
    n = trash // m
    trash = trash % m + trash // m
    ans += n
print(ans)

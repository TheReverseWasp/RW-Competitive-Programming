n,m,a,b = map(int,input().split())
ans = 0
while n > 0:
    if n >= m:
        if b <= a * m:
            ans += b
        else:
            ans += a * m
        n-=m
    else:
        if n * a <= b:
            ans += a * n
        else:
            ans += b
        n = 0
print(ans)
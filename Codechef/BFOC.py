t = int(input())
while t:
    t-=1
    n, m, l = map(int, input().split())
    cur = l + n - 1
    while m >= l and cur >= l:
        m -= int(m / cur) * cur
        cur = max(m, l)
    print(m)

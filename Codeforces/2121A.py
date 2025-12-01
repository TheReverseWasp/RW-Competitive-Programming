tc = int(input())
for __ in range(tc):
    n, s = map(int,input().split())
    a = list(map(int,input().split()))
    min_a, max_a = min(a), max(a)
    ans = 0
    if s <= min_a:
        ans = max_a - s
    elif s >= max_a:
        ans = s - min_a
    else:
        ans = max_a - min_a
        ans += min(abs(s - min_a), abs(max_a - s))
    print(ans)
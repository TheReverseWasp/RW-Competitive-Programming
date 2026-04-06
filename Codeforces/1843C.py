tc = int(input())
for __ in range(tc):
    bm = int(input())
    ans = bm + 0
    while bm >= 1:
        bm //= 2
        ans += bm
    print(ans)
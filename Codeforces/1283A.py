tc = int(input())
for __ in range(tc):
    h, m = map(int, input().split())
    ans = 24 * 60 - h * 60 - m
    print(ans)

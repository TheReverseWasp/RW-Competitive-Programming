tc = int(input())
for __ in range(tc):
    j, a, b, c = map(int, input().split())
    ans = 3 * (j // (a+b+c))
    j %= a + b + c
    if j <= 0:
        print(ans)
        continue
    j -= a
    ans += 1
    if j <= 0:
        print(ans)
        continue
    j -= b
    ans += 1
    if j <= 0:
        print(ans)
        continue
    j -= c
    ans += 1
    if j <= 0:
        print(ans)
        continue

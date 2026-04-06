tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    ones, minus_ones = a.count(1), a.count(-1)
    ans = 0
    if n <= 3:
        print(n - ones)
        continue
    if n % 2 == 1:
        if ones < n // 2 + 1:
            ans = n // 2 + 1 - ones
            ones = n // 2 + 1
            minus_ones = n - ones
        if minus_ones % 2 == 1:
            ans += 1
        else:
            ans += 0
    else:
        if ones < n // 2:
            ans = n // 2 - ones
            ones = n // 2
            minus_ones = n - ones
        if minus_ones % 2 == 1:
            ans += 1
        else:
            ans += 0

    print(ans)
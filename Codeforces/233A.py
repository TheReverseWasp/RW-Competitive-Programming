n = int(input())
if n%2 == 1:
    print(-1)
else:
    base = [2,1]
    actual = 0
    while actual < n:
        print(base[0], base[1], end=" ")
        base[0] += 2
        base[1] += 2
        actual += 2
    print()
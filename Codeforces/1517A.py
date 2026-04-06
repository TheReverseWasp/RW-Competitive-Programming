def decompose(n):
    runner = 2050
    i = 1
    while runner <= n:
        runner *= 10
    runner //= 10
    if runner == 205:
        return -1, -1
    return i, n-runner
tc = int(input())
for _ in range(tc):
    n = int(input())
    acum = 0
    while n > 0:
        temp, new_n = decompose(n)
        acum += temp
        n = new_n + 0
    if n == 0:
        print(acum)
    else:
        print(n)


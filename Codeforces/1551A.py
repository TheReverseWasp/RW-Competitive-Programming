tc = int(input())
for __ in range(tc):
    n = int(input())
    if n == 1:
        print(1,0)
        continue
    if n == 2:
        print(0, 1)
        continue
    _1 = n // 3
    _2 = (n - _1) // 2
    if _1 + _2 * 2 < n:
        _1 += 1
    print(_1, _2)

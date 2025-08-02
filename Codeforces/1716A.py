tc = int(input())
for __ in range(tc):
    n = int(input())
    if n == 1:
        print(2)
        continue
    if n % 3 == 0:
        print(n // 3)
        continue
    else:
        print((n // 3) + 1)
        continue
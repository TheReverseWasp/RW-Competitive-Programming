tc=int(input())
for _ in range(tc):
    n = int(input())
    temp = 1
    while temp <= n:
        temp *= 2
    temp //= 2
    print(temp)
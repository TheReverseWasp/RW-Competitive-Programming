tc = int(input())
for _ in range(tc):
    n = int(input())
    if n % 4 == 0:
        temp = n // 4
        print(temp, temp, temp, temp)
        continue
    else:
        print(n-3,1,1,1)
tc = int(input())
for _ in range(tc):
    n = int(input())
    if n <= 3:
        print(n)
    else:
        print(n % 2)
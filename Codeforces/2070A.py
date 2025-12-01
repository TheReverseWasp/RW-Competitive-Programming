tc = int(input())
for _ in range(tc):
    n = int(input())
    acum = n % 15
    if acum >= 2:
        acum = 3
    else:
        acum += 1
    print(n//15 * 4 - (n//15) + acum)
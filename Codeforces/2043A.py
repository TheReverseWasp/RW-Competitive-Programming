tc = int(input())
for _ in range(tc):
    n = int(input())
    coins = 1
    while n > 3:
        n //= 4
        coins *= 2
    print(coins)
tc = int(input())
for __ in range(tc):
    n = int(input())
    coins = [2**i for i in range(1,n+1)]
    set_1 = [coins[-1]]
    for i in range(n//2 - 1):
        set_1.append(coins[i])
    sum_a = sum(set_1)
    sum_b = sum(coins) - sum_a
    print(abs(sum_a - sum_b))
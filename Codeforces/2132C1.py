tc = int(input())
for __ in range(tc):
    n = int(input())
    total_cost = 0
    while n > 0:
        i = 0
        while 3**i <= n:
            i+=1
        i-=1
        n-=3**i
        total_cost+=(3**(i+1))+(i*(3**(i-1)))
    print(int(total_cost))

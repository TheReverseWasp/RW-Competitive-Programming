tc = int(input())
for __ in range(tc):
    n = int(input())
    ans, actual, acum = 0,1,0
    n-=actual
    ans+=1
    acum += 1
    while n > 0:
        actual += 2
        ans += 1
        n-=actual
        acum += actual
    print(ans)
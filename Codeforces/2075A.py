tc = int(input())
for _ in range(tc):
    n,k = map(int,input().split())
    ans = 0
    while n > 0:
        if n <= k:
            n = 0
            ans += 1
        else:
            if n % 2 == 1:
                n-=k
                ans += 1
            else:
                ans += n//(k-1)
                n%=k-1
    print(ans)

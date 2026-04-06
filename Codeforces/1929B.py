tc = int(input())
for _ in range(tc):
    n,k= map(int,input().split())
    maxo = 4*n-2
    if k <= n*2:
        print((k+1)//2)
    else:
        ans = n
        if k == maxo:
            ans = 2*n
        else:
            k -= ans*2
            if k > 0:
                ans += (k+1) // 2
        print(ans)
tc = int(input())
for _ in range(tc):
    n,l,r,k = map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    ans = 0
    for choco in a:
        if choco > k:
            break
        else:
            if l <= choco and choco <= r:
                k-=choco
                ans+=1
    print(ans)
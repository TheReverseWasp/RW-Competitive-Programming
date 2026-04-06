tc=int(input())
for __ in range(tc):
    i,e,u=map(int,input().split())
    ans = i + 0
    if e%3==0:
        ans+=e//3
        ans+=u//3+(1 if u%3 != 0 else 0)
    else:
        needed=3-e%3
        if u < needed:
            ans = -1
        else:
            u-=needed
            e+=needed
            ans+=e//3
            ans+=u//3+(1 if u%3 != 0 else 0)
    print(ans)
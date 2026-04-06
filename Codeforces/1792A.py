tc=int(input())
for __ in range(tc):
    n =int(input())
    a=list(map(int,input().split()))
    ones = a.count(1)
    ans = ones // 2 + (1 if ones % 2 == 1 else 0)
    for monster in a:
        if monster != 1:
            ans+=1
    print(ans)
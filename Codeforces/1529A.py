tc=int(input())
for __ in range(tc):
    n=int(input())
    a=list(map(int,input().split()))
    mimic = min(a)
    ans = 0
    for elem in a:
        if elem>mimic:
            ans+=1
    print(ans)
tc = int(input())
for _ in range(tc):
    n,b,x,y = map(int,input().split())
    ans = [0]
    while len(ans)<=n:
        if ans[-1] + x <= b:
            ans.append(ans[-1] + x)
        else:
            ans.append(ans[-1] - y)
    print(sum(ans))
    ans.clear()
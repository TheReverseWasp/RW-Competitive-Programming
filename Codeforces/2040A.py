tc=int(input())
for _ in range(tc):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    win_absolute = False
    ans = -1
    for i in range(n):
        ai = a[i]
        win_round = True
        for j in range(n):
            if i == j:
                continue
            aj = a[j]
            if abs(a[i]-a[j]) % k == 0:
                win_round = False
                break
        if win_round:
            win_absolute = True
            ans = i + 1
            break
    if win_absolute:
        print("YES")
        print(ans)
    else:
        print("NO")
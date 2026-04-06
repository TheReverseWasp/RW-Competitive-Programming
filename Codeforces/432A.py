n,k = map(int,input().split())
v_l = list(map(int,input().split()))
v_l.sort()
i = 0
ans = 0
if n >= 3:    
    while i < n - 2:
        if v_l[i + 2] + k <= 5:
            ans += 1
        else:
            break
        i += 3
print(ans)
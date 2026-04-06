tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    count_2 = a.count(2)
    if count_2 % 2 == 1:
        print(-1)
    else:
        acum = 0
        ans = 1
        while ans < n:
            if a[ans-1] == 2:
                acum +=1
            if acum == count_2 // 2:
                break
            ans += 1
        print(ans)
    
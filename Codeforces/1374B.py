tc = int(input())
for __ in range(tc):
    n = int(input())
    ans = 0
    while n != 1:
        if n % 6 == 0:
            n//=6
            ans += 1
            continue
        else:
            if n % 3 == 0:
                n *= 2
                ans += 1
                continue
            else:
                break
    if n == 1:
        print(ans)
    else:
        print(-1)

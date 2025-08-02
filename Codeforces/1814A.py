tc = int(input())
for __ in range(tc):
    n,k = map(int,input().split())
    if n == 1:
        if k == 1:
            print("YES")
            continue
        else:
            print("NO")
            continue
    else:
        if n % 2 == 1:
            if k % 2 == 1 and k <= n:
                print("YES")
                continue
            else:
                print("NO")
                continue
        else:
            print("YES")
            continue
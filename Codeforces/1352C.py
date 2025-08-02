tc = int(input())
for __ in range(tc):
    n,k = map(int,input().split())
    ans = k + 0
    temp = k//n
    ans += temp
    k = k % n
    k += temp
    while temp != 0:
        temp = k // n
        ans += temp
        k = k % n
        k += temp
    print(ans)


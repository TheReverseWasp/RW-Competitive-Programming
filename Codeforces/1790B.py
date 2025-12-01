tc = int(input())
for __ in range(tc):
    n,s,r = map(int, input().split())
    ans = s-r
    print(ans, end=" ")
    s-=ans
    n-=1
    while n > 0:
        ans = s // n
        s-=ans
        n-=1
        print(ans, end=" ")
    print()
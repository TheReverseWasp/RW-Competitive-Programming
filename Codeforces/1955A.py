tc = int(input())
for __ in range(tc):
    n,a,b=map(int, input().split())
    ans = 0
    if n >= 2:
        if a * 2 < b:
            ans = a*2 * (n//2)
        else:
            ans = b * (n//2)
        n%=2
    ans += n*a
    print(ans)
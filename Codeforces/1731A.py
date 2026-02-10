tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 1
    for elem in a:
        ans *= elem
    ans += n-1
    print(ans*2022)
tc = int(input())
for _ in range(tc):
    n = int(input())
    ans = 0
    a = list(map(int,input().split()))
    for elem in a:
        ans |= elem
    print(ans)
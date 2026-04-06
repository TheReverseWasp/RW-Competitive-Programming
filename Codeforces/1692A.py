tc = int(input())
for i in range(tc):
    l = list(map(int,input().split()))
    ans = 0
    for j in range(1,4):
        ans += 1 if l[j] > l[0] else 0
    print(ans)
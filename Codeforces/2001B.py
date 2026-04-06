tc=int(input())
for _ in range(tc):
    n = int(input())
    if n%2 == 0:
        print(-1)
        continue
    ans = []
    for i in range(n,0,-2):
        ans.append(str(i))
    for i in range(2, n, 2):
        ans.append(str(i))
    print(" ".join(ans))
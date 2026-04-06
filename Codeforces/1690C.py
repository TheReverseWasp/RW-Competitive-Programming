tc = int(input())
for _ in range(tc):
    n = int(input())
    ans = list()
    s = list(map(int,input().split()))
    f = list(map(int,input().split()))
    curr = 0
    for i in range(n):
        dur = f[i] - max(curr, s[i])
        curr = f[i] + 0
        ans.append(dur)
    for elem in ans:
        print(elem, end=" ")
    print()
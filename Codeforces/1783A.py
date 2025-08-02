tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    if len(set(a)) == 1:
        print("NO")
        continue
    a.sort()
    print("YES")
    ans = list()
    for i in range(n//2):
        ans.append(a[i])
        ans.append(a[-1-i])
    if len(ans) < len(a):
        ans.append(a[n//2])
    for elem in ans:
        print(elem,end=" ")
    print()
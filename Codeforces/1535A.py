tc = int(input())
for __ in range(tc):
    a = list(map(int,input().split()))
    b = sorted(a)
    if (b[-1] in a[:2] and b[-2] in a[2:]) or  (b[-2] in a[:2] and b[-1] in a[2:]):
        print("YES")
    else:
        print("NO")

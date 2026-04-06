tc=int(input())
for _ in range(tc):
    n=int(input())
    a=list(map(int,input().split()))
    b = tuple(a)
    a.sort()
    if tuple(a) == b:
        print("NO")
    else:
        print("YES")
tc = int(input())
for _ in range(tc):
    n,m=map(int,input().split())
    s = sum(list(map(int,input().split())))
    if s == m:
        print("YES")
    else:
        print("NO")
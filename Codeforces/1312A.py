tc=int(input())
for _ in range(tc):
    n,m = map(int,input().split())
    if n%m == 0:
        print("YES")
    else:
        print("NO")
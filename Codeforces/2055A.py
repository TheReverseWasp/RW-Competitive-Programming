tc = int(input())
for i in range(tc):
    n,a,b = map(int,input().split())
    if abs(a-b) % 2 == 1:
        print("NO")
    else:
        print("YES")
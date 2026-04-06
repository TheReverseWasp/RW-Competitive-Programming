tc = int(input())
for __ in range(tc):
    n,j,k = map(int,input().split())
    a = list(map(int,input().split()))
    if k == 1 and a[j-1] != max(a):
        print("NO")
    else:
        print("YES")
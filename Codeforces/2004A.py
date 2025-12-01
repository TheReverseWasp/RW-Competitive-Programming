tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    if n > 2:
        print("NO")
        continue
    if abs(a[0] - a[1]) != 1:
        print("YES")
    else:
        print("NO") 
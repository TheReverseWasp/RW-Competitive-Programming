tc = int(input())
for __ in range(tc):
    n = int(input())
    a = sum(list(map(int,input().split())))
    if a % 2 == 0:
        print("YES")
    else:
        print("NO")

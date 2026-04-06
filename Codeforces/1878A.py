tc = int(input())
for __ in range(tc):
    n, mc = map(int,input().split())
    a = list(map(int,input().split()))
    if mc in a:
        print("YES")
    else:
        print("NO")

tc = int(input())
for _ in range(tc):
    n,m = map(int,input().split())
    a = sum(list(map(int,input().split())))
    if m >= a:
        print(0)
    else:
        print(a-m)
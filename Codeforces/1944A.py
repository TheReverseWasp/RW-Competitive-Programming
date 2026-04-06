tc = int(input())
for _ in range(tc):
    n, k = map(int,input().split())
    if k >= n-1:
        print(1)
    else:
        print(n)
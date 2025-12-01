tc = int(input())
for _ in range(tc):
    n, k = map(int,input().split())
    print(n*k - (k - 1))
tc = int(input())
for _ in range(tc):
    n,m = map(int,input().split())
    if n < m:
        n,m = m,n
    print(m*2 - 2 + n - (1 if n == 1 else 0))
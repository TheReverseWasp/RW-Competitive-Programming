tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    print((max(a) - min(a))*(n-1))
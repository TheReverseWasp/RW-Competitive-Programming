tc=int(input())
for _ in range(tc):
    n=int(input())
    a=list(map(int,input().split()))
    multiplier = max(a[0], max(a[1:]))
    print(multiplier*n)
                     
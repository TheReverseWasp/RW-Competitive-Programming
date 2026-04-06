tc = int(input())
for __ in range(tc):
    n,m = map(int,input().split())
    if m % 2 == 1:
        m-=1
    print((n*m)//2)
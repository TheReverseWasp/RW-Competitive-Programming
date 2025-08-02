tc = int(input())
for __ in range(tc):
    x,y,n = map(int,input().split())
    a = (n//x)*x + y
    b = (n//x - 1)*(x) + y
    if a > n:
        print(b)
    else:
        print(a)
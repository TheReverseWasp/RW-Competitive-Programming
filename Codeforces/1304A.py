tc = int(input())
for _ in range(tc):
    x,y,a,b = map(int,input().split())
    dist = abs(x-y)
    if dist % (a+b) == 0:
        print(dist//(a+b))
    else:
        print(-1)
tc = int(input())
for __ in range(tc):
    a,b,c,x,y = map(int,input().split())
    x-=min(x,a)
    y-=min(y,b)
    uni = x+y
    if c >= uni:
        print("YES")
    else:
        print("NO")
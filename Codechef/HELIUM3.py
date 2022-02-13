tc = int(input())

while tc:
    a,b,x,y = map(int,input().split())
    if a*b <= x*y:
        print("Yes")
    else:
        print("No")
    tc-=1

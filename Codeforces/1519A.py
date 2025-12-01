t=int(input())
for __ in range(t):
    r,b,d=map(int,input().split())
    r,b=min(r,b),max(r,b)
    if b <= r*(d+1):
        print("YES")
    else:
        print("NO")
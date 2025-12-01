t=int(input())
for __ in range(t):
    fruit=int(input())
    x,c=map(int,input().split())
    print(fruit//min(x,c) + (1 if fruit%min(x,c)>0 else 0))
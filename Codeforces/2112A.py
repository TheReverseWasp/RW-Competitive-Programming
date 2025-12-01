tc=int(input())
for _ in range(tc):
    a,x,y=list(map(int,input().split()))
    if (a >= x and y >= a) or (a <= x and y <= a): 
        print("NO")
    else:
        print("YES")
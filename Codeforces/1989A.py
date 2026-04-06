n = int(input())
for __ in range(n):
    x,y = map(int,input().split())
    if y <= -2:
        print("NO")
    else:
        print("YES")
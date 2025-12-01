tc = int(input())
for _ in range(tc):
    x,y,k = map(int,input().split())
    if x <= y:
        x = min(x+k, y)
    print(y + max(x,y)-min(x,y))
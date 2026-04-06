tc = int(input())
for _ in range(tc):
    x,y=map(int,input().split())
    if y % x == 0:
        print(1, y//x)
    else:
        print(0,0)
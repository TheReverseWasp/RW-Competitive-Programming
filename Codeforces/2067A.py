tc = int(input())
for _ in range(tc):
    x,y=map(int,input().split())
    if x + 1 >= y and (x + 1 - y) % 9== 0:
        print("yes")
        continue
    print("no")
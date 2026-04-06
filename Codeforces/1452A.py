for _ in range(int(input())):
    x,y=map(int,input().split())
    if x == y:
        print(x+y)
        continue
    else:
        print(max(x,y)*2-1)
tc = int(input())
while tc:
    x, y = map(int,input().split())
    if x < y:
        print("BIKE")
    elif y < x:
        print("CAR")
    else:
        print("SAME")
    tc-=1

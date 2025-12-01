tc = int(input())
for _ in range(tc):
    a,b,c,d = map(int,input().split())
    jelly_chose = min(b,d)
    flower_chose = min(a,c)
    if jelly_chose >flower_chose:
        print("Flower")
    else:
        print("Gellyfish")
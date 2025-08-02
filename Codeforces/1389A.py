from copy import copy
def lcm(a,b):
    x = copy(a)
    y = copy(b)
    if x > y:
       greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

tc = int(input())
for __ in range(tc):
    l,r = map(int,input().split())
    x,y = l, l * 2
    if y <= r:
        print(x,y)
    else:
        print(-1,-1)
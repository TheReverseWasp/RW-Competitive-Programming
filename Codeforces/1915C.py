import math
tc = int(input())
for __ in range(tc):
    input()
    sq_area = sum(list(map(int,input().split())))
    sq =  int(math.sqrt(sq_area))
    if sq * sq == sq_area:
        print("YES")
    else:
        print("NO")
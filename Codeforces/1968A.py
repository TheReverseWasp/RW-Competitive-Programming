import math
tc = int(input())
for __ in range(tc):
    x = int(input())
    max_ope = 0
    ans = 1
    for y in range(1, x):
        res = math.gcd(x,y)+ y
        if res > max_ope:
            max_ope = res + 0
            ans = y + 0
    print(ans)
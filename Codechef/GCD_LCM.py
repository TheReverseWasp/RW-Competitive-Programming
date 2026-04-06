import math

t = int(input())
while t:
    t-=1
    x, c = map(int, input().split())
    if x == 1 or c == 1:
        print(1)
    else:
        temp = 2
        l = []
        while temp ** c <= x:
            l.append((temp**c * x /(math.gcd(temp ** c, x)))/math.gcd(temp ** c, x))
            temp += 1
        l.append((temp**c * x /(math.gcd(temp ** c, x)))/math.gcd(temp ** c, x))
        print(int(min(l + [x])))

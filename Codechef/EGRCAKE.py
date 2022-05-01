import math

t = int(input())
while t:
    t-=1
    n,m = map(int, input().split())
    gcd_ = math.gcd(n,m)
    if gcd_ == 1 and n == 1:
        print("Yes")
    elif gcd_ == 1:
        print("Yes")
    else:
        print(f"No {int(n/gcd_)}")
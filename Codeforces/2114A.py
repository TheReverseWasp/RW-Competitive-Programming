import math

tc = int(input())
for __ in range(tc):
    n = int(input())
    sq = int(math.sqrt(n))
    if sq * sq != n:
        print(-1)
        continue
    print(0,sq)
    
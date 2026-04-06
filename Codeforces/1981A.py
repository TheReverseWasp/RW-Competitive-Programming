import math
tc=int(input())
for _ in range(tc):
    l,r = map(int,input().split())
    print(int(math.log2(r)))
import math
tc = int(input())
for i in range(tc):
    a,b,c = map(int, input().split())
    diff = abs(a-b) / 2
    ans = math.ceil(diff/c)
    print(ans)
import math
tc=int(input())
for _ in range(tc):
    x,y = map(int,input().split())
    if x == 0 and y==0:
        print(0)
        continue
    euclidean_d = math.sqrt(x**2 + y**2)
    euclidean_d_int = euclidean_d//1
    if euclidean_d == euclidean_d_int:
        print(1)
    else:
        print(2)

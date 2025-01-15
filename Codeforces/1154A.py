import copy as cp

x = list(map(int,input().split()))
x.sort()
b = (x[0] - x[1] + x[2]) // 2
a = (x[0] + x[1] - x[2]) // 2
c = (x[2] + x[1] - x[0]) // 2
print(a,b,c) 
import math

n,m,a = map(float,input().split(" "))
print(math.ceil(int(math.ceil(n / a) * a * math.ceil(m / a) * a) / int(a*a)))
import math

t = int(input())
while t:
    t-=1
    n = int(input())
    l = list(map(int, input().split()))
    for i in range(1, n, 2):
        if i == n-1:
            break
        if math.gcd(l[i-1],l[i]) == 1 or math.gcd(l[i],l[i+1]) == 1:
            l[i] = l[i +1] * l[i -1]
    if math.gcd(l[n-1], l[n-2]) == 1:
        l[n-1] = l[n-2]
    print(" ".join([str(i) for i in l]))

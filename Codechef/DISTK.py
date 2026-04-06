import numpy as np

tc = int(input())
while tc:
    n, k = map(int, input().split())
    k-=n
    l = []
    arr = np.ones(n)
    while k:
        if len(l) < n:
            if len(l) == 0 or l[0] == 0:
                l = [1] + l
            else:
                l = [0] + l
        else:
            
    tc-=1

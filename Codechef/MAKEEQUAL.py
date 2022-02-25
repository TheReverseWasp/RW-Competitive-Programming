from operator import itemgetter
import numpy as np
t = int(input())
while t:
    t-=1
    n = int(input())
    l = list(map(int, input().split()))
    max_ = max(l)
    min_ = min(l)
    print(max_ - min_)

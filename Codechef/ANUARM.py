import numpy as np

t= int(input())
while t:
    t-=1
    n, m =map(int, input().split())
    a = list(map(int, input().split()))
    
    minmax =[1000000, -1]

    for soldier in a:
        if soldier > minmax[1]:
            minmax[1] = soldier
        if soldier < minmax[0]:
            minmax[0] = soldier

    for i in range(n):
        print(max(abs(minmax[0] - i), abs(minmax[1] - i)), sep=" ")
    print()

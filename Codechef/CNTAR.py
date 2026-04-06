import numpy as np

tc = int(input())
while tc:
    n,m = map(int, input().split())
    A = list(map(int, input().split()))
    sA = set(A)
    answer = 1
    for i in range(m, m-len(sA), -1):
        answer *= i
    print(answer%1000000007)

    tc-=1

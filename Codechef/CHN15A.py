import numpy as np

tc = int(input())
while tc:
    n, k = map(int, input().split())
    a = np.array(list(map(int, input().split())))
    a += k
    answer = 0
    for i in a:
        if i%7 == 0:
            answer +=1
    print(answer)
    tc-=1

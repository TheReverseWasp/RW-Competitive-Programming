tc = int(input())
import numpy as np
while tc:
    tc -= 1
    n, k = map(int, input().split())
    answer = np.zeros(n)
    used_numbers = set()
    i = 0
    temp = k + 0
    while k > 0:
        answer[i] = i + 1
        i+=1
        k-=1
    if answer[n-1] == 0:
        answer[n-1] = i + 1
        i+=1
        while i < n:
            answer[i - 1] = i + 1
            i+=1
    if temp == n -1:
        answer[0] = 2
        answer[1] = 1
    answer = list(answer)
    answer = [str(int(elem)) for elem in answer]
    print(" ".join(answer))

def comb(n, k):
    if n < k:
        return 0
    ans = 1
    for i in range(k + 1, n + 1):
        ans *= i
    temp = 1
    for i in range(2, n - k + 1):
        temp *= i
    return ans / temp


t = int(input())

while t:
    t-=1
    n = int(input())
    l = list(map(int, input().split()))
    twos = 0
    zeros = 0
    for elem in l:
        if elem == 2:
            twos += 1
        if elem == 0:
            zeros += 1
    print(int(comb(twos, 2))+ int(comb(zeros, 2)))

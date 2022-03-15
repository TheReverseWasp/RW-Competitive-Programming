import numpy as np

t= int(input())
while t:
    t-=1
    n, m =map(int, input().split())
    a = list(map(int, input().split()))
    ans = np.ones(n) * -1
    s = set()
    while len(s) < n:
        temp_s = set()
        for elem in a:
            if not elem in s:
                ans[elem] = m - 1
                s.add(elem)
                temp_s.add(max(0, elem - 1))
                temp_s.add(min(n - 1, elem + 1))
        a = list(temp_s)
        m += 1
    for elem in ans:
        print(int(elem), end = " ")

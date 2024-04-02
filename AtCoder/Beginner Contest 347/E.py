import numpy as np
n, q = map(int, input().split())
queries = list(map(int, input().split()))

ans = np.zeros(n)
s = set()
for elem in queries:
    if elem in s:
        s.remove(elem)
    else:
        s.add(elem)
    
    for elem in s:
        ans[elem - 1] += len(s)

for elem in ans:
    print(int(elem), end=" ")
print()
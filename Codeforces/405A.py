n = int(input())
nl = list(map(int, input().split()))
nl.sort()
for i in range(n):
    print(nl[i], end=" ")
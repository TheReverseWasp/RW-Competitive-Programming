tc = int(input())
for __ in range(tc):
    n,d = map(int,input().split())
    s = input()
    maxo = 0
    for i in range(n + 1):
        maxo = max(int(s[:i] + str(d) + s[i:]), maxo)
    print(maxo)
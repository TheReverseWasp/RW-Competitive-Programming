tc = int(input())
for __ in range(tc):
    n = int(input())
    s = list(map(int,input().split()))
    s.sort()
    min_diff = 99999999
    for i in range(n-1):
        temp = abs(s[i + 1] - s[i])
        if temp < min_diff:
            min_diff = temp + 0
    print(min_diff)

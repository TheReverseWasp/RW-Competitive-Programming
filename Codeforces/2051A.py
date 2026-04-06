tc = int(input())
for __ in range(tc):
    days = int(input())
    mon = list(map(int,input().split()))
    ste = list(map(int,input().split()))
    ste.append(0)
    max_diff = 0
    for i in range(days):
        diff = mon[i] - ste[i + 1]
        if diff > 0:
            max_diff += diff
    print(max_diff)

tc = int(input())
for __ in range(tc):
    n = int(input())
    excluded = set()
    mini, maxi = 1, 999999999999
    for i in range(n):
        opcion, val = map(int,input().split())
        if opcion == 1:
            if val > mini:
                mini = val + 0
        if opcion == 2:
            if val < maxi:
                maxi = val + 0
        if opcion == 3:
            excluded.add(val + 0)
    ans = maxi - mini + 1
    for elem in excluded:
        if elem >= mini and elem <= maxi:
            ans -= 1
    print(max(ans,0))
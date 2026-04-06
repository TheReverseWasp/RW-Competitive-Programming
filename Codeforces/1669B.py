tc = int(input())
for __ in range(tc):
    n = input()
    arr = list(map(int,input().split()))
    db = {}
    ans = -1
    for elem in arr:
        if not elem in db:
            db[elem] = 0
        db[elem] += 1
        if db[elem] == 3:
            ans = elem
            break
    print(ans)
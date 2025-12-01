tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    db = {}
    for elem in a:
        if not elem in db:
            db[elem] = 0
        db[elem] += 1
    ans = 0
    for val in db.values():
        ans += val // 2
    print(ans)
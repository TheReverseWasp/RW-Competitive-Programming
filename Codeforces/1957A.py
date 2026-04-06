tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    db = dict()
    for elem in a:
        if not elem in db:
            db[elem] = 0
        db[elem] += 1
    ans = 0
    for value in db.values():
        ans += value//3
    print(ans)
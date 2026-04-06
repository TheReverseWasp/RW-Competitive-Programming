tc = int(input())
for _ in range(tc):
    n,c=map(int,input().split())
    db = dict()
    a = list(map(int,input().split()))
    for elem in a:
        if not elem in db:
            db[elem] = 1
        else:
            db[elem] += 1
    cost = 0
    for value in db.values():
        cost += min(value, c)
    print(cost)
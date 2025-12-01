tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    db = dict()
    for elem in a:
        if not elem in db:
            db[elem] = 0
        db[elem] += 1
    flag = False
    for v in db.values():
        if v >=2:
            flag = True
            break
    if flag:
        print("yes")
    else:
        print("no")
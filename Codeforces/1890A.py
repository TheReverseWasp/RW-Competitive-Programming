tc = int(input())
for __ in range(tc):
    n = int(input())
    b = list(map(int,input().split()))
    db = {}
    for elem in b:
        if not elem in db:
            db[elem] = 0
        db[elem] += 1
    if len(db) > 2:
        print("NO")
    else:
        if len(db) == 1:
            print("YES")
            continue
        val_db = list()
        for value in db.values():
            val_db.append(value)
        if abs(val_db[0] - val_db[1]) <= 1:
            print("YES")
        else:
            print("NO")
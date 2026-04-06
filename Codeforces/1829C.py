tc = int(input())
for __ in range(tc):
    n = int(input())
    db = {}
    for i in range(n):
        cost, learning = input().split()
        cost = int(cost)
        if learning == "00":
            continue
        if not learning in db:
            db[learning] = cost
        else:
            db[learning] = min(db[learning], cost)
    if len(db.keys()) == 3:
        if db["11"] <= db["01"] + db["10"]:
            print(db["11"])
        else:
            print(db["01"] + db["10"])
    elif len(db.keys()) == 2:
        if "11" in db:
            print(db["11"])
        else:
            print(db["01"] + db["10"])
    elif len(db.keys()) == 1:
        if "11" in db:
            print(db["11"])
        else:
            print(-1)
    else:
        print(-1)
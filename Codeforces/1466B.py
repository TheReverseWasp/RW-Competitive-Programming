tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    db = set()
    for elem in a:
        if elem in db:
            if elem + 1 in db:
                continue
            else:
                db.add(elem+1)
        else:
            db.add(elem)
    print(len(db))
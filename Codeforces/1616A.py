tc = int(input())
for _ in range(tc):
    n=int(input())
    a=list(map(int,input().split()))
    db = set()
    for elem in a:
        if elem in db:
            if elem == 0:
                continue
            else:
                db.add(-elem)
        else:
            db.add(elem)
    print(len(db))
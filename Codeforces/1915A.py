tc = int(input())
for i in range(tc):
    l = list(map(int,input().split()))
    db = {}
    for i in range(3):
        if not l[i] in db:
            db[l[i]] = list()
        db[l[i]].append(i + 1)
    for k,v in db.items():
        if len(v) == 1:
            print(k)
            break
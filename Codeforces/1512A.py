tc = int(input())
for i in range(tc):
    n = int(input())
    ag_l = list(map(int,input().split()))
    db = {}
    for i in range(n):
        if not ag_l[i] in db:
            db[ag_l[i]] = list()
        db[ag_l[i]].append(i)
    for k,v in db.items():
        if len(v) == 1:
            print(v[0] + 1)
            break
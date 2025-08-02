tc = int(input())
for __ in range(tc):
    n = int(input())
    l = list(map(int,input().split()))
    db = {}
    for i in range(n):
        if not l[i] in db:
            db[l[i]] = 0
        db[l[i]] += 1
    flag = True
    for v in db.values():
        if v > 1:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")

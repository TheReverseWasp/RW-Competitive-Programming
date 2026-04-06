tc=int(input())
for _ in range(tc):
    n=int(input())
    a=list(map(int,input().split()))
    db=dict()
    for elem in a:
        if not elem in db:
            db[elem] = 0
        db[elem] += 1
    min_item = 999
    for k,v in db.items():
        min_item = min(min_item,k)
    print(len(a)-db[min_item])
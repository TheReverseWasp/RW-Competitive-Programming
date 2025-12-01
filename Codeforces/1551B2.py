tc = int(input())
for __ in range(tc):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    colors = list()
    db = dict()
    for num in a:
        if not num in db:
            db[num] = 0
        if db[num] == k:
            continue
        else:
            db[num] += 1
    
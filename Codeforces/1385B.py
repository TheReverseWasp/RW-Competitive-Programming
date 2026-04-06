tc = int(input())
for __ in range(tc):
    n = int(input())
    p = list(map(int,input().split()))
    db = set()
    perm = list()
    for elem in p:
        if elem in db:
            continue
        db.add(elem)
        perm.append(elem)
    for elem in perm:
        print(elem,end=" ")
    print()
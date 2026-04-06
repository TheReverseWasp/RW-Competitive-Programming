tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    db = set()
    for elem in a:
        db.add(elem%2)
    if len(db) == 1:
        print("YES")
    else:
        if min(a) % 2 == 1:
            print("YES")
            continue
        else:
            print("NO")
            continue
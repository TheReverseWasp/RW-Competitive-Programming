n,k = map(int,input().split())
a = list(map(int,input().split()))
db = dict()
for idx, elem in enumerate(a):
    if not elem in db:
        db[elem] = list()
    db[elem].append(idx+1)

if len(db) >= k:
    print("YES")
    counter = 0
    for v in db.values():
        counter += 1
        print(v[0], end=" ")
        if counter == k:
            break
    print()
else:
    print("NO")
tc = int(input())
for _ in range(tc):
    l,a,b = map(int,input().split())
    db = set()
    db.add(a)
    new_one = (a + b) % l
    while not new_one in db:
        db.add(new_one)
        new_one = (new_one + b) % l
    print(max(db))
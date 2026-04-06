tc = int(input())
for _ in range(tc):
    db = set()
    a = input()
    for elem in a:
        db.add(elem)
    a = input()
    for elem in a:
        db.add(elem)
    if len(db) == 1:
        print(0)
    elif len(db) == 2:
        print(1)
    elif len(db) == 3:
        print(2)
    else:
        print(3)
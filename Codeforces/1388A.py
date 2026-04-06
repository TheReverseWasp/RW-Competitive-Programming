tc = int(input())
for _ in range(tc):
    n = int(input())
    if n <= 30:
        print("NO")
        continue
    else:
        print("YES")
        db = set([6,10,14])
        if n - 30 in db:
            db.remove(10)
            db.add(15)
            db.add(n-35)
        else:
            db.add(n-30)
        for elem in db:
            print(elem, end=" ")
        print()
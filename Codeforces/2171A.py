tc = int(input())
for _ in range(tc):
    db = set()
    n = int(input())
    if n % 2 != 0:
        print(0)
        continue
    chickens, cows = n//2, 0
    db.add((chickens+0,cows+0))
    while chickens > 1:
        chickens-=2
        cows+=1
        if not (cows, chickens) in db:
            db.add((chickens+0,cows+0))
    print(len(db))

tc = int(input())
for __ in range(tc):
    a = input()
    db = dict()
    for letter in a:
        if not letter in db:
            db[letter] = 0
        db[letter] += 1
    valid_pairs = 0
    for v in db.values():
        if v>=2:
            valid_pairs += 1
    if valid_pairs > 1:
        print("yes")
    else:
        print("no")
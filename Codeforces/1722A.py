tc = int(input())
for __ in range(tc):
    n = int(input())
    s = input()
    if n != 5:
        print("NO")
        continue
    db = set()
    for letter in s:
        if not letter in db:
            db.add(letter)

    if "T" in db and "i" in db and "m" in db and "u" in db and "r" in db:
        print("YES")
    else:
        print("NO")

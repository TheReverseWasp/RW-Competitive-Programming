tc = int(input())
for __ in range(tc):
    s = input()
    db = set()
    days = 0
    for letter in s:
        db.add(letter)
        if len(db) == 4:
            db.clear()
            db.add(letter)
            days+=1
    days += 1
    print(days)
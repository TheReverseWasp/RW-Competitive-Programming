lol = input()
lol += input()
antilol = input()
db = {}
for i in range(len(lol)):
    if not lol[i] in db:
        db[lol[i]] = 0
    db[lol[i]] += 1

pansery_the_reno = True
for i in range(len(antilol)):
    if not antilol[i] in db:
        pansery_the_reno = False
        break
    db[antilol[i]] -= 1

if not pansery_the_reno:
    print("NO")
else:
    for v in db.values():
        if v != 0:
            pansery_the_reno = False
            break
    if pansery_the_reno:
        print("YES")
    else:
        print("NO")
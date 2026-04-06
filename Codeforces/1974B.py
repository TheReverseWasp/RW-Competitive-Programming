tc = int(input())
for __ in range(tc):
    n = int(input())
    s = input()
    db = set()
    for elem in s:
        db.add(elem)
    db = list(db)
    db.sort()
    translator = {}
    for i in range(len(db)):
        letter = db[i]
        translation = db[len(db) - 1 - i]
        translator[letter] = translation 
        translator[translation] = letter 
    ans = ""
    for elem in s:
        ans += translator[elem]
    print(ans)

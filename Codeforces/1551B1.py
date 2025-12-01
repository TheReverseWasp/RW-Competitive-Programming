tc = int(input())
for __ in range(tc):
    s = input()
    db = dict()
    for letter in s:
        if not letter in db:
            db[letter] = 0
        if db[letter] == 2:
            continue
        else:
            db[letter]+=1
    temp = 0
    for val in db.values():
        temp+=val
    if temp % 2 == 1:
        temp-=1
    ans = temp // 2
    print(ans)
tc = int(input())
for _ in range(tc):
    n = input()
    db = {}
    for elem in n:
        if not elem in db:
            db[elem] = 1
        else:
            db[elem] +=1
    if len(db) >= 3:
        print(4)
    elif len(db) == 1:
        print(-1)
    else:
        flag_pair = False
        for k, v in db.items():
            if v == 2:
                flag_pair = True
            else:
                break
        if flag_pair:
            print(4)
        else:
            print(6)
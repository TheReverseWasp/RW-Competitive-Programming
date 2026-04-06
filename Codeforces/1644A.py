tc = int(input())
for _ in range(tc):
    s = input()
    db = set()
    flag = True
    for elem in s:
        if elem in "rgb":
            db.add(elem)
        else:
            if elem.lower() in db:
                continue
            else:
                flag=False
                break
    if flag:
        print("YES")
    else:
        print("NO")
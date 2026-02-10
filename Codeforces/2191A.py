tc=int(input())
for _ in range(tc):
    n=int(input())
    db = dict()
    a=list(map(int,input().split()))
    for idx, elem in enumerate(a):
        if idx % 2 == 0:
            db[elem] = True
        else:
            db[elem] = False
    a.sort()
    ans = True
    for idx, elem in enumerate(a):
        color = idx % 2 == 0
        if db[elem] == color:
            continue
        else:
            ans = False
            break
    if not ans:
        new_ans = True
        for idx, elem in enumerate(a):
            color = idx % 2 == 1
            if db[elem] == color:
                continue
            else:
                new_ans = False
                break
        ans = ans or new_ans
    if ans:
        print("YES")
    else:
        print("NO")
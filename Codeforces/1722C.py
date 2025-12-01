tc = int(input())
for __ in range(tc):
    n = int(input())
    db = {}
    a_score, b_score, c_score = 0,0,0
    a = set(list(input().split()))
    b = set(list(input().split()))
    c = set(list(input().split()))
    ## A
    for elem in a:
        if elem in db:
            a_score += db[elem]
        else:
            temp = 0
            if not elem in b and not elem in c:
                db[elem] = 3
                temp = 3
            elif not elem in b or not elem in c:
                db[elem] = 1
                temp = 1
            else:
                db[elem] = 0
                temp = 0
            a_score+=temp
    ## B
    for elem in b:
        if elem in db:
            b_score += db[elem]
        else:
            temp = 0
            if not elem in a and not elem in c:
                db[elem] = 3
                temp = 3
            elif not elem in a or not elem in c:
                db[elem] = 1
                temp = 1
            else:
                db[elem] = 0
                temp = 0
            b_score+=temp
    ## C
    for elem in c:
        if elem in db:
            c_score += db[elem]
        else:
            temp = 0
            if not elem in b and not elem in a:
                db[elem] = 3
                temp = 3
            elif not elem in b or not elem in a:
                db[elem] = 1
                temp = 1
            else:
                db[elem] = 0
                temp = 0
            c_score+=temp

    print(a_score,b_score,c_score)
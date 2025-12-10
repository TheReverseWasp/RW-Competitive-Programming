tc = int(input())
for _ in range(tc):
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    db = {"even":[0,0], "odd":[0,0]}
    for elem in a:
        if elem % 2 == 0:
            db["even"][0]+=elem
            db["even"][1]+=1
        else:
            db["odd"][0]+=elem
            db["odd"][1]+=1
    for __ in range(q):
        typo, xj = map(int,input().split())
        if typo == 0:
            db["even"][0] += db["even"][1] * xj
            if xj % 2 == 1:
                db["odd"][0] += db["even"][0]
                db["odd"][1] += db["even"][1]
                db["even"] = [0, 0]
        else:
            db["odd"][0] += db["odd"][1] * xj
            if xj % 2 == 1:
                db["even"][0] += db["odd"][0]
                db["even"][1] += db["odd"][1]
                db["odd"] = [0, 0]

        print(db["even"][0] + db["odd"][0])
tc = int(input())
for __ in range(tc):
    r,c = map(int,input().split())
    db = list()
    for i in range(r):
        db.append(input())
    ans = db[-1].count("D")
    for i in range(r):
        if db[i][-1] == "R":
            ans+=1

    print(ans)
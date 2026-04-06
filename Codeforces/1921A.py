tc = int(input())
for __ in range(tc):
    db = set()
    for ___ in range(4):
        a, b = map(int,input().split())
        db.add(a)
    temp = list(db)
    ans = abs(temp[0] - temp[1])**2
    print(ans)
    db.clear()
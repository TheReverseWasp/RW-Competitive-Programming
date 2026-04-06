tc = int(input())
for __ in range(tc):
    n,m = map(int,input().split())
    db = [0]
    for i in range(n):
        db.append(db[-1] + len(input()))
    ans = -1
    for elem in db:
        if elem > m:
            break
        else:
            ans += 1
    print(ans)
tc=int(input())
for _ in range(tc):
    n,m = map(int,input().split())
    a=list(map(int,input().split()))
    db = set()
    for idx in a:
        if idx-1 < m-idx and not idx-1 in db:
            db.add(idx-1)
        elif idx-1 < m-idx and idx-1 in db:
            db.add(m-idx)
        elif idx-1 >= m - idx and not m - idx in db:
            db.add(m-idx)
        else:
            db.add(idx-1)
    ans = ""
    for i in range(m):
        if i in db:
            ans+="A"
        else:
            ans+="B"
    print(ans)
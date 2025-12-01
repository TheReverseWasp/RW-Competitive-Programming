tc = int(input())
for _ in range(tc):
    n,k=map(int,input().split())
    db = [k]
    if k != 1:
        while db[-1] < 1000000009:
            db.append(db[-1]*k)
    ans = 0
    db.reverse()
    db.append(1)
    while n > 0:
        for powerade in db:
            if powerade > n:
                pass
            else:
                ans += n // powerade
                n %= powerade
    print(ans) 
